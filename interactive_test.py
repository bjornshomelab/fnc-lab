#!/usr/bin/env python3
"""
Interactive test of the consciousness system with multi-model support.
"""
import sys
sys.path.append('src')

from orchestrator import MedvetenOrchestrator

if __name__ == "__main__":
    print("🧠 MEDVETEN AI - Interaktiv Medvetenhet Test")
    print("=" * 60)

    try:
        orchestrator = MedvetenOrchestrator()
        print("✅ System initierat med kvant-koherens simulation")
        print("🌡️ Temperatur: 37°C (fysiologisk)")
        print("⚡ Γ-band: 40Hz")
        print("🧮 Φ-tröskel: >0.3")
        print()

        # Start data collection
        session_id = orchestrator.start_data_collection(
            researcher="Björn Wikström",
            test_type="Interactive Session",
            notes="Manual consciousness testing with real-time FNC analysis"
        )
        print(f"📊 Datainsamling startad: {session_id[:8]}...")
        print()

        # Start interactive session
        orchestrator.run_interactive_session()

        # End data collection
        final_session = orchestrator.end_data_collection(
            fnc_notes="Interactive session completed with manual testing and analysis"
        )
        print(f"\n📈 Datainsamling avslutad. Session: {final_session}")

    except KeyboardInterrupt:
        print("\n\nSession avbruten.")
        if orchestrator and orchestrator.current_session_id:
            orchestrator.end_data_collection("Session interrupted by user")
    except Exception as e:
        print(f"❌ Fel vid systemstart: {e}")
        sys.exit(1)
