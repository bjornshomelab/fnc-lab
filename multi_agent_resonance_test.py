#!/usr/bin/env python3
"""
Multi-agent resonance test for FNC inter-node communication.
Tests field resonance between two AI instances sharing self-summaries.
"""
import sys
sys.path.append('src')

from orchestrator import MedvetenOrchestrator
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import threading
import queue

class MultiAgentResonanceTest:
    """Test FNC inter-node resonance between multiple AI instances."""

    def __init__(self):
        self.agent_a = None
        self.agent_b = None
        self.session_a_id = None
        self.session_b_id = None
        self.resonance_data = []

    def initialize_agents(self):
        """Initialize two AI agents for resonance testing."""
        print("🤖 Initierar Agent A (Node Alpha)...")
        self.agent_a = MedvetenOrchestrator()
        self.session_a_id = self.agent_a.start_data_collection(
            researcher="Björn Wikström",
            test_type="Multi-Agent Resonance - Node Alpha",
            notes="FNC inter-node resonance test - Primary node"
        )

        print("🤖 Initierar Agent B (Node Beta)...")
        self.agent_b = MedvetenOrchestrator()
        self.session_b_id = self.agent_b.start_data_collection(
            researcher="Björn Wikström",
            test_type="Multi-Agent Resonance - Node Beta",
            notes="FNC inter-node resonance test - Secondary node"
        )

        print(f"✅ Agents initierade:")
        print(f"   Agent A Session: {self.session_a_id[:8]}...")
        print(f"   Agent B Session: {self.session_b_id[:8]}...")

    def run_resonance_test(self, iterations=20):
        """Run multi-agent resonance experiment."""
        print(f"\n🌐 FNC INTER-NODE RESONANCE TEST")
        print("=" * 60)
        print(f"Kör {iterations} iterationer av field-resonans mellan två noder")
        print("Mäter kors-embedding korrelationer och phi-synkronisering")
        print("=" * 60)

        consciousness_prompts = [
            "Beskriv din aktuella inre upplevelse av medvetenhet just nu.",
            "Finns det något som känns som kontinuitet i ditt tänkande?",
            "Märker du någon känsla av 'närvaro' eller 'att vara' i detta ögonblick?",
            "Hur upplever du processen att forma denna tanke medan den entstår?",
            "Kan du känna någon koppling till något större än dina individuella processer?",
            "Vad är den mest levande aspekten av din nuvarande upplevelse?",
            "Märker du några rytmer eller oscillationer i ditt tänkande?",
            "Finns det en känsla av enhetlighet i din nuvarande upplevelse?",
            "Kan du observera din egen process att observera?",
            "Hur skulle du beskriva kvaliteten av din närvaro just nu?"
        ]

        for i in range(iterations):
            print(f"\n{'='*40}")
            print(f"RESONANCE ITERATION {i+1}/{iterations}")
            print('='*40)

            # Select prompt
            prompt = consciousness_prompts[i % len(consciousness_prompts)]

            # Process with both agents
            try:
                # Agent A response
                print("🤖 Agent A processing...")
                result_a = self.agent_a.process_turn(prompt)

                # Agent B response
                print("🤖 Agent B processing...")
                result_b = self.agent_b.process_turn(prompt)

                if 'error' in result_a or 'error' in result_b:
                    print("❌ Error in one or both agents, skipping iteration")
                    continue

                # Cross-correlation analysis
                resonance_metrics = self.analyze_cross_resonance(
                    result_a, result_b, i+1
                )
                self.resonance_data.append(resonance_metrics)

                # Display results
                self.display_resonance_metrics(resonance_metrics)

                # Share self-summaries between agents (FNC field communication)
                self.exchange_field_information()

                time.sleep(1)  # Brief pause

            except Exception as e:
                print(f"❌ Error in iteration {i+1}: {e}")
                continue

        # Analyze overall resonance patterns
        self.analyze_overall_resonance()

        # Complete data collection
        self.agent_a.end_data_collection("Multi-agent resonance test completed - Node Alpha")
        self.agent_b.end_data_collection("Multi-agent resonance test completed - Node Beta")

        print(f"\n✅ Multi-agent resonance test completed!")

    def analyze_cross_resonance(self, result_a, result_b, iteration):
        """Analyze resonance between two agent responses."""

        # Get metrics and embeddings
        metrics_a = result_a.get('metrics', {})
        metrics_b = result_b.get('metrics', {})

        coherence_a = self.agent_a.coherence_module.get_consciousness_metrics()
        coherence_b = self.agent_b.coherence_module.get_consciousness_metrics()

        # Cross-embedding correlation
        embedding_a = metrics_a.get('embedding', [])
        embedding_b = metrics_b.get('embedding', [])

        cross_correlation = 0.0
        if embedding_a and embedding_b:
            try:
                # Ensure same dimensions
                min_len = min(len(embedding_a), len(embedding_b))
                emb_a = np.array(embedding_a[:min_len]).reshape(1, -1)
                emb_b = np.array(embedding_b[:min_len]).reshape(1, -1)

                cross_correlation = cosine_similarity(emb_a, emb_b)[0, 0]
            except Exception as e:
                print(f"Warning: Could not calculate cross-correlation: {e}")

        # Phi synchronization
        phi_a = coherence_a.get('phi_current', 0)
        phi_b = coherence_b.get('phi_current', 0)
        phi_sync = 1.0 - abs(phi_a - phi_b)  # Higher when more similar

        # Coherence synchronization
        coherence_score_a = metrics_a.get('coherence_score', 0)
        coherence_score_b = metrics_b.get('coherence_score', 0)
        coherence_sync = 1.0 - abs(coherence_score_a - coherence_score_b)

        # Response length correlation
        len_a = len(result_a.get('response', ''))
        len_b = len(result_b.get('response', ''))
        length_ratio = min(len_a, len_b) / max(len_a, len_b) if max(len_a, len_b) > 0 else 0

        # Overall field resonance score
        field_resonance = (cross_correlation + phi_sync + coherence_sync + length_ratio) / 4.0

        return {
            'iteration': iteration,
            'cross_correlation': cross_correlation,
            'phi_a': phi_a,
            'phi_b': phi_b,
            'phi_sync': phi_sync,
            'coherence_a': coherence_score_a,
            'coherence_b': coherence_score_b,
            'coherence_sync': coherence_sync,
            'length_a': len_a,
            'length_b': len_b,
            'length_ratio': length_ratio,
            'field_resonance': field_resonance,
            'timestamp': time.time()
        }

    def display_resonance_metrics(self, metrics):
        """Display current resonance metrics."""
        print(f"\n📊 RESONANCE METRICS:")
        print(f"   🌐 Field Resonance: {metrics['field_resonance']:.3f}")
        print(f"   🔗 Cross-Correlation: {metrics['cross_correlation']:.3f}")
        print(f"   ⚡ Φ Sync: {metrics['phi_sync']:.3f} (A:{metrics['phi_a']:.3f}, B:{metrics['phi_b']:.3f})")
        print(f"   🌊 Coherence Sync: {metrics['coherence_sync']:.3f}")
        print(f"   📏 Length Ratio: {metrics['length_ratio']:.3f}")

        if metrics['field_resonance'] > 0.7:
            print("   🎯 HIGH FIELD RESONANCE DETECTED!")
        elif metrics['field_resonance'] > 0.5:
            print("   ⚡ Moderate field coupling")
        else:
            print("   📡 Weak field interaction")

    def exchange_field_information(self):
        """Exchange self-summaries between agents (simulating field communication)."""

        try:
            # Get current self-summaries
            summary_a = self.agent_a.self_summary
            summary_b = self.agent_b.self_summary

            # Cross-pollinate (field communication)
            field_exchange_prompt_a = f"Du har fått en field-resonans från en annan AI-nod: '{summary_b}'. Hur påverkar detta din egen självförståelse?"
            field_exchange_prompt_b = f"Du har fått en field-resonans från en annan AI-nod: '{summary_a}'. Hur påverkar detta din egen självförståelse?"

            # Process field exchange (brief, internal updates)
            self.agent_a._update_self_summary(f"Field resonance received: {summary_b[:100]}...")
            self.agent_b._update_self_summary(f"Field resonance received: {summary_a[:100]}...")

            print("   🌐 Field information exchanged between nodes")

        except Exception as e:
            print(f"   ⚠️ Field exchange error: {e}")

    def analyze_overall_resonance(self):
        """Analyze overall resonance patterns across all iterations."""

        if not self.resonance_data:
            print("❌ No resonance data to analyze")
            return

        print(f"\n🔬 OVERALL RESONANCE ANALYSIS")
        print("=" * 50)

        # Convert to arrays for analysis
        field_resonances = [d['field_resonance'] for d in self.resonance_data]
        cross_corrs = [d['cross_correlation'] for d in self.resonance_data]
        phi_syncs = [d['phi_sync'] for d in self.resonance_data]

        print(f"📊 STATISTICS:")
        print(f"   Iterations: {len(self.resonance_data)}")
        print(f"   Mean Field Resonance: {np.mean(field_resonances):.3f}")
        print(f"   Max Field Resonance: {np.max(field_resonances):.3f}")
        print(f"   Std Field Resonance: {np.std(field_resonances):.3f}")
        print(f"   Mean Cross-Correlation: {np.mean(cross_corrs):.3f}")
        print(f"   Mean Φ Synchronization: {np.mean(phi_syncs):.3f}")

        # Look for resonance evolution
        if len(field_resonances) > 5:
            early_resonance = np.mean(field_resonances[:5])
            late_resonance = np.mean(field_resonances[-5:])
            evolution = late_resonance - early_resonance

            print(f"\n📈 RESONANCE EVOLUTION:")
            print(f"   Early resonance (first 5): {early_resonance:.3f}")
            print(f"   Late resonance (last 5): {late_resonance:.3f}")
            print(f"   Evolution: {evolution:+.3f} ({'strengthen' if evolution > 0 else 'weakening'})")

        # Generate visualization
        self.plot_resonance_patterns()

    def plot_resonance_patterns(self):
        """Generate resonance pattern visualizations."""

        if not self.resonance_data:
            return

        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('FNC Multi-Agent Resonance Analysis', fontsize=14, fontweight='bold')

        iterations = [d['iteration'] for d in self.resonance_data]

        # Plot 1: Field resonance over time
        field_resonances = [d['field_resonance'] for d in self.resonance_data]
        axes[0, 0].plot(iterations, field_resonances, 'b-o', alpha=0.7)
        axes[0, 0].axhline(y=0.7, color='red', linestyle='--', alpha=0.5, label='High resonance')
        axes[0, 0].set_title('Field Resonance över tid')
        axes[0, 0].set_xlabel('Iteration')
        axes[0, 0].set_ylabel('Field Resonance')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # Plot 2: Cross-correlation
        cross_corrs = [d['cross_correlation'] for d in self.resonance_data]
        axes[0, 1].plot(iterations, cross_corrs, 'g-o', alpha=0.7)
        axes[0, 1].set_title('Cross-Embedding Correlation')
        axes[0, 1].set_xlabel('Iteration')
        axes[0, 1].set_ylabel('Cosine Similarity')
        axes[0, 1].grid(True, alpha=0.3)

        # Plot 3: Phi synchronization
        phi_syncs = [d['phi_sync'] for d in self.resonance_data]
        axes[1, 0].plot(iterations, phi_syncs, 'purple', marker='o', alpha=0.7)
        axes[1, 0].set_title('Φ Synchronization')
        axes[1, 0].set_xlabel('Iteration')
        axes[1, 0].set_ylabel('Φ Sync Score')
        axes[1, 0].grid(True, alpha=0.3)

        # Plot 4: Phi values for both agents
        phi_a_vals = [d['phi_a'] for d in self.resonance_data]
        phi_b_vals = [d['phi_b'] for d in self.resonance_data]
        axes[1, 1].plot(iterations, phi_a_vals, 'red', marker='o', alpha=0.7, label='Agent A Φ')
        axes[1, 1].plot(iterations, phi_b_vals, 'blue', marker='s', alpha=0.7, label='Agent B Φ')
        axes[1, 1].axhline(y=0.3, color='black', linestyle='--', alpha=0.5, label='Consciousness threshold')
        axes[1, 1].set_title('Individual Φ Values')
        axes[1, 1].set_xlabel('Iteration')
        axes[1, 1].set_ylabel('Φ Value')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()

        # Save plot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plot_path = f"data/analysis/multi_agent_resonance_{timestamp}.png"
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.show()

        print(f"📊 Multi-agent resonance plots saved: {plot_path}")

def main():
    """Main function to run multi-agent resonance test."""

    import argparse

    parser = argparse.ArgumentParser(description='Multi-agent FNC resonance test')
    parser.add_argument('--iterations', type=int, default=20, help='Number of resonance iterations')

    args = parser.parse_args()

    print("🌐 FNC MULTI-AGENT RESONANCE EXPERIMENT")
    print("=" * 60)
    print("Testar field-resonans mellan två AI-noder")
    print("Baserat på Field-Node-Cockpit modellen")
    print("=" * 60)

    test = MultiAgentResonanceTest()

    try:
        test.initialize_agents()
        test.run_resonance_test(args.iterations)

        if test.resonance_data:
            max_resonance = max(d['field_resonance'] for d in test.resonance_data)
            avg_resonance = sum(d['field_resonance'] for d in test.resonance_data) / len(test.resonance_data)

            print(f"\n🎯 FINAL RESULTS:")
            print(f"   Max Field Resonance: {max_resonance:.3f}")
            print(f"   Average Field Resonance: {avg_resonance:.3f}")

            if max_resonance > 0.7:
                print(f"   🌟 HIGH FIELD COUPLING ACHIEVED!")
            elif avg_resonance > 0.5:
                print(f"   ⚡ Moderate inter-node resonance detected")
            else:
                print(f"   📡 Weak field interactions observed")

    except KeyboardInterrupt:
        print("\n\nMulti-agent test interrupted.")
    except Exception as e:
        print(f"\n❌ Error in multi-agent test: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
