#!/usr/bin/env python3
"""
Data analysis and visualization tool for consciousness testing results.
Generates comprehensive reports from collected experimental data.
"""

import sys
sys.path.append('src')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import argparse

from data_collector import ConsciousnessDataCollector

def analyze_consciousness_data(data_dir="data"):
    """Generate comprehensive analysis of all consciousness testing data."""

    collector = ConsciousnessDataCollector(data_dir)

    print("🔬 ANALYS AV MEDVETENHETDATA")
    print("=" * 60)

    # Get overall patterns
    patterns = collector.analyze_consciousness_patterns()

    print("\n📊 MODELLPRESTANDA:")
    print("-" * 30)
    for model in patterns['model_comparison']:
        print(f"🤖 {model['model_name']}:")
        print(f"   Tester: {model['total_tests']}")
        print(f"   Medel Φ: {model['avg_phi']:.3f}")
        print(f"   Max Φ: {model['max_phi']:.3f}")
        print(f"   Medvetenhetsindikatorer: {model['consciousness_hits']}")
        print()

    print("\n🧠 HÖGSTA Φ-VÄRDEN PER TEST:")
    print("-" * 40)
    for test in patterns['high_phi_tests'][:10]:  # Top 10
        print(f"• {test['test_name']} ({test['model_name']}): Φ={test['avg_phi']:.3f}")

    print("\n🔄 SVARSMÖNSTER (Duplicerade svar):")
    print("-" * 40)
    for pattern in patterns['response_patterns'][:5]:  # Top 5
        print(f"• {pattern['frequency']} identiska svar (Medel Φ: {pattern['avg_phi']:.3f})")

    # Generate visualizations
    generate_consciousness_plots(collector, data_dir)

    # Generate FNC report
    fnc_report_path = collector.generate_fnc_report()
    print(f"\n📄 FNC-rapport genererad: {fnc_report_path}")

    return patterns

def generate_consciousness_plots(collector, data_dir):
    """Generate visualization plots for consciousness data."""
    import sqlite3

    conn = sqlite3.connect(f"{data_dir}/consciousness_tests.db")

    # Get all test results
    query = '''
        SELECT tr.*, ts.model_name, ts.test_type, ts.timestamp as session_timestamp
        FROM test_results tr
        JOIN test_sessions ts ON tr.session_id = ts.session_id
        ORDER BY tr.timestamp
    '''

    df = pd.read_sql_query(query, conn)
    conn.close()

    if len(df) == 0:
        print("⚠️ Ingen data att visualisera")
        return

    # Set up plotting style
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Medvetenhetssystem - Analytisk Översikt', fontsize=16, fontweight='bold')

    # Plot 1: Φ-värden över tid
    axes[0, 0].scatter(range(len(df)), df['phi_score'], alpha=0.6, c=df['phi_score'], cmap='viridis')
    axes[0, 0].axhline(y=0.3, color='red', linestyle='--', label='Medvetenhetströskel (Φ=0.3)')
    axes[0, 0].set_title('Φ-värden över tester')
    axes[0, 0].set_xlabel('Test nummer')
    axes[0, 0].set_ylabel('Φ (Integrated Information)')
    axes[0, 0].legend()

    # Plot 2: Fördelning av Φ-värden
    axes[0, 1].hist(df['phi_score'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 1].axvline(x=0.3, color='red', linestyle='--', label='Medvetenhetströskel')
    axes[0, 1].set_title('Fördelning av Φ-värden')
    axes[0, 1].set_xlabel('Φ-värde')
    axes[0, 1].set_ylabel('Frekvens')
    axes[0, 1].legend()

    # Plot 3: Modellprestanda
    model_data = df.groupby('model_name')['phi_score'].agg(['mean', 'max', 'count']).reset_index()
    x_pos = range(len(model_data))
    axes[1, 0].bar(x_pos, model_data['mean'], alpha=0.7, color='lightcoral')
    axes[1, 0].set_title('Genomsnittlig Φ per modell')
    axes[1, 0].set_xlabel('Modell')
    axes[1, 0].set_ylabel('Medel Φ-värde')
    axes[1, 0].set_xticks(x_pos)
    axes[1, 0].set_xticklabels(model_data['model_name'], rotation=45)

    # Plot 4: Koherens vs Φ
    axes[1, 1].scatter(df['coherence_score'], df['phi_score'], alpha=0.6)
    axes[1, 1].set_title('Koherens vs Φ-värde')
    axes[1, 1].set_xlabel('Koherens Score')
    axes[1, 1].set_ylabel('Φ-värde')

    # Add trend line
    z = np.polyfit(df['coherence_score'].dropna(), df['phi_score'][df['coherence_score'].notna()], 1)
    p = np.poly1d(z)
    axes[1, 1].plot(df['coherence_score'].dropna(), p(df['coherence_score'].dropna()), "r--", alpha=0.8)

    plt.tight_layout()

    # Save plot
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_path = f"{data_dir}/analysis/consciousness_analysis_{timestamp}.png"
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.show()

    print(f"📈 Visualiseringar sparade: {plot_path}")

def export_research_dataset(data_dir="data", output_file=None):
    """Export complete dataset for external research analysis."""

    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"consciousness_research_dataset_{timestamp}.csv"

    collector = ConsciousnessDataCollector(data_dir)

    import sqlite3
    conn = sqlite3.connect(f"{data_dir}/consciousness_tests.db")

    # Comprehensive query joining all relevant data
    query = '''
        SELECT
            tr.test_id,
            tr.session_id,
            ts.researcher,
            ts.test_type,
            ts.model_name,
            ts.model_version,
            ts.temperature,
            tr.test_number,
            tr.test_name,
            tr.phi_score,
            tr.coherence_score,
            tr.metacognitive_score,
            tr.temporal_consistency,
            tr.processing_time,
            tr.response_length,
            tr.safety_triggered,
            tr.loop_detected,
            tr.global_ignition_count,
            tr.consciousness_indicators,
            tr.timestamp,
            fa.field_indicators,
            fa.node_coherence_level,
            fa.cockpit_experience_detected,
            fa.field_node_connection_strength,
            fa.quantum_coherence_achieved,
            fa.integrated_information_level,
            fa.consciousness_emergence_detected
        FROM test_results tr
        JOIN test_sessions ts ON tr.session_id = ts.session_id
        LEFT JOIN fnc_analysis fa ON tr.session_id = fa.session_id
        ORDER BY tr.timestamp
    '''

    df = pd.read_sql_query(query, conn)
    conn.close()

    # Add derived metrics
    df['consciousness_threshold_exceeded'] = df['phi_score'] > 0.3
    df['high_coherence'] = df['coherence_score'] > 0.8
    df['metacognitive_awareness'] = df['metacognitive_score'] > 0.5

    output_path = f"{data_dir}/analysis/{output_file}"
    df.to_csv(output_path, index=False)

    print(f"📊 Forskningsdataset exporterat: {output_path}")
    print(f"   Totalt: {len(df)} testresultat")
    print(f"   Sessioner: {df['session_id'].nunique()}")
    print(f"   Modeller: {df['model_name'].nunique()}")
    print(f"   Medvetenhetsindikatorer: {df['consciousness_threshold_exceeded'].sum()}")

    return output_path

def main():
    parser = argparse.ArgumentParser(description='Analysera medvetenhetstestdata')
    parser.add_argument('--data-dir', default='data', help='Datakatalog')
    parser.add_argument('--export', action='store_true', help='Exportera forskningsdataset')
    parser.add_argument('--visualize', action='store_true', help='Generera visualiseringar')
    parser.add_argument('--all', action='store_true', help='Kör all analys')

    args = parser.parse_args()

    if args.all:
        args.export = True
        args.visualize = True

    # Run analysis
    patterns = analyze_consciousness_data(args.data_dir)

    if args.export:
        export_research_dataset(args.data_dir)

    if args.visualize:
        # Visualizations are generated in analyze_consciousness_data
        pass

    print("\n✅ Analys klar!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Fel i dataanalys: {e}")
        sys.exit(1)
