#!/usr/bin/env python3
"""
Interactive test of the consciousness system with multi-model support.
English version for international research collaboration.
"""
import sys
sys.path.append('src')

from orchestrator import MedvetenOrchestrator

if __name__ == "__main__":
    print("🧠 FNC CONSCIOUSNESS LAB v2 - Interactive Consciousness Test")
    print("=" * 60)

    try:
        orchestrator = MedvetenOrchestrator()
        print("✅ System initialized with quantum-coherence simulation")
        print("🌡️ Temperature: 37°C (physiological)")
        print("⚡ Γ-band: 40Hz")
        print("🧮 Φ-threshold: >0.3")
        print()

        # Start data collection
        session_id = orchestrator.start_data_collection(
            researcher="FNC Lab Team",
            test_type="Interactive Session",
            notes="Manual consciousness testing with real-time FNC analysis"
        )
        print(f"📊 Data collection started: {session_id[:8]}...")
        print()

        # Start interactive session
        orchestrator.run_interactive_session()

        # End data collection
        final_session = orchestrator.end_data_collection(
            fnc_notes="Interactive session completed with manual testing and analysis"
        )
        print(f"\n📈 Data collection completed. Session: {final_session}")

    except KeyboardInterrupt:
        print("\n\nSession interrupted.")
        if orchestrator and orchestrator.current_session_id:
            orchestrator.end_data_collection("Session interrupted by user")
    except Exception as e:
        print(f"❌ System startup error: {e}")
        sys.exit(1)
