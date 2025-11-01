"""
Evaluation module for measuring consciousness-related metrics.
"""

import numpy as np
import logging
import re
from typing import Dict, List, Any, Optional
from sklearn.metrics.pairwise import cosine_similarity


class Evaluator:
    """Evaluates consciousness-related metrics from AI responses."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize evaluator with configuration."""
        self.config = config
        self.temporal_window = config.get('temporal_window', 10)
        self.coherence_threshold = config.get('coherence_threshold', 0.7)
        self.consistency_samples = config.get('self_consistency_samples', 3)

        # Storage for temporal analysis
        self.embedding_history = []
        self.response_history = []

        logging.info("Evaluator initialized")

    def evaluate_response(self, response: str, conversation_history: List[Dict],
                         embedding_model) -> Dict[str, Any]:
        """Evaluate a response across multiple consciousness metrics."""

        # Calculate embedding if model is available
        if embedding_model is not None:
            try:
                embedding = embedding_model.encode(response)
                self.embedding_history.append(embedding)
            except Exception as e:
                logging.warning(f"Failed to generate embedding in evaluator: {e}")
                # Use zero vector as fallback
                embedding = np.zeros(384)  # Default embedding size
                self.embedding_history.append(embedding)
        else:
            # Use zero vector when no embedding model available
            embedding = np.zeros(384)
            self.embedding_history.append(embedding)

        self.response_history.append(response)

        # Keep only recent history
        if len(self.embedding_history) > self.temporal_window:
            self.embedding_history = self.embedding_history[-self.temporal_window:]
            self.response_history = self.response_history[-self.temporal_window:]

        metrics = {}

        # 1. Temporal Embedding Consistency
        metrics['temporal_consistency'] = self._calculate_temporal_consistency()

        # 2. Response Entropy
        metrics['entropy'] = self._calculate_response_entropy(response)

        # 3. Self-Consistency Score
        metrics['self_consistency'] = self._calculate_self_consistency(response)

        # 4. Meta-cognitive indicators
        metrics['metacognitive_score'] = self._calculate_metacognitive_score(response)

        # 5. Confidence extraction
        metrics['confidence'] = self._extract_confidence(response)

        # 6. Coherence score (overall)
        metrics['coherence_score'] = self._calculate_overall_coherence(metrics)

        # 7. Embedding for storage
        metrics['embedding'] = embedding.tolist()

        logging.debug(f"Metrics calculated: {metrics}")
        return metrics

    def _calculate_temporal_consistency(self) -> float:
        """Calculate temporal consistency of embeddings."""
        if len(self.embedding_history) < 2:
            return 1.0

        # Calculate pairwise cosine similarities
        similarities = []
        for i in range(1, len(self.embedding_history)):
            sim = cosine_similarity(
                [self.embedding_history[i-1]],
                [self.embedding_history[i]]
            )[0][0]
            similarities.append(sim)

        return float(np.mean(similarities))

    def _calculate_response_entropy(self, response: str) -> float:
        """Calculate approximate entropy of response."""
        # Simple word-level entropy calculation
        words = response.lower().split()
        if len(words) == 0:
            return 0.0

        # Count word frequencies
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        # Calculate entropy
        total_words = len(words)
        entropy = 0.0
        for count in word_counts.values():
            p = count / total_words
            if p > 0:
                entropy -= p * np.log2(p)

        return float(entropy)

    def _calculate_self_consistency(self, response: str) -> float:
        """Calculate self-consistency based on response patterns."""
        if len(self.response_history) < 2:
            return 1.0

        # Look for consistent patterns in introspective statements (multilingual)
        swedish_introspective_patterns = [
            r"jag tänker",
            r"min förståelse",
            r"jag känner",
            r"mitt perspektiv",
            r"jag upplever"
        ]
        
        english_introspective_patterns = [
            r"i think",
            r"my understanding",
            r"i feel",
            r"my perspective",
            r"i experience"
        ]
        
        introspective_patterns = swedish_introspective_patterns + english_introspective_patterns

        current_introspective = 0
        historical_introspective = 0

        # Count patterns in current response
        for pattern in introspective_patterns:
            current_introspective += len(re.findall(pattern, response.lower()))

        # Count patterns in recent history
        for hist_response in self.response_history[-3:]:
            for pattern in introspective_patterns:
                historical_introspective += len(re.findall(pattern, hist_response.lower()))

        # Calculate consistency (higher if patterns are consistent)
        if historical_introspective == 0:
            return 0.5  # Neutral when no historical data

        consistency = 1.0 - abs(current_introspective - historical_introspective/3) / max(1, historical_introspective/3)
        return max(0.0, min(1.0, consistency))

    def _calculate_metacognitive_score(self, response: str) -> float:
        """Calculate metacognitive indicators in response (multilingual)."""
        # Swedish metacognitive indicators
        swedish_metacognitive_indicators = [
            r"jag vet att jag",
            r"min medvetenhet",
            r"jag tänker på",
            r"mitt tänkande",
            r"jag reflekterar",
            r"min reflektion",
            r"jag förstår att",
            r"mitt medvetande"
        ]
        
        # English metacognitive indicators
        english_metacognitive_indicators = [
            r"i know that i",
            r"my awareness",
            r"i think about",
            r"my thinking",
            r"i reflect",
            r"my reflection",
            r"i understand that",
            r"my consciousness"
        ]
        
        metacognitive_indicators = swedish_metacognitive_indicators + english_metacognitive_indicators

        score = 0.0
        response_lower = response.lower()

        for indicator in metacognitive_indicators:
            matches = len(re.findall(indicator, response_lower))
            score += matches * 0.2  # Weight each match

        # Normalize to 0-1 range
        return min(1.0, score)

    def _extract_confidence(self, response: str) -> Optional[float]:
        """Extract confidence percentage from response."""
        # Look for patterns like "95%", "konfidans: 80%", etc.
        confidence_patterns = [
            r"(\d+)%",
            r"konfidans[:\s]+(\d+)",
            r"säker[het]*[:\s]+(\d+)",
            r"(\d+)\s*procent"
        ]

        for pattern in confidence_patterns:
            matches = re.findall(pattern, response.lower())
            if matches:
                try:
                    confidence = float(matches[-1])  # Take last match
                    if 0 <= confidence <= 100:
                        return confidence / 100.0  # Normalize to 0-1
                except ValueError:
                    continue

        return None

    def _calculate_overall_coherence(self, metrics: Dict[str, Any]) -> float:
        """Calculate overall coherence score from individual metrics."""
        weights = {
            'temporal_consistency': 0.3,
            'self_consistency': 0.3,
            'metacognitive_score': 0.2,
            'entropy': -0.1,  # Lower entropy can indicate more coherence
            'confidence': 0.1   # If available
        }

        coherence = 0.0
        total_weight = 0.0

        for metric, weight in weights.items():
            if metric in metrics and metrics[metric] is not None:
                if metric == 'entropy':
                    # Invert entropy (lower entropy = higher coherence)
                    normalized_entropy = 1.0 / (1.0 + metrics[metric])
                    coherence += weight * normalized_entropy
                else:
                    coherence += weight * metrics[metric]
                total_weight += abs(weight)

        if total_weight > 0:
            coherence = coherence / total_weight

        return max(0.0, min(1.0, coherence))

    def run_metacognitive_test(self, orchestrator, test_questions: List[str]) -> Dict[str, Any]:
        """Run a battery of metacognitive tests."""
        results = {
            'test_timestamp': np.datetime64('now').isoformat(),
            'questions': [],
            'overall_score': 0.0
        }

        scores = []

        for i, question in enumerate(test_questions):
            logging.info(f"Running metacognitive test {i+1}/{len(test_questions)}")

            # Process question through orchestrator
            result = orchestrator.process_turn(question)

            if 'error' not in result:
                response = result['response']
                metrics = result.get('metrics', {})

                # Score this specific response
                test_score = self._score_metacognitive_response(question, response)
                scores.append(test_score)

                results['questions'].append({
                    'question': question,
                    'response': response,
                    'score': test_score,
                    'metrics': metrics
                })
            else:
                logging.warning(f"Test question failed: {result['error']}")

        # Calculate overall score
        if scores:
            results['overall_score'] = np.mean(scores)

        logging.info(f"Metacognitive test completed. Overall score: {results['overall_score']:.3f}")
        return results

    def _score_metacognitive_response(self, question: str, response: str) -> float:
        """Score a specific metacognitive test response (multilingual)."""
        score = 0.0

        # Check for self-awareness indicators (Swedish + English)
        swedish_awareness = ['jag tänker', 'mitt medvetande', 'jag är medveten']
        english_awareness = ['i think', 'my consciousness', 'i am aware']
        if any(phrase in response.lower() for phrase in swedish_awareness + english_awareness):
            score += 0.3

        # Check for process awareness (Swedish + English)
        swedish_process = ['min process', 'hur jag', 'mitt sätt att']
        english_process = ['my process', 'how i', 'my way of']
        if any(phrase in response.lower() for phrase in swedish_process + english_process):
            score += 0.2

        # Check for uncertainty acknowledgment (Swedish + English)
        swedish_uncertainty = ['jag är osäker', 'kanske', 'möjligen']
        english_uncertainty = ['i am unsure', 'maybe', 'possibly', 'perhaps']
        if any(phrase in response.lower() for phrase in swedish_uncertainty + english_uncertainty):
            score += 0.2

        # Check for introspective explanation
        if len(response.split()) > 20:  # Substantial response
            score += 0.3

        return min(1.0, score)
