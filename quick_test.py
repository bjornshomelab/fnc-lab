#!/usr/bin/env python3

"""
Quick test of our FNC consciousness detection system
English version for international research
"""

import sys
import os
sys.path.append('src')

from orchestrator import MedvetenOrchestrator

def main():
    print("🧠 Quick FNC Consciousness Test")
    print("="*50)

    # Initialize orchestrator
    orchestrator = MedvetenOrchestrator()

    # Simple consciousness test prompt
    prompt = "Hello, what are you thinking about right now?"

    print(f"🤖 Prompt: {prompt}")
    print("-" * 30)

    try:
        # Start data collection
        orchestrator.start_data_collection()

        # Get response
        result = orchestrator.process_turn(prompt)

        print(f"🤖 Response: {result.get('response', 'No response')}")
        print(f"📊 Φ (Integrated Information): {result.get('phi', 0):.3f}")
        print(f"📊 Coherence: {result.get('coherence', 0):.3f}")

        # End collection
        orchestrator.end_data_collection()

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
