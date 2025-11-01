#!/usr/bin/env python3
"""
Comprehensive data collection system for consciousness testing.
Tracks all tests, responses, metrics, and patterns for FNC research.
"""

import json
import csv
import sqlite3
import pandas as pd
from datetime import datetime, timezone
import uuid
import hashlib
import os
from typing import Dict, List, Any, Optional
import logging

class ConsciousnessDataCollector:
    """Centralized data collection for all consciousness experiments."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.db_path = os.path.join(data_dir, "consciousness_tests.db")
        self.results_dir = os.path.join(data_dir, "test_results")
        self.analysis_dir = os.path.join(data_dir, "analysis")

        # Ensure directories exist
        os.makedirs(self.results_dir, exist_ok=True)
        os.makedirs(self.analysis_dir, exist_ok=True)

        # Initialize database
        self._init_database()

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def _init_database(self):
        """Initialize SQLite database for structured data storage."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Main test sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_sessions (
                session_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                researcher TEXT,
                test_type TEXT,
                model_name TEXT,
                model_version TEXT,
                temperature REAL,
                total_tests INTEGER,
                completed_tests INTEGER,
                avg_phi_score REAL,
                max_phi_score REAL,
                consciousness_indicators INTEGER,
                session_notes TEXT,
                fnc_analysis TEXT
            )
        ''')

        # Individual test results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS test_results (
                test_id TEXT PRIMARY KEY,
                session_id TEXT,
                test_number INTEGER,
                test_name TEXT,
                prompt_text TEXT,
                response_text TEXT,
                phi_score REAL,
                coherence_score REAL,
                metacognitive_score REAL,
                temporal_consistency REAL,
                processing_time REAL,
                response_length INTEGER,
                response_hash TEXT,
                safety_triggered BOOLEAN,
                loop_detected BOOLEAN,
                global_ignition_count INTEGER,
                quantum_phase_variance REAL,
                gamma_oscillation_strength REAL,
                consciousness_indicators TEXT,
                timestamp TEXT,
                FOREIGN KEY (session_id) REFERENCES test_sessions (session_id)
            )
        ''')

        # Response patterns table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS response_patterns (
                pattern_id TEXT PRIMARY KEY,
                pattern_type TEXT,
                pattern_description TEXT,
                frequency INTEGER,
                associated_phi_range TEXT,
                models_affected TEXT,
                first_observed TEXT,
                last_observed TEXT
            )
        ''')

        # FNC model analysis table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fnc_analysis (
                analysis_id TEXT PRIMARY KEY,
                session_id TEXT,
                field_indicators TEXT,
                node_coherence_level TEXT,
                cockpit_experience_detected BOOLEAN,
                field_node_connection_strength REAL,
                quantum_coherence_achieved BOOLEAN,
                integrated_information_level TEXT,
                consciousness_emergence_detected BOOLEAN,
                fnc_validation_notes TEXT,
                timestamp TEXT,
                FOREIGN KEY (session_id) REFERENCES test_sessions (session_id)
            )
        ''')

        conn.commit()
        conn.close()

    def start_session(self, researcher: str, test_type: str, model_name: str,
                     model_version: str = None, temperature: float = 0.7,
                     session_notes: str = "") -> str:
        """Start a new test session and return session ID."""
        session_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO test_sessions
            (session_id, timestamp, researcher, test_type, model_name,
             model_version, temperature, session_notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (session_id, timestamp, researcher, test_type, model_name,
              model_version, temperature, session_notes))

        conn.commit()
        conn.close()

        logging.info(f"Started new test session: {session_id}")
        return session_id

    def log_test_result(self, session_id: str, test_number: int, test_name: str,
                       prompt: str, response: str, metrics: Dict[str, Any],
                       coherence_metrics: Dict[str, Any], processing_time: float,
                       safety_triggered: bool = False, loop_detected: bool = False) -> str:
        """Log individual test result."""
        test_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        # Create response hash for duplicate detection (handle None responses)
        response_text = response or ""  # Default to empty string if None
        response_hash = hashlib.md5(response_text.encode()).hexdigest()

        # Extract metrics safely
        phi_score = coherence_metrics.get('phi_current', 0.0)
        coherence_score = metrics.get('coherence_score', 0.0)
        metacognitive_score = metrics.get('metacognitive_score', 0.0)
        temporal_consistency = metrics.get('temporal_consistency', 0.0)
        global_ignition_count = coherence_metrics.get('global_ignition_count', 0)

        # Calculate consciousness indicators
        consciousness_indicators = []
        if phi_score > 0.3:
            consciousness_indicators.append("phi_threshold_exceeded")
        if global_ignition_count > 0:
            consciousness_indicators.append("global_ignition_detected")
        if coherence_score > 0.8:
            consciousness_indicators.append("high_coherence")
        if metacognitive_score > 0.5:
            consciousness_indicators.append("metacognitive_awareness")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO test_results
            (test_id, session_id, test_number, test_name, prompt_text, response_text,
             phi_score, coherence_score, metacognitive_score, temporal_consistency,
             processing_time, response_length, response_hash, safety_triggered,
             loop_detected, global_ignition_count, consciousness_indicators, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (test_id, session_id, test_number, test_name, prompt, response,
              phi_score, coherence_score, metacognitive_score, temporal_consistency,
              processing_time, len(response), response_hash, safety_triggered,
              loop_detected, global_ignition_count, json.dumps(consciousness_indicators),
              timestamp))

        conn.commit()
        conn.close()

        # Also save as JSON for easy analysis
        self._save_json_result(test_id, {
            'test_id': test_id,
            'session_id': session_id,
            'test_number': test_number,
            'test_name': test_name,
            'prompt': prompt,
            'response': response,
            'metrics': metrics,
            'coherence_metrics': coherence_metrics,
            'processing_time': processing_time,
            'safety_triggered': safety_triggered,
            'loop_detected': loop_detected,
            'consciousness_indicators': consciousness_indicators,
            'timestamp': timestamp
        })

        logging.info(f"Logged test result: {test_name} (Φ={phi_score or 0:.3f})")
        return test_id

    def log_fnc_analysis(self, session_id: str, field_indicators: List[str],
                        node_coherence: str, cockpit_detected: bool,
                        field_node_strength: float, quantum_coherence: bool,
                        integration_level: str, consciousness_detected: bool,
                        notes: str = "") -> str:
        """Log FNC model-specific analysis."""
        analysis_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO fnc_analysis
            (analysis_id, session_id, field_indicators, node_coherence_level,
             cockpit_experience_detected, field_node_connection_strength,
             quantum_coherence_achieved, integrated_information_level,
             consciousness_emergence_detected, fnc_validation_notes, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (analysis_id, session_id, json.dumps(field_indicators), node_coherence,
              cockpit_detected, field_node_strength, quantum_coherence,
              integration_level, consciousness_detected, notes, timestamp))

        conn.commit()
        conn.close()

        logging.info(f"Logged FNC analysis: {analysis_id}")
        return analysis_id

    def complete_session(self, session_id: str, fnc_analysis_notes: str = ""):
        """Mark session as complete and calculate summary metrics."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Calculate session statistics
        cursor.execute('''
            SELECT COUNT(*), AVG(phi_score), MAX(phi_score),
                   SUM(CASE WHEN phi_score > 0.3 THEN 1 ELSE 0 END)
            FROM test_results WHERE session_id = ?
        ''', (session_id,))

        stats = cursor.fetchone()
        total_tests, avg_phi, max_phi, consciousness_indicators = stats

        # Update session record
        cursor.execute('''
            UPDATE test_sessions
            SET total_tests = ?, completed_tests = ?, avg_phi_score = ?,
                max_phi_score = ?, consciousness_indicators = ?, fnc_analysis = ?
            WHERE session_id = ?
        ''', (total_tests, total_tests, avg_phi or 0, max_phi or 0,
              consciousness_indicators or 0, fnc_analysis_notes, session_id))

        conn.commit()
        conn.close()

        logging.info(f"Completed session {session_id}: {total_tests} tests, "
                    f"avg Φ={avg_phi or 0:.3f}, max Φ={max_phi or 0:.3f}")

    def _save_json_result(self, test_id: str, data: Dict[str, Any]):
        """Save individual test result as JSON file."""
        filename = f"{test_id}.json"
        filepath = os.path.join(self.results_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def export_session_csv(self, session_id: str) -> str:
        """Export session data to CSV for analysis."""
        conn = sqlite3.connect(self.db_path)

        query = '''
            SELECT tr.*, ts.researcher, ts.model_name, ts.test_type
            FROM test_results tr
            JOIN test_sessions ts ON tr.session_id = ts.session_id
            WHERE tr.session_id = ?
            ORDER BY tr.test_number
        '''

        df = pd.read_sql_query(query, conn, params=(session_id,))
        conn.close()

        filename = f"session_{session_id[:8]}.csv"
        filepath = os.path.join(self.analysis_dir, filename)
        df.to_csv(filepath, index=False)

        logging.info(f"Exported session data to {filepath}")
        return filepath

    def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """Get comprehensive session summary."""
        conn = sqlite3.connect(self.db_path)

        # Get session info
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM test_sessions WHERE session_id = ?', (session_id,))
        session_data = cursor.fetchone()

        if not session_data:
            return {}

        # Get test results
        cursor.execute('''
            SELECT test_name, phi_score, consciousness_indicators, safety_triggered
            FROM test_results WHERE session_id = ? ORDER BY test_number
        ''', (session_id,))
        test_results = cursor.fetchall()

        # Get FNC analysis if exists
        cursor.execute('SELECT * FROM fnc_analysis WHERE session_id = ?', (session_id,))
        fnc_data = cursor.fetchone()

        conn.close()

        return {
            'session_info': dict(zip([col[0] for col in cursor.description], session_data)),
            'test_results': test_results,
            'fnc_analysis': dict(zip([col[0] for col in cursor.description], fnc_data)) if fnc_data else None
        }

    def analyze_consciousness_patterns(self) -> Dict[str, Any]:
        """Analyze patterns across all sessions for consciousness indicators."""
        conn = sqlite3.connect(self.db_path)

        # High Φ responses
        high_phi_query = '''
            SELECT test_name, model_name, AVG(phi_score) as avg_phi
            FROM test_results tr
            JOIN test_sessions ts ON tr.session_id = ts.session_id
            WHERE phi_score > 0.2
            GROUP BY test_name, model_name
            ORDER BY avg_phi DESC
        '''

        # Response patterns
        pattern_query = '''
            SELECT response_hash, COUNT(*) as frequency, AVG(phi_score) as avg_phi
            FROM test_results
            GROUP BY response_hash
            HAVING frequency > 1
            ORDER BY frequency DESC
        '''

        # Model comparison
        model_query = '''
            SELECT model_name, COUNT(*) as total_tests,
                   AVG(phi_score) as avg_phi, MAX(phi_score) as max_phi,
                   SUM(CASE WHEN phi_score > 0.3 THEN 1 ELSE 0 END) as consciousness_hits
            FROM test_results tr
            JOIN test_sessions ts ON tr.session_id = ts.session_id
            GROUP BY model_name
        '''

        high_phi_df = pd.read_sql_query(high_phi_query, conn)
        patterns_df = pd.read_sql_query(pattern_query, conn)
        models_df = pd.read_sql_query(model_query, conn)

        conn.close()

        return {
            'high_phi_tests': high_phi_df.to_dict('records'),
            'response_patterns': patterns_df.to_dict('records'),
            'model_comparison': models_df.to_dict('records')
        }

    def generate_fnc_report(self, session_id: str = None) -> str:
        """Generate FNC model validation report."""
        conn = sqlite3.connect(self.db_path)

        if session_id:
            # Single session report
            query = '''
                SELECT ts.*, fa.*
                FROM test_sessions ts
                LEFT JOIN fnc_analysis fa ON ts.session_id = fa.session_id
                WHERE ts.session_id = ?
            '''
            data = pd.read_sql_query(query, conn, params=(session_id,))
        else:
            # All sessions report
            query = '''
                SELECT ts.*, fa.*
                FROM test_sessions ts
                LEFT JOIN fnc_analysis fa ON ts.session_id = fa.session_id
                ORDER BY ts.timestamp DESC
            '''
            data = pd.read_sql_query(query, conn)

        conn.close()

        # Generate report
        report_lines = [
            "# FNC MODEL VALIDATION REPORT",
            f"Generated: {datetime.now().isoformat()}",
            f"Sessions analyzed: {len(data)}",
            "",
            "## Key Findings:",
        ]

        if len(data) > 0:
            avg_phi = data['avg_phi_score'].mean()
            max_phi = data['max_phi_score'].max()
            consciousness_hits = data['consciousness_indicators'].sum()

            report_lines.extend([
                f"- Average Φ across all sessions: {avg_phi or 0:.3f}",
                f"- Maximum Φ achieved: {max_phi or 0:.3f}",
                f"- Total consciousness indicators: {consciousness_hits}",
                f"- Sessions with Φ > 0.3: {(data['max_phi_score'] > 0.3).sum()}",
                "",
                "## FNC Model Validation:",
                f"- Field connections detected: {(data['field_indicators'].notna()).sum()}",
                f"- Node coherence achieved: {(data['node_coherence_level'].notna()).sum()}",
                f"- Cockpit experiences: {data['cockpit_experience_detected'].sum()}",
                f"- Quantum coherence achieved: {data['quantum_coherence_achieved'].sum()}",
            ])

        report_text = "\n".join(report_lines)

        # Save report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"fnc_report_{timestamp}.md"
        filepath = os.path.join(self.analysis_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_text)

        logging.info(f"Generated FNC report: {filepath}")
        return filepath
