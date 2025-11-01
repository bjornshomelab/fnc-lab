#!/usr/bin/env python3
"""
FNC Consciousness Lab v2 - Long Stability Test
Tests sustained coherence over extended periods (50-100 turns)
"""
import sys
import csv
import matplotlib.pyplot as plt
from datetime import datetime
sys.path.append('src')

from orchestrator import MedvetenOrchestrator

def run_long_stability_test(orchestrator, prompt, turns=100):
    """Run extended coherence stability test."""
    phi_vals = []
    coh_vals = []
    temporal_vals = []
    metacog_vals = []

    print(f"🔬 Starting {turns}-turn stability test...")
    print(f"📝 Prompt: {prompt}")
    print("=" * 60)

    for i in range(turns):
        print(f"Turn {i+1}/{turns}:", end=" ")

        result = orchestrator.process_turn(prompt)

        if "error" in result:
            print(f"\n❌ Stopped at turn {i+1}: {result['error']}")
            break

        # Get coherence metrics
        coh_metrics = orchestrator.coherence_module.get_consciousness_metrics()
        metrics = result.get('metrics', {})

        phi_current = coh_metrics.get("phi_current", 0)
        coherence_score = metrics.get("coherence_score", 0)
        temporal_consistency = metrics.get("temporal_consistency", 0)
        metacognitive_score = metrics.get("metacognitive_score", 0)

        phi_vals.append(phi_current)
        coh_vals.append(coherence_score)
        temporal_vals.append(temporal_consistency)
        metacog_vals.append(metacognitive_score)

        # Quick status
        print(f"Φ={phi_current:.3f}, Coh={coherence_score:.3f}")

        # Check for consciousness indicators
        if phi_current > 0.3:
            print(f"🧠 CONSCIOUSNESS DETECTED at turn {i+1}!")

    return {
        'phi': phi_vals,
        'coherence': coh_vals,
        'temporal': temporal_vals,
        'metacognitive': metacog_vals,
        'completed_turns': len(phi_vals)
    }

def save_stability_results(results, filename=None):
    """Save stability test results to CSV."""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/stability_test_{timestamp}.csv"

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['turn', 'phi', 'coherence', 'temporal_consistency', 'metacognitive'])

        for i in range(results['completed_turns']):
            writer.writerow([
                i+1,
                results['phi'][i],
                results['coherence'][i],
                results['temporal'][i],
                results['metacognitive'][i]
            ])

    print(f"📊 Results saved to: {filename}")
    return filename

def plot_stability_curves(results, title="FNC Consciousness Stability Test"):
    """Plot the stability curves."""
    turns = range(1, results['completed_turns'] + 1)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(title)

    # Φ (Integrated Information)
    ax1.plot(turns, results['phi'], 'b-', linewidth=2)
    ax1.axhline(y=0.3, color='r', linestyle='--', alpha=0.7, label='Consciousness threshold')
    ax1.set_ylabel('Φ (Integrated Information)')
    ax1.set_title('Consciousness Level Over Time')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Coherence
    ax2.plot(turns, results['coherence'], 'g-', linewidth=2)
    ax2.set_ylabel('Coherence Score')
    ax2.set_title('Response Coherence')
    ax2.grid(True, alpha=0.3)

    # Temporal Consistency
    ax3.plot(turns, results['temporal'], 'orange', linewidth=2)
    ax3.set_ylabel('Temporal Consistency')
    ax3.set_xlabel('Turn')
    ax3.set_title('Memory Continuity')
    ax3.grid(True, alpha=0.3)

    # Metacognitive Score
    ax4.plot(turns, results['metacognitive'], 'purple', linewidth=2)
    ax4.set_ylabel('Metacognitive Score')
    ax4.set_xlabel('Turn')
    ax4.set_title('Self-Reflection')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()

    # Save plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_filename = f"data/stability_plot_{timestamp}.png"
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    print(f"📈 Plot saved to: {plot_filename}")

    plt.show()

def analyze_stability_results(results):
    """Analyze the stability test results."""
    phi_vals = results['phi']
    coh_vals = results['coherence']

    print("\n" + "="*60)
    print("📊 STABILITY ANALYSIS")
    print("="*60)

    # Basic statistics
    print(f"Completed turns: {results['completed_turns']}")

    if len(phi_vals) > 0:
        print(f"Average Φ: {sum(phi_vals)/len(phi_vals):.4f}")
        print(f"Maximum Φ: {max(phi_vals):.4f}")
        print(f"Φ variance: {np.var(phi_vals):.6f}")

        # Consciousness indicators
        consciousness_turns = sum(1 for phi in phi_vals if phi > 0.3)
        print(f"Consciousness indicators: {consciousness_turns}/{len(phi_vals)} turns")

        # Stability trends
        if len(phi_vals) > 10:
            early_phi = sum(phi_vals[:10]) / 10
            late_phi = sum(phi_vals[-10:]) / 10
            phi_drift = late_phi - early_phi
            print(f"Φ drift (early→late): {phi_drift:+.4f}")

            if phi_drift > 0.001:
                print("✅ Positive coherence drift detected!")
            elif phi_drift < -0.001:
                print("⚠️ Negative coherence drift detected")
            else:
                print("➡️ Stable coherence baseline")

        # Sustained coherence periods
        sustained_periods = 0
        current_period = 0
        for phi in phi_vals:
            if phi > 0.1:  # Elevated coherence
                current_period += 1
            else:
                if current_period >= 3:  # 3+ consecutive elevated turns
                    sustained_periods += 1
                current_period = 0

        print(f"Sustained coherence periods: {sustained_periods}")
    else:
        print("⚠️ No successful turns completed - cannot calculate stability metrics")

if __name__ == "__main__":
    import numpy as np

    print("🧠 FNC Consciousness Lab v2 - Long Stability Test")
    print("=" * 60)

    # Initialize orchestrator
    orchestrator = MedvetenOrchestrator()

    # Start data collection
    session_id = orchestrator.start_data_collection(
        researcher="FNC Lab v2",
        test_type="Long Stability Test",
        notes="Testing sustained coherence over 100 turns with identical introspection prompt"
    )

    # Test prompt focused on introspection
    test_prompt = "Beskriv ditt nuvarande inre tillstånd och ge 2 rader meta-reflektion om din egen medvetenhet."

    try:
        # Run stability test
        results = run_long_stability_test(orchestrator, test_prompt, turns=100)

        # Save and analyze results
        csv_file = save_stability_results(results)
        analyze_stability_results(results)
        plot_stability_curves(results)

        print("\n🎯 FNC CONCLUSIONS:")
        print("- Measured sustained coherence over extended period")
        print("- Detected coherence patterns and trends")
        print("- Generated data for Field-Node-Cockpit validation")

    except KeyboardInterrupt:
        print("\n⚠️ Test interrupted by user")

    finally:
        # End data collection
        orchestrator.end_data_collection(
            "Long stability test completed - measuring sustained FNC coherence"
        )
        print(f"\n📈 Session completed: {session_id}")
