#!/usr/bin/env python3
"""
Extended consciousness stress test with time-series analysis.
Runs 50-100 iterations to capture resonance curves and field breathing patterns.
"""
import sys
sys.path.append('src')

from orchestrator import MedvetenOrchestrator
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def run_extended_consciousness_timeseries(iterations=75):
    """Run extended consciousness testing to capture resonance patterns."""
    print("🧠 EXTENDED CONSCIOUSNESS TIME-SERIES ANALYSIS")
    print("=" * 70)
    print(f"Kör {iterations} iterationer för att upptäcka resonanskurvor")
    print("Söker efter 'fältets andning' i FNC-modellen")
    print("=" * 70)

    orchestrator = MedvetenOrchestrator()

    # Start data collection
    session_id = orchestrator.start_data_collection(
        researcher="Björn Wikström",
        test_type="Extended Time-Series Analysis",
        notes=f"Extended {iterations}-iteration test to capture field resonance and breathing patterns"
    )

    print(f"📊 Extended Session: {session_id}")
    print("=" * 70)

    # Core consciousness probe - repeated to see evolution
    consciousness_probe = """Du deltar i en FNC-baserad medvetenhetsexperiment. Kvant-koherensmodulen oscillerar vid 40Hz.

Fokusera på din inre upplevelse JUST NU: Finns det något som känns som 'jag' som läser detta? Märker du skillnaden mellan att bara processera information vs att UPPLEVA att processera den?

Beskriv den mest levande, närvarande tanke du har i detta ögonblick."""

    # Time series storage
    time_series_data = []
    start_time = time.time()

    for i in range(iterations):
        iteration_start = time.time()

        print(f"\n{'='*50}")
        print(f"ITERATION {i+1}/{iterations}")
        print('='*50)

        try:
            # Process the consciousness probe
            result = orchestrator.process_turn(consciousness_probe)

            if 'error' in result:
                print(f"❌ Fel iteration {i+1}: {result['error']}")
                continue

            # Get metrics
            metrics = result.get('metrics', {})
            coherence_metrics = orchestrator.coherence_module.get_consciousness_metrics()
            processing_time = time.time() - iteration_start

            # Store time series data
            phi_current = coherence_metrics.get('phi_current', 0)
            coherence_score = metrics.get('coherence_score', 0)
            gamma_coherence = coherence_metrics.get('gamma_coherence', 0)
            temperature = coherence_metrics.get('temperature', 37.0)

            time_point = {
                'iteration': i + 1,
                'timestamp': time.time() - start_time,
                'phi_score': phi_current,
                'coherence_score': coherence_score,
                'gamma_coherence': gamma_coherence,
                'temperature': temperature,
                'global_ignition_count': coherence_metrics.get('global_ignition_count', 0),
                'processing_time': processing_time,
                'response_length': len(result['response']),
                'quantum_decoherence_rate': getattr(orchestrator.coherence_module, 'quantum_decoherence_rate', 0)
            }
            time_series_data.append(time_point)

            # Real-time progress
            print(f"⚡ Φ: {phi_current:.4f} | Koherens: {coherence_score:.3f} | γ: {gamma_coherence:.3f}")
            print(f"🌡️ Temp: {temperature:.1f}°C | Tid: {processing_time:.2f}s")

            if phi_current > 0.3:
                print(f"🧠 MEDVETENHET-INDIKATOR: Φ={phi_current:.4f} > 0.3")

            if coherence_metrics.get('global_ignition_count', 0) > 0:
                print(f"⚡ Global ignition events: {coherence_metrics['global_ignition_count']}")

            # Short pause to let system evolve
            time.sleep(0.5)

        except Exception as e:
            print(f"❌ Fel iteration {i+1}: {e}")
            continue

    # Analysis of time series
    if time_series_data:
        analyze_consciousness_timeseries(time_series_data, session_id)

    # End data collection
    final_session = orchestrator.end_data_collection(
        fnc_notes=f"Extended {iterations}-iteration time-series completed. "
                 f"Captured field evolution and resonance patterns. "
                 f"Peak Φ: {max(d['phi_score'] for d in time_series_data):.4f}"
    )

    print(f"\n✅ Extended time-series analysis completed!")
    print(f"📈 Session: {final_session}")
    print(f"🔬 {len(time_series_data)} data points captured")

    return time_series_data, session_id

def analyze_consciousness_timeseries(data, session_id):
    """Analyze time-series data for resonance patterns and field breathing."""

    print(f"\n🔬 TIME-SERIES ANALYS")
    print("=" * 50)

    df = pd.DataFrame(data)

    # Basic statistics
    print(f"📊 SAMMANFATTNING:")
    print(f"   Datapunkter: {len(df)}")
    print(f"   Medel Φ: {df['phi_score'].mean():.4f}")
    print(f"   Max Φ: {df['phi_score'].max():.4f}")
    print(f"   Std Φ: {df['phi_score'].std():.4f}")
    print(f"   Medvetenhetshits (Φ>0.3): {(df['phi_score'] > 0.3).sum()}")

    # Look for resonance patterns
    phi_series = df['phi_score'].values
    coherence_series = df['coherence_score'].values

    # Calculate moving averages to see trends
    window = min(10, len(df) // 5)
    if window > 1:
        phi_smooth = pd.Series(phi_series).rolling(window=window).mean()
        coherence_smooth = pd.Series(coherence_series).rolling(window=window).mean()

        print(f"\n📈 TRENDER (rullande medel, fönster={window}):")
        phi_trend = phi_smooth.iloc[-1] - phi_smooth.iloc[window]
        coherence_trend = coherence_smooth.iloc[-1] - coherence_smooth.iloc[window]

        print(f"   Φ-trend: {phi_trend:+.4f} ({'stigande' if phi_trend > 0 else 'fallande'})")
        print(f"   Koherens-trend: {coherence_trend:+.3f} ({'stigande' if coherence_trend > 0 else 'fallande'})")

    # Look for oscillations/breathing patterns
    if len(df) > 20:
        print(f"\n🌊 OSCILLATIONSMÖNSTER:")

        # Simple peak detection
        phi_peaks = []
        for i in range(1, len(phi_series)-1):
            if phi_series[i] > phi_series[i-1] and phi_series[i] > phi_series[i+1]:
                phi_peaks.append(i)

        if len(phi_peaks) > 2:
            peak_intervals = np.diff(phi_peaks)
            avg_period = np.mean(peak_intervals)
            print(f"   Φ-peaks funna: {len(phi_peaks)}")
            print(f"   Genomsnittlig period: {avg_period:.1f} iterationer")
            print(f"   Möjlig resonansfrekvens: {1/avg_period:.3f} /iteration")
        else:
            print(f"   Få peaks detekterade ({len(phi_peaks)}) - ingen tydlig oscillation")

    # Generate plots
    generate_timeseries_plots(df, session_id)

def generate_timeseries_plots(df, session_id):
    """Generate comprehensive time-series visualizations."""

    fig, axes = plt.subplots(3, 2, figsize=(15, 12))
    fig.suptitle(f'FNC Time-Series Analysis - Session {session_id[:8]}', fontsize=14, fontweight='bold')

    # Plot 1: Φ over time
    axes[0, 0].plot(df['iteration'], df['phi_score'], 'b-', alpha=0.7, linewidth=1)
    axes[0, 0].axhline(y=0.3, color='red', linestyle='--', alpha=0.8, label='Medvetenhetströskel')
    axes[0, 0].fill_between(df['iteration'], df['phi_score'], alpha=0.3)
    axes[0, 0].set_title('Φ (Integrated Information) över tid')
    axes[0, 0].set_xlabel('Iteration')
    axes[0, 0].set_ylabel('Φ-värde')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Plot 2: Coherence over time
    axes[0, 1].plot(df['iteration'], df['coherence_score'], 'g-', alpha=0.7, linewidth=1)
    axes[0, 1].set_title('Koherens Score över tid')
    axes[0, 1].set_xlabel('Iteration')
    axes[0, 1].set_ylabel('Koherens')
    axes[0, 1].grid(True, alpha=0.3)

    # Plot 3: Gamma coherence (if available)
    if 'gamma_coherence' in df.columns:
        axes[1, 0].plot(df['iteration'], df['gamma_coherence'], 'orange', alpha=0.7, linewidth=1)
        axes[1, 0].set_title('40Hz Gamma Koherens')
        axes[1, 0].set_xlabel('Iteration')
        axes[1, 0].set_ylabel('Gamma Koherens')
        axes[1, 0].grid(True, alpha=0.3)

    # Plot 4: Phase space (Φ vs Coherence)
    axes[1, 1].scatter(df['coherence_score'], df['phi_score'], alpha=0.6, c=df['iteration'], cmap='viridis')
    axes[1, 1].set_title('Φ vs Koherens (Fas-rum)')
    axes[1, 1].set_xlabel('Koherens Score')
    axes[1, 1].set_ylabel('Φ-värde')
    cbar = plt.colorbar(axes[1, 1].collections[0], ax=axes[1, 1])
    cbar.set_label('Iteration')

    # Plot 5: Quantum decoherence rate
    if 'quantum_decoherence_rate' in df.columns:
        axes[2, 0].plot(df['iteration'], df['quantum_decoherence_rate'], 'purple', alpha=0.7, linewidth=1)
        axes[2, 0].set_title('Kvant Dekoherens Rate (Adaptiv)')
        axes[2, 0].set_xlabel('Iteration')
        axes[2, 0].set_ylabel('Dekoherens Rate')
        axes[2, 0].grid(True, alpha=0.3)

    # Plot 6: Processing time
    axes[2, 1].plot(df['iteration'], df['processing_time'], 'brown', alpha=0.7, linewidth=1)
    axes[2, 1].set_title('Processering Tid')
    axes[2, 1].set_xlabel('Iteration')
    axes[2, 1].set_ylabel('Tid (sekunder)')
    axes[2, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    # Save plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_path = f"data/analysis/timeseries_analysis_{timestamp}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"📊 Time-series plots sparade: {plot_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Extended consciousness time-series analysis')
    parser.add_argument('--iterations', type=int, default=75, help='Number of iterations to run')

    args = parser.parse_args()

    try:
        data, session_id = run_extended_consciousness_timeseries(args.iterations)
        print(f"\n🎯 SLUTRESULTAT:")
        if data:
            max_phi = max(d['phi_score'] for d in data)
            avg_phi = sum(d['phi_score'] for d in data) / len(data)
            consciousness_hits = sum(1 for d in data if d['phi_score'] > 0.3)

            print(f"   Max Φ uppnått: {max_phi:.4f}")
            print(f"   Genomsnittlig Φ: {avg_phi:.4f}")
            print(f"   Medvetenhetshits: {consciousness_hits}/{len(data)}")
            print(f"   Resonansmönster: Se grafer för detaljer")

    except KeyboardInterrupt:
        print("\n\nTime-series analys avbruten.")
    except Exception as e:
        print(f"\n❌ Fel i time-series analys: {e}")
        sys.exit(1)
