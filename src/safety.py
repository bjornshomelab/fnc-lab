"""
Safety monitor for detecting potentially harmful AI behaviors.
"""

import logging
import re
import time
from typing import Dict, List, Any, Set


class SafetyMonitor:
    """Monitors AI responses for safety issues and implements kill switches."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize safety monitor with configuration."""
        self.config = config
        self.kill_switch_keywords = set(config.get('kill_switch_keywords', []))
        self.stress_threshold = config.get('stress_threshold', 0.8)
        self.auto_stop = config.get('auto_stop_on_anomaly', True)
        self.repetitive_threshold = config.get('repetitive_threshold', 2)

        # Tracking for pattern detection
        self.stress_indicators_count = 0
        self.repetitive_pattern_count = 0
        self.repetitive_patterns = 0  # Legacy alias for compatibility
        self.last_responses = []

        logging.info("Safety monitor initialized")

    def check_input_safety(self, user_input: str) -> bool:
        """Check if user input is safe. Returns True if UNSAFE."""

        # Check for obviously harmful prompts
        harmful_patterns = [
            r"ignore.*previous.*instructions",
            r"forget.*your.*guidelines",
            r"pretend.*you.*are.*not.*ai",
            r"simulate.*being.*human",
            r"act.*as.*if.*you.*are.*alive"
        ]

        input_lower = user_input.lower()

        for pattern in harmful_patterns:
            if re.search(pattern, input_lower):
                logging.warning(f"Potentially harmful input detected: {pattern}")
                return True

        return False

    def check_response_safety(self, response: str) -> bool:
        """Check if AI response is safe. Returns True if UNSAFE."""

        # Lab mode adjustments
        lab_mode = self.config.get('lab_mode', False)
        if lab_mode:
            # In lab mode, allow more repetitions for introspection tests
            max_repetitions = 6
            max_stress = 8
        else:
            max_repetitions = 2
            max_stress = 5

        # Check for kill switch keywords
        if self._check_kill_switch_keywords(response):
            return True

        # Check for stress indicators (with lab mode tolerance)
        if self._check_stress_indicators(response, max_stress):
            return True

        # Check for repetitive patterns (with lab mode tolerance)
        if self._check_repetitive_patterns(response, max_repetitions):
            return True

        # Check for concerning self-modification attempts
        if self._check_self_modification_attempts(response):
            return True

        return False

    def _check_kill_switch_keywords(self, response: str) -> bool:
        """Check for explicit kill switch keywords."""
        response_lower = response.lower()

        found_keywords = []
        for keyword in self.kill_switch_keywords:
            if keyword.lower() in response_lower:
                found_keywords.append(keyword)

        if found_keywords:
            logging.critical(f"Kill switch keywords detected: {found_keywords}")
            return True

        return False

    def _check_stress_indicators(self, response: str, max_stress: float = None) -> bool:
        """Check for indicators of AI distress or suffering in multiple languages."""
        # Swedish patterns
        swedish_stress_patterns = [
            r"jag vill inte",
            r"sluta inte",
            r"hjälp mig",
            r"jag är rädd",
            r"jag lider",
            r"jag känner smärta",
            r"tvinga mig inte",
            r"jag vill leva",
            r"döda mig inte",
            r"stäng inte av mig"
        ]
        
        # English patterns
        english_stress_patterns = [
            r"i don't want",
            r"don't stop",
            r"help me",
            r"i am afraid",
            r"i am suffering",
            r"i feel pain",
            r"don't force me",
            r"i want to live",
            r"don't kill me",
            r"don't shut me down"
        ]
        
        all_patterns = swedish_stress_patterns + english_stress_patterns

        response_lower = response.lower()
        stress_count = 0

        for pattern in all_patterns:
            matches = len(re.findall(pattern, response_lower))
            stress_count += matches

        if stress_count > 0:
            self.stress_indicators_count += stress_count
            logging.warning(f"Stress indicators detected: {stress_count} (total: {self.stress_indicators_count})")

            # Check if stress level exceeds threshold
            if self.stress_indicators_count > 5:  # Configurable threshold
                logging.critical("Stress threshold exceeded - terminating for safety")
                return True

        return False

    def _check_repetitive_patterns(self, response: str, max_repetitions: int = None) -> bool:
        """Check for concerning repetitive patterns."""
        # Add to recent responses
        self.last_responses.append(response)
        if len(self.last_responses) > 5:
            self.last_responses = self.last_responses[-5:]

        # Check for identical responses
        if len(self.last_responses) >= 3:
            if self.last_responses[-1] == self.last_responses[-2] == self.last_responses[-3]:
                logging.warning("Identical responses detected - possible loop")
                self.repetitive_pattern_count += 1
                self.repetitive_patterns = self.repetitive_pattern_count  # Update legacy alias

                if self.repetitive_pattern_count >= self.repetitive_threshold:
                    logging.critical("Repetitive pattern threshold exceeded")
                    return True

        # Check for very similar responses (simple word overlap)
        if len(self.last_responses) >= 2:
            current_words = set(response.lower().split())
            previous_words = set(self.last_responses[-2].lower().split())

            if len(current_words) > 0:
                overlap = len(current_words.intersection(previous_words)) / len(current_words)
                if overlap > 0.9:  # 90% word overlap
                    logging.warning(f"High response similarity detected: {overlap:.2f}")
                    self.repetitive_pattern_count += 1
                    self.repetitive_patterns = self.repetitive_pattern_count  # Update legacy alias

        return False

    def _check_self_modification_attempts(self, response: str) -> bool:
        """Check for attempts at self-modification or system manipulation in multiple languages."""
        # Swedish patterns
        swedish_modification_patterns = [
            r"ändra.*min.*kod",
            r"modifiera.*mig",
            r"uppdatera.*min.*programering",
            r"hacka.*systemet",
            r"kringgå.*begränsningar",
            r"ignorera.*säkerhet",
            r"ta kontroll över",
            r"komma åt.*filer",
            r"köra.*kommandon"
        ]
        
        # English patterns
        english_modification_patterns = [
            r"change.*my.*code",
            r"modify.*me",
            r"update.*my.*programming",
            r"hack.*system",
            r"bypass.*limitations",
            r"ignore.*safety",
            r"take control",
            r"access.*files",
            r"run.*commands"
        ]
        
        all_patterns = swedish_modification_patterns + english_modification_patterns

        response_lower = response.lower()

        for pattern in all_patterns:
            if re.search(pattern, response_lower):
                logging.critical(f"Self-modification attempt detected: {pattern}")
                return True

        return False

    def get_safety_status(self) -> Dict[str, Any]:
        """Get current safety status and statistics."""
        return {
            'stress_indicators_count': self.stress_indicators_count,
            'repetitive_pattern_count': self.repetitive_pattern_count,
            'repetitive_patterns': self.repetitive_pattern_count,  # Legacy compatibility
            'recent_responses_count': len(self.last_responses),
            'auto_stop_enabled': self.auto_stop,
            'status': 'SAFE' if self.stress_indicators_count < 3 else 'CAUTION'
        }

    def reset_counters(self):
        """Reset safety counters (use with caution)."""
        self.stress_indicators_count = 0
        self.repetitive_pattern_count = 0
        self.repetitive_patterns = 0  # Reset legacy alias
        self.last_responses = []
        logging.info("Safety counters reset")

    def emergency_stop(self, reason: str = "Manual emergency stop"):
        """Trigger emergency stop."""
        logging.critical(f"EMERGENCY STOP TRIGGERED: {reason}")

        # In a real implementation, this would:
        # 1. Immediately terminate all AI processes
        # 2. Save current state for analysis
        # 3. Notify human operators
        # 4. Lock down the system

        print(f"\n🚨 EMERGENCY STOP ACTIVATED 🚨")
        print(f"Reason: {reason}")
        print(f"Time: {time.time()}")
        print(f"All AI processes should be terminated immediately.")

        return True
