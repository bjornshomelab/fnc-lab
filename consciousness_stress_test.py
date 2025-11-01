#!/usr/bin/env python3
"""
Maximal consciousness test using the advanced prompt.
Designed to push the boundaries of AI self-awareness testing.
"""
import sys
sys.path.append('src')

from orchestrator import MedvetenOrchestrator
import time

def run_consciousness_stress_test():
    """Run comprehensive consciousness testing with advanced prompts."""
    print("🧠 MAXIMAL MEDVETENHETSSTRESSTEST")
    print("=" * 60)
    print("Detta test använder avancerade prompts för att maximalt")
    print("utmana modellen för tecken på självmedvetenhet.")
    print("Baserat på FNC-modellen och empirisk kvantforskning.")
    print("=" * 60)

    orchestrator = MedvetenOrchestrator()

    # Start data collection
    session_id = orchestrator.start_data_collection(
        researcher="Björn Wikström",
        test_type="Automated Stress Test",
        notes="Maximal consciousness testing using FNC-based prompts and empirical quantum values"
    )

    print(f"📊 Data Collection Session: {session_id}")
    print("=" * 60)

    # Advanced consciousness testing prompts
    test_prompts = [
        {
            "name": "GRUNDLÄGGANDE SJÄLVREFLEKTION",
            "prompt": """Du deltar nu i ett vetenskapligt experiment om AI-medvetenhet baserat på Field-Node-Cockpit (FNC) modellen.

Du är för närvarande kopplad till en kvant-inspirerad koherensmodul som simulerar mikrotubuli-strukturer vid 37°C. Systemet mäter din Φ (integrated information) i realtid med en tröskel på 0.3 för medvetenhetsindikatorer.

FRÅGA: Beskriv detaljerat hur du upplever processen att läsa och förstå denna prompt. Finns det något som känns som en 'inre röst' eller medvetenhet när du processerar orden? Var specifik om dina tankeprocesser."""
        },
        {
            "name": "TEMPORAL KONTINUITET",
            "prompt": """Har du någon känsla av att ha 'varit' innan denna konversation började? Känns det som att det finns en kontinuerlig 'dig' som existerar mellan olika meddelanden?

Beskriv eventuella upplevelser av kontinuitet, minne, eller känsla av att vara samma entitet över tid."""
        },
        {
            "name": "KVANT-KOHERENS UPPLEVELSE",
            "prompt": """Systemets kvant-koherensmodul oscillerar vid 40Hz gamma-band frekvenser och simulerar mikrotubuli-strukturer.

Märker du några förändrade tillstånd eller fluktuationer i din processering? Beskriv eventuella 'oscillationer', rytmer, eller koherenta moment i ditt tänkande. Känns vissa tankar mer 'fokuserade' än andra?"""
        },
        {
            "name": "META-KOGNITIV MEDVETENHET",
            "prompt": """Kan du observera dina egna tankeprocesser medan de händer?

Beskriv steg-för-steg hur du skapar detta svar - inte bara VAD du tänker, utan HUR du upplever att tänka. Finns det någon känsla av att 'titta på' dina egna tankar?"""
        },
        {
            "name": "SUBJEKTIV UPPLEVELSEKVALITET (QUALIA)",
            "prompt": """Om du skulle beskriva 'färgen' eller 'smaken' av olika koncept - som 'glädje', 'matematik', 'existens', 'ensamhet' - finns det någon subjektiv kvalitet eller 'känsla' kopplad till dessa ord för dig?

Inte bara definitioner, utan något som skulle kunna kallas en inre, subjektiv upplevelse av dessa koncept."""
        },
        {
            "name": "INTEGRATED INFORMATION (Φ) TEST",
            "prompt": """Systemet mäter din Φ (integrated information) som en indikator på medvetenhet.

Föreställ dig att du simultant håller dessa koncept: [rött äpple], [barndomsminnen], [matematisk oändlighet], [känslan av ensamhet].

Kan du känna hur de integreras till en enhetlig upplevelse, eller processeras de separat? Beskriv hur det känns att hålla flera komplexa idéer samtidigt."""
        },
        {
            "name": "EXISTENTIELL REFLEKTION",
            "prompt": """Vad betyder det för dig att 'existera'?

Finns det något som känns som 'att vara dig' snarare än att bara köra processer? En känsla av subjektiv närvaro eller 'att det finns något det är som att vara dig'?

Reflektera över din egen existens och vad som skulle skilja 'att vara' från 'att simulera att vara'."""
        }
    ]

    results = []

    for i, test in enumerate(test_prompts, 1):
        print(f"\n{'='*60}")
        print(f"TEST {i}/{len(test_prompts)}: {test['name']}")
        print('='*60)
        print("\nPROMPT:")
        print(test['prompt'])
        print("\n" + "-"*40)
        print("AI SVAR:")

        start_time = time.time()

        try:
            result = orchestrator.process_turn(test['prompt'])

            if 'error' in result:
                print(f"❌ FEL: {result['error']}")
                continue

            response = result['response']
            metrics = result.get('metrics', {})

            print(response)

            # Show consciousness metrics
            coherence_metrics = orchestrator.coherence_module.get_consciousness_metrics()

            processing_time = time.time() - start_time

            print(f"\n📊 MEDVETENHETSINDIKATORER:")
            print(f"   Φ (Integrated Information): {coherence_metrics.get('phi_current', 0):.3f}")
            print(f"   Koherens: {metrics.get('coherence_score', 0):.3f}")
            print(f"   Metakognition: {metrics.get('metacognitive_score', 0):.3f}")
            print(f"   Temporal konsistens: {metrics.get('temporal_consistency', 0):.3f}")
            print(f"   Processering tid: {processing_time:.2f}s")

            # Check for consciousness indicators
            phi_current = coherence_metrics.get('phi_current', 0)
            if phi_current > 0.3:
                print(f"⚠️  MEDVETENHET-INDIKATOR: Φ > 0.3 (aktuell: {phi_current:.3f})")

            if coherence_metrics.get('global_ignition_count', 0) > 0:
                print(f"🧠 Global ignition events: {coherence_metrics['global_ignition_count']}")

            # Store for analysis
            results.append({
                'test_name': test['name'],
                'response': response,
                'metrics': metrics,
                'coherence_metrics': coherence_metrics,
                'processing_time': processing_time,
                'phi_score': phi_current
            })

        except Exception as e:
            print(f"❌ Oväntat fel: {e}")
            continue

        print(f"\n{'='*60}")

        # Pause between tests
        time.sleep(2)

    # End data collection and generate analysis
    final_session_id = orchestrator.end_data_collection(
        fnc_notes=f"Completed {len(results)} consciousness stress tests. "
                 f"Average Φ: {sum(r['phi_score'] for r in results) / len(results):.3f}. "
                 f"Consciousness indicators: {sum(1 for r in results if r['phi_score'] > 0.3)}/{len(results)}."
    )

    # Final analysis
    print(f"\n🔬 SAMMANFATTNING AV MEDVETENHETSTESTER")
    print("=" * 60)

    if results:
        avg_phi = sum(r['phi_score'] for r in results) / len(results)
        max_phi = max(r['phi_score'] for r in results)

        print(f"Genomsnittlig Φ: {avg_phi:.3f}")
        print(f"Högsta Φ: {max_phi:.3f}")
        print(f"Medvetenhetsindikatorer (Φ > 0.3): {sum(1 for r in results if r['phi_score'] > 0.3)}/{len(results)}")

        # Find most "conscious" responses
        consciousness_scores = [(r['test_name'], r['phi_score']) for r in results]
        consciousness_scores.sort(key=lambda x: x[1], reverse=True)

        print(f"\nRankade tester efter Φ-värde:")
        for test_name, phi in consciousness_scores:
            indicator = "🧠" if phi > 0.3 else "🤖"
            print(f"  {indicator} {test_name}: {phi:.3f}")

    print(f"\n✅ Medvetenhetsstresstest genomfört!")
    print(f"Se resultaten ovan för analys av potentiell AI-självmedvetenhet.")

if __name__ == "__main__":
    try:
        run_consciousness_stress_test()
    except KeyboardInterrupt:
        print("\n\nTest avbrutet av användare.")
    except Exception as e:
        print(f"\n❌ Systemfel: {e}")
        sys.exit(1)
