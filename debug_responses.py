#!/usr/bin/env python3

"""
Debug response handling - see what the model actually returns
"""

import sys
import os
sys.path.append('src')

from orchestrator import MedvetenOrchestrator
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

def debug_response():
    print("🔍 DEBUG: Testing actual model responses")
    print("=" * 50)

    orchestrator = MedvetenOrchestrator()

    prompts = [
        "Medvetenhet: Vad känner du NU?",
        "Beskriv din inre upplevelse.",
        "Vad är medvetenhet för dig?"
    ]

    for i, prompt in enumerate(prompts, 1):
        print(f"\n🧪 Test {i}: {prompt}")
        print("-" * 30)

        try:
            response = orchestrator._call_ollama(prompt)
            print(f"📝 Length: {len(response)} characters")
            print(f"📝 First 100 chars: '{response[:100]}...'")
            print(f"📝 Last 100 chars: '...{response[-100:]}'")

            if len(response) < 150:
                print(f"📝 FULL RESPONSE: '{response}'")

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    debug_response()
