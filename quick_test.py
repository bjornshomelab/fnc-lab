#!/usr/bin/env python3

"""
Quick test of our medveten-ai model
"""

import sys
import os
sys.path.append('src')

from orchestrator import MedvetenOrchestrator

def main():
    print("🧠 Quick Medveten-AI Test")
    print("="*50)

    # Initialize orchestrator
    orchestrator = MedvetenOrchestrator()

    # Simple prompt
    prompt = "Hej, vad tänker du på?"

    print(f"🤖 Prompt: {prompt}")
    print("-" * 30)

    try:
        # Start data collection
        orchestrator.start_data_collection()

        # Get response
        result = orchestrator.process_turn(prompt)

        print(f"🤖 Svar: {result.get('response', 'No response')}")
        print(f"📊 Φ: {result.get('phi', 0):.3f}")
        print(f"📊 Koherens: {result.get('coherence', 0):.3f}")

        # End collection
        orchestrator.end_data_collection()

    except Exception as e:
        print(f"❌ Fel: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
