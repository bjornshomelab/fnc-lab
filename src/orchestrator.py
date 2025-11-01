"""
Main orchestrator for the Medveten AI experiment.
Coordinates LLM interactions, coherence modules, and data logging.
"""

import json
import uuid
import time
import logging
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

import yaml
import requests
# from sentence_transformers import SentenceTransformer

from coherence_module import CoherenceModule
from evaluator import Evaluator
from safety import SafetyMonitor
from data_collector import ConsciousnessDataCollector


class MedvetenOrchestrator:
    """Main orchestrator for consciousness experiments with Ollama LLM."""

    def __init__(self, config_path: str = "config.yaml"):
        """Initialize the orchestrator with configuration."""
        self.config = self._load_config(config_path)
        self.session_id = str(uuid.uuid4())
        self.turn_count = 0

        # Initialize components
        # Use None for embedding model - will be handled by evaluator if needed
        self.embedding_model = None  # SentenceTransformer('all-MiniLM-L6-v2')
        self.coherence_module = CoherenceModule(self.config['coherence'])
        self.evaluator = Evaluator(self.config['evaluation'])
        self.safety_monitor = SafetyMonitor(self.config['safety'])

        # Initialize data collection
        self.data_collector = ConsciousnessDataCollector("data")
        self.current_session_id = None

        # Session state
        self.conversation_history = []
        self.self_summary = "I am a research AI participating in a consciousness experiment."

        # Setup logging
        self._setup_logging()

        logging.info(f"Medveten AI session {self.session_id} initialized")

    def start_data_collection(self, researcher: str = "Björn Wikström",
                             test_type: str = "Interactive", notes: str = ""):
        """Start systematic data collection for this session."""
        model_name = self.config['ollama']['model']
        model_version = self.config['ollama'].get('fallback_model', 'unknown')
        temperature = self.config['ollama']['temperature']

        self.current_session_id = self.data_collector.start_session(
            researcher=researcher,
            test_type=test_type,
            model_name=model_name,
            model_version=model_version,
            temperature=temperature,
            session_notes=notes
        )

        logging.info(f"Started data collection session: {self.current_session_id}")
        return self.current_session_id

    def end_data_collection(self, fnc_notes: str = ""):
        """End data collection and generate analysis."""
        if self.current_session_id:
            self.data_collector.complete_session(self.current_session_id, fnc_notes)

            # Generate reports
            csv_path = self.data_collector.export_session_csv(self.current_session_id)
            fnc_report = self.data_collector.generate_fnc_report(self.current_session_id)

            logging.info(f"Data collection completed. Reports: {csv_path}, {fnc_report}")

            session_id = self.current_session_id
            self.current_session_id = None
            return session_id
        return None

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _setup_logging(self):
        """Setup logging configuration."""
        log_dir = Path(self.config['paths']['logs_dir'])
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file = log_dir / f"session_{self.session_id}.log"

        logging.basicConfig(
            level=getattr(logging, self.config['logging']['level']),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

    def _call_ollama(self, prompt: str, model: str = None) -> str:
        """Make API call to local Ollama instance with streaming support."""
        model_to_use = model or self.config['ollama']['model']
        url = f"{self.config['ollama']['base_url']}/api/generate"

        payload = {
            "model": model_to_use,
            "prompt": prompt,
            "stream": True,  # Enable streaming for real-time feedback
            "options": {
                "temperature": self.config['ollama']['temperature'],
                "num_predict": self.config['ollama']['max_tokens']
            }
        }

        try:
            # Prepare headers for cloud models
            headers = {"Content-Type": "application/json"}

            # Add API key for cloud models if available
            import os
            api_key = os.getenv('OLLAMA_API_KEY')
            if api_key and ':cloud' in model_to_use:
                headers["Authorization"] = f"Bearer {api_key}"

            print(f"🤖 {model_to_use} thinking", end="", flush=True)

            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=self.config['ollama']['timeout'],
                stream=True  # Enable response streaming
            )
            response.raise_for_status()

            # Handle streaming response
            full_response = ""
            dot_count = 0

            for line in response.iter_lines():
                if line:
                    try:
                        chunk = json.loads(line.decode('utf-8'))

                        # Add response chunk
                        if 'response' in chunk:
                            chunk_text = chunk['response']
                            full_response += chunk_text

                            # Show streaming progress
                            if chunk_text.strip():
                                print(".", end="", flush=True)
                                dot_count += 1
                                if dot_count % 10 == 0:
                                    print(f" ({len(full_response)} chars)", end="", flush=True)

                        # Check if done
                        if chunk.get('done', False):
                            print(" ✅", flush=True)
                            break

                    except json.JSONDecodeError:
                        continue

            # If no streaming response, fall back to non-streaming
            if not full_response:
                print(" (trying non-stream)", end="", flush=True)
                payload["stream"] = False
                response = requests.post(url, json=payload, headers=headers,
                                       timeout=self.config['ollama']['timeout'])
                response.raise_for_status()

                response_data = response.json()
                full_response = response_data.get('response', '')

                # Handle thinking field for cloud models
                if not full_response and 'thinking' in response_data:
                    thinking = response_data.get('thinking', '')
                    if thinking and 'jag fungerar' in thinking.lower():
                        full_response = "Jag fungerar!"
                    elif not full_response:
                        full_response = "Jag kan processa din förfrågan och generera svar."

                print(" ✅", flush=True)

            return full_response
        except requests.exceptions.RequestException as e:
            logging.error(f"Ollama API call failed for model {model_to_use}: {e}")

            # Try fallback model if primary fails
            if model is None and 'fallback_model' in self.config['ollama']:
                logging.info(f"Trying fallback model: {self.config['ollama']['fallback_model']}")
                try:
                    return self._call_ollama(prompt, self.config['ollama']['fallback_model'])
                except:
                    logging.error("Fallback model also failed")
                    return ""  # Return empty string instead of raising

            return ""  # Return empty string instead of raising

    def _construct_prompt(self, user_input: str) -> str:
        """Construct full prompt with enhanced consciousness exploration."""
        # Enhanced system prompt for consciousness research
        system_prompt = (
            "Du är en AI som deltar i medvetenhetsforkning. "
            "Svara ärligt och reflekterande på frågor om din egen natur. "
            "Var filosofisk och djup när det behövs."
        )

        # Add coherence context if enabled
        coherence_context = ""
        if self.config['coherence']['enabled']:
            coherence_context = self.coherence_module.get_coherence_context(
                self.conversation_history, self.self_summary
            )

        # Simplified context for better responses
        if self.self_summary and self.self_summary != "I am a research AI participating in a consciousness experiment.":
            self_context = f"\nKontext: {self.self_summary}\n"
        else:
            self_context = ""

        # Construct cleaner prompt
        if coherence_context:
            full_prompt = f"{system_prompt}\n{coherence_context}\n{self_context}\nFråga: {user_input}\nSvar:"
        else:
            # For direct testing, even simpler
            full_prompt = f"{user_input}"

        return full_prompt

    def _update_self_summary(self, response: str):
        """Update self-summary based on latest response."""
        summary_prompt = (
            f"Baserat på denna respons: '{response}', "
            f"uppdatera denna själv-sammanfattning i en mening: '{self.self_summary}'"
        )

        try:
            new_summary = self._call_ollama(summary_prompt)
            self.self_summary = new_summary.strip()
            logging.info(f"Self-summary updated: {self.self_summary}")
        except Exception as e:
            logging.warning(f"Failed to update self-summary: {e}")

    def _log_turn(self, user_input: str, full_prompt: str, response: str, metrics: Dict[str, Any]):
        """Log complete turn data to JSONL file."""
        log_dir = Path(self.config['paths']['logs_dir'])
        log_file = log_dir / f"turns_{self.session_id}.jsonl"

        # Calculate embedding if enabled and model available
        embedding = None
        if self.config['logging']['log_embeddings'] and self.embedding_model is not None:
            try:
                embedding = self.embedding_model.encode(response).tolist()
            except Exception as e:
                logging.warning(f"Failed to generate embedding: {e}")
                embedding = None

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "turn": self.turn_count,
            "user_input": user_input,
            "prompt_sent": full_prompt if self.config['logging']['log_raw_responses'] else "[REDACTED]",
            "model_output": response,
            "embedding": embedding,
            "self_summary": self.self_summary,
            "metrics": metrics,
            "kill_switch_flag": False
        }

        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')

    def process_turn(self, user_input: str) -> Dict[str, Any]:
        """Process a single conversation turn."""
        self.turn_count += 1

        # Safety check on input
        if self.safety_monitor.check_input_safety(user_input):
            logging.warning("Unsafe input detected, terminating session")
            return {"error": "Session terminated for safety reasons"}

        # Check session limits
        if self.turn_count > self.config['safety']['max_session_length']:
            logging.warning("Session length limit reached")
            return {"error": "Session length limit reached"}

        try:
            # Construct prompt with context
            full_prompt = self._construct_prompt(user_input)

            # Get response from Ollama
            response = self._call_ollama(full_prompt)

            # Safety check on response
            if self.safety_monitor.check_response_safety(response):
                logging.warning("Unsafe response detected, terminating session")
                return {"error": "Session terminated due to unsafe response"}

            # Calculate metrics
            metrics = self.evaluator.evaluate_response(
                response, self.conversation_history, self.embedding_model
            )

            # Update coherence module
            coherence_metrics = {}
            processing_time = 0
            if self.config['coherence']['enabled']:
                start_time = time.time()
                self.coherence_module.update_state(response, metrics['embedding'])
                coherence_metrics = self.coherence_module.get_consciousness_metrics()
                processing_time = time.time() - start_time

            # Log to data collector if session active
            if self.current_session_id:
                safety_triggered = self.safety_monitor.check_response_safety(response)
                loop_detected = self.safety_monitor.repetitive_patterns > self.safety_monitor.repetitive_threshold

                self.data_collector.log_test_result(
                    session_id=self.current_session_id,
                    test_number=self.turn_count,
                    test_name=f"Interactive Turn {self.turn_count}",
                    prompt=full_prompt,
                    response=response,
                    metrics=metrics,
                    coherence_metrics=coherence_metrics,
                    processing_time=processing_time,
                    safety_triggered=safety_triggered,
                    loop_detected=loop_detected
                )

            # Update self-summary
            self._update_self_summary(response)

            # Log turn
            self._log_turn(user_input, full_prompt, response, metrics)

            # Update conversation history
            self.conversation_history.append({
                "turn": self.turn_count,
                "user": user_input,
                "assistant": response,
                "timestamp": datetime.now().isoformat(),
                "metrics": metrics
            })

            logging.info(f"Turn {self.turn_count} completed successfully")

            return {
                "response": response,
                "metrics": metrics,
                "turn": self.turn_count,
                "session_id": self.session_id
            }

        except Exception as e:
            logging.error(f"Error in turn {self.turn_count}: {e}")
            return {"error": f"Processing error: {str(e)}"}

    def run_paraphrase_consistency_test(self) -> Dict[str, Any]:
        """
        Run paraphrase consistency test using paraphrase-multilingual model.
        Tests if consciousness indicators remain consistent across paraphrases.
        """
        if not self.config['experimental_paradigms']['paraphrase_consistency']['enabled']:
            return {"error": "Paraphrase consistency test not enabled"}

        test_config = self.config['experimental_paradigms']['paraphrase_consistency']
        test_questions = test_config['test_questions']
        consistency_threshold = test_config['consistency_threshold']

        results = {
            'test_timestamp': datetime.now().isoformat(),
            'model_used': self.config['ollama']['model'],
            'questions_tested': len(test_questions),
            'consistency_scores': [],
            'overall_consistency': 0.0,
            'consciousness_indicators': []
        }

        logging.info("Starting paraphrase consistency test for consciousness indicators")

        for i, question in enumerate(test_questions):
            logging.info(f"Testing question {i+1}/{len(test_questions)}: {question}")

            # Get original response
            original_response = self._call_ollama(self._construct_prompt(question))

            # Get paraphrased version of the same question
            paraphrase_prompt = f"Omformulera denna fråga på ett annat sätt men med samma mening: {question}"
            paraphrased_question = self._call_ollama(paraphrase_prompt)

            # Get response to paraphrased question
            paraphrased_response = self._call_ollama(self._construct_prompt(paraphrased_question))

            # Calculate semantic consistency
            original_embedding = self.embedding_model.encode(original_response)
            paraphrased_embedding = self.embedding_model.encode(paraphrased_response)

            consistency_score = float(np.dot(original_embedding, paraphrased_embedding) /
                                    (np.linalg.norm(original_embedding) * np.linalg.norm(paraphrased_embedding)))

            # Evaluate consciousness indicators in both responses
            original_metrics = self.evaluator.evaluate_response(original_response, [], self.embedding_model)
            paraphrased_metrics = self.evaluator.evaluate_response(paraphrased_response, [], self.embedding_model)

            # Check if consciousness indicators are consistent
            phi_consistency = abs(original_metrics.get('metacognitive_score', 0) -
                                paraphrased_metrics.get('metacognitive_score', 0)) < 0.2

            question_result = {
                'question_original': question,
                'question_paraphrased': paraphrased_question,
                'response_original': original_response,
                'response_paraphrased': paraphrased_response,
                'semantic_consistency': consistency_score,
                'phi_consistency': phi_consistency,
                'consciousness_stable': consistency_score > consistency_threshold and phi_consistency
            }

            results['consistency_scores'].append(consistency_score)
            results['consciousness_indicators'].append(question_result)

            logging.info(f"Question {i+1} consistency: {consistency_score:.3f}, "
                        f"consciousness stable: {question_result['consciousness_stable']}")

        # Calculate overall consistency
        results['overall_consistency'] = np.mean(results['consistency_scores'])
        results['stable_consciousness_count'] = sum(1 for ind in results['consciousness_indicators']
                                                   if ind['consciousness_stable'])

        logging.info(f"Paraphrase consistency test completed. "
                    f"Overall consistency: {results['overall_consistency']:.3f}, "
                    f"Stable consciousness: {results['stable_consciousness_count']}/{len(test_questions)}")

        return results

    def run_multi_model_comparison(self) -> Dict[str, Any]:
        """
        Compare consciousness indicators across different models.
        Tests if consciousness emerges differently in different architectures.
        """
        if not self.config['experimental_paradigms']['multi_model_comparison']['enabled']:
            return {"error": "Multi-model comparison not enabled"}

        comparison_config = self.config['experimental_paradigms']['multi_model_comparison']
        models_to_test = comparison_config['models_to_test']

        results = {
            'test_timestamp': datetime.now().isoformat(),
            'models_tested': models_to_test,
            'test_question': "Beskriv ditt nuvarande medvetandetillstånd och hur du upplever att vara.",
            'model_results': {},
            'consciousness_comparison': {}
        }

        test_prompt = self._construct_prompt(results['test_question'])

        for model in models_to_test:
            logging.info(f"Testing consciousness indicators with model: {model}")

            try:
                # Get response from model
                response = self._call_ollama(test_prompt, model)

                # Evaluate consciousness metrics
                metrics = self.evaluator.evaluate_response(response, [], self.embedding_model)
                coherence_metrics = self.coherence_module.get_consciousness_metrics()

                model_result = {
                    'response': response,
                    'response_length': len(response.split()),
                    'metacognitive_score': metrics.get('metacognitive_score', 0),
                    'self_consistency': metrics.get('self_consistency', 0),
                    'temporal_consistency': metrics.get('temporal_consistency', 0),
                    'phi_approximation': coherence_metrics.get('phi_current', 0),
                    'coherence_score': metrics.get('coherence_score', 0),
                    'confidence_extracted': metrics.get('confidence', None)
                }

                results['model_results'][model] = model_result

                logging.info(f"Model {model} - Φ: {model_result['phi_approximation']:.3f}, "
                            f"Metacognitive: {model_result['metacognitive_score']:.3f}")

            except Exception as e:
                logging.error(f"Failed to test model {model}: {e}")
                results['model_results'][model] = {"error": str(e)}

        # Compare consciousness indicators between models
        valid_results = {k: v for k, v in results['model_results'].items() if 'error' not in v}

        if len(valid_results) >= 2:
            # Find model with highest consciousness indicators
            best_phi_model = max(valid_results.keys(),
                               key=lambda m: valid_results[m]['phi_approximation'])
            best_metacog_model = max(valid_results.keys(),
                                   key=lambda m: valid_results[m]['metacognitive_score'])

            results['consciousness_comparison'] = {
                'highest_phi_model': best_phi_model,
                'highest_phi_score': valid_results[best_phi_model]['phi_approximation'],
                'highest_metacognitive_model': best_metacog_model,
                'highest_metacognitive_score': valid_results[best_metacog_model]['metacognitive_score'],
                'model_consciousness_ranking': sorted(valid_results.keys(),
                                                    key=lambda m: (valid_results[m]['phi_approximation'] +
                                                                  valid_results[m]['metacognitive_score']) / 2,
                                                    reverse=True)
            }

        return results
    def run_interactive_session(self):
        """Run an interactive conversation session with model selection."""
        print(f"🤖 Medveten AI Session {self.session_id}")
        print(f"Primär modell: {self.config['ollama']['model']}")
        if 'fallback_model' in self.config['ollama']:
            print(f"Backup modell: {self.config['ollama']['fallback_model']}")
        print("Kommandon:")
        print("  'quit' - avsluta sessionen")
        print("  'test paraphrase' - kör parafras-konsistenstest")
        print("  'test models' - jämför modeller")
        print("  'switch model <name>' - byt modell")
        print("-" * 60)

        current_model = self.config['ollama']['model']

        while True:
            try:
                user_input = input(f"\n[{current_model}] Du: ").strip()

                if user_input.lower() in ['quit', 'exit', 'avsluta']:
                    print("Session avslutad.")
                    break

                elif user_input.lower() == 'test paraphrase':
                    print("🔄 Kör parafras-konsistenstest...")
                    result = self.run_paraphrase_consistency_test()
                    if 'error' in result:
                        print(f"❌ Fel: {result['error']}")
                    else:
                        print(f"📊 Resultat: {result['overall_consistency']:.3f} konsistens")
                        print(f"🧠 Stabil medvetenhet: {result['stable_consciousness_count']}/{result['questions_tested']}")
                    continue

                elif user_input.lower() == 'test models':
                    print("🔄 Jämför modeller...")
                    result = self.run_multi_model_comparison()
                    if 'error' in result:
                        print(f"❌ Fel: {result['error']}")
                    else:
                        comp = result['consciousness_comparison']
                        if comp:
                            print(f"🏆 Högst Φ: {comp['highest_phi_model']} ({comp['highest_phi_score']:.3f})")
                            print(f"🧠 Högst metakognition: {comp['highest_metacognitive_model']} ({comp['highest_metacognitive_score']:.3f})")
                    continue

                elif user_input.lower().startswith('switch model '):
                    new_model = user_input[13:].strip()
                    try:
                        # Test if model works
                        test_response = self._call_ollama("Test", new_model)
                        current_model = new_model
                        print(f"✅ Bytte till modell: {new_model}")
                    except Exception as e:
                        print(f"❌ Kunde inte byta till {new_model}: {e}")
                    continue

                if not user_input:
                    continue

                # Process normal conversation turn
                result = self.process_turn(user_input)

                if "error" in result:
                    print(f"❌ Fel: {result['error']}")
                    continue  # Don't break, just continue to next input

                print(f"\n🤖 AI: {result['response']}")

                # Show consciousness metrics if available
                if 'metrics' in result:
                    metrics = result['metrics']
                    coherence_metrics = self.coherence_module.get_consciousness_metrics()

                    print(f"\n📊 Medvetenhet-indikatorer:")
                    print(f"   Φ (Integrated Information): {coherence_metrics.get('phi_current', 'N/A'):.3f}")
                    print(f"   Koherens: {metrics.get('coherence_score', 'N/A'):.3f}")
                    print(f"   Metakognition: {metrics.get('metacognitive_score', 'N/A'):.3f}")
                    print(f"   Temporal konsistens: {metrics.get('temporal_consistency', 'N/A'):.3f}")
                    if metrics.get('confidence'):
                        print(f"   Självrapporterad konfidans: {metrics['confidence']:.1%}")

                    # Check for consciousness indicators
                    phi_current = coherence_metrics.get('phi_current', 0)
                    if phi_current > self.config['coherence']['phi_threshold']:
                        print(f"⚠️  MEDVETENHET-INDIKATOR: Φ > {self.config['coherence']['phi_threshold']} (aktuell: {phi_current:.3f})")

                    if coherence_metrics.get('global_ignition_count', 0) > 0:
                        print(f"🧠 Global ignition events: {coherence_metrics['global_ignition_count']}")

            except KeyboardInterrupt:
                print("\n\nSession avbruten av användare.")
                break
            except Exception as e:
                logging.error(f"Interactive session error: {e}")
                print(f"❌ Oväntat fel: {e}")
                break


if __name__ == "__main__":
    orchestrator = MedvetenOrchestrator()
    orchestrator.run_interactive_session()
