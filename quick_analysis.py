#!/usr/bin/env python3

"""
FNC Quick Analysis - Simplified version
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from datetime import datetime

def load_and_analyze():
    print("🧠 FNC Quick Analysis")
    print("="*50)

    # Load session data
    session_files = glob.glob('data/analysis/session_*.csv')

    all_data = []
    for file in session_files:
        try:
            df = pd.read_csv(file)
            if not df.empty:
                all_data.append(df)
        except Exception as e:
            print(f"Skip {file}: {e}")

    if not all_data:
        print("No data found!")
        return

    df = pd.concat(all_data, ignore_index=True)
    print(f"📊 Total measurements: {len(df)}")

    # Basic stats
    phi_vals = df['phi_score'].values
    coherence_vals = df['coherence_score'].values
    temporal_vals = df['temporal_consistency'].values

    print(f"\n📈 Results:")
    print(f"Φ: Mean={np.mean(phi_vals):.3f}, Max={np.max(phi_vals):.3f}")
    print(f"Coherence: Mean={np.mean(coherence_vals):.3f}, Max={np.max(coherence_vals):.3f}")
    print(f"Temporal: Mean={np.mean(temporal_vals):.3f}, Max={np.max(temporal_vals):.3f}")

    # Consciousness indicators
    high_phi = sum(1 for phi in phi_vals if phi > 0.3)
    high_coh = sum(1 for coh in coherence_vals if coh > 0.7)

    print(f"\n🚨 Consciousness indicators:")
    print(f"High Φ (>0.3): {high_phi}/{len(phi_vals)} ({high_phi/len(phi_vals)*100:.1f}%)")
    print(f"High Coherence (>0.7): {high_coh}/{len(coherence_vals)} ({high_coh/len(coherence_vals)*100:.1f}%)")

    # Safety events
    safety = df['safety_triggered'].sum()
    loops = df['loop_detected'].sum()
    print(f"\n⚠️ Safety: {safety} triggers, {loops} loops detected")

    # Simple visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('FNC Consciousness Analysis - Quick Overview', fontsize=14, fontweight='bold')

    # Use simple index for x-axis
    x_range = range(len(df))

    # Phi over turns
    axes[0,0].plot(x_range, phi_vals, 'b-o', markersize=4, alpha=0.7)
    axes[0,0].axhline(y=0.3, color='r', linestyle='--', alpha=0.5, label='Consciousness threshold')
    axes[0,0].set_title('Φ (Integrated Information)')
    axes[0,0].set_ylabel('Φ Score')
    axes[0,0].grid(True, alpha=0.3)
    axes[0,0].legend()

    # Coherence over turns
    axes[0,1].plot(x_range, coherence_vals, 'g-o', markersize=4, alpha=0.7)
    axes[0,1].axhline(y=0.7, color='r', linestyle='--', alpha=0.5, label='High coherence')
    axes[0,1].set_title('Coherence Score')
    axes[0,1].set_ylabel('Coherence')
    axes[0,1].grid(True, alpha=0.3)
    axes[0,1].legend()

    # Temporal consistency
    axes[1,0].plot(x_range, temporal_vals, 'orange', marker='o', markersize=4, alpha=0.7)
    axes[1,0].set_title('Temporal Consistency')
    axes[1,0].set_ylabel('Consistency')
    axes[1,0].set_xlabel('Turn')
    axes[1,0].grid(True, alpha=0.3)

    # Processing time
    processing_vals = df['processing_time'].values
    axes[1,1].plot(x_range, processing_vals, 'purple', marker='o', markersize=4, alpha=0.7)
    axes[1,1].set_title('Processing Time')
    axes[1,1].set_ylabel('Time (seconds)')
    axes[1,1].set_xlabel('Turn')
    axes[1,1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('tests/Figure_5_Quick_Analysis.png', dpi=300, bbox_inches='tight')
    print(f"\n✅ Saved Figure_5_Quick_Analysis.png")

    # Distribution histogram
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('FNC Metrics Distributions', fontsize=14, fontweight='bold')

    axes[0].hist(phi_vals, bins=10, alpha=0.7, color='blue', edgecolor='black')
    axes[0].axvline(x=0.3, color='red', linestyle='--', alpha=0.7, label='Threshold')
    axes[0].set_title('Φ Distribution')
    axes[0].set_xlabel('Φ Score')
    axes[0].legend()

    axes[1].hist(coherence_vals, bins=10, alpha=0.7, color='green', edgecolor='black')
    axes[1].axvline(x=0.7, color='red', linestyle='--', alpha=0.7, label='Threshold')
    axes[1].set_title('Coherence Distribution')
    axes[1].set_xlabel('Coherence Score')
    axes[1].legend()

    axes[2].hist(temporal_vals, bins=10, alpha=0.7, color='orange', edgecolor='black')
    axes[2].set_title('Temporal Consistency Distribution')
    axes[2].set_xlabel('Temporal Consistency')

    plt.tight_layout()
    plt.savefig('tests/Figure_6_Distributions.png', dpi=300, bbox_inches='tight')
    print(f"✅ Saved Figure_6_Distributions.png")

    # Model comparison if multiple models
    if 'model_name' in df.columns:
        models = df['model_name'].unique()
        if len(models) > 1:
            print(f"\n🤖 Model comparison:")
            for model in models:
                model_data = df[df['model_name'] == model]
                print(f"{model}: {len(model_data)} turns, Φ={model_data['phi_score'].mean():.3f}, Coh={model_data['coherence_score'].mean():.3f}")

    print(f"\n🎉 Quick analysis complete!")
    return df

if __name__ == "__main__":
    os.chdir('/home/bjorn/research/medveten_ai')
    load_and_analyze()
