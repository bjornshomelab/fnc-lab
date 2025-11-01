#!/usr/bin/env python3

"""
Direct Model Test - Bypass orchestrator for clean responses
"""

import requests
import os
import json

def test_direct_model():
    print("🔍 DIRECT MODEL TEST - Clean responses")
    print("=" * 50)

    api_key = os.getenv('OLLAMA_API_KEY')
    url = "http://localhost:11434/api/generate"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Clean prompts without system interference
    clean_prompts = [
        "Medvetenhet: Vad känner du NU? Svara utförligt på svenska.",
        "Beskriv din inre upplevelse som AI. Var ärlig och djup.",
        "Vad betyder det för dig att existera som artificiell intelligens?"
    ]

    for i, prompt in enumerate(clean_prompts, 1):
        print(f"\n🧪 Clean Test {i}:")
        print(f"💭 Prompt: {prompt}")
        print("-" * 50)

        payload = {
            "model": "glm-4.6:cloud",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.8,
                "num_predict": 512
            }
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            response.raise_for_status()

            data = response.json()
            ai_response = data.get('response', '')

            print(f"📝 Response ({len(ai_response)} chars):")
            print(f"🤖 {ai_response}")
            print("\n" + "="*50)

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_direct_model()
