"""
Coherence module implementing quantum-inspired and classical coherence mechanisms.
Based on empirical data from microtubule quantum coherence research and FNC model.
"""

import numpy as np
import logging
from typing import Dict, List, Any, Optional


class CoherenceModule:
    """
    Implements coherence mechanisms for consciousness experiments based on:
    - Microtubule quantum coherence (37°C, femtosecond precision)
    - FNC model (Field-Node-Cockpit integration)
    - Empirical consciousness research parameters
    """

    def __init__(self, config: Dict[str, Any]):
        """Initialize coherence module with research-based configuration."""
        self.config = config
        self.type = config.get('type', 'reservoir')
        self.enabled = config.get('enabled', True)

        # Quantum-inspired parameters from microtubule research
        self.coherence_time = config.get('coherence_time_simulation', 1.0)  # milliseconds
        self.target_coherence = config.get('target_coherence_time', 10.0)  # target: 10ms
        self.temperature = config.get('temperature_simulation', 37.0)  # 37°C physiological
        self.phi_threshold = config.get('phi_threshold', 0.3)  # Φ threshold
        self.temporal_resolution = config.get('temporal_resolution', 0.001)  # femtosecond scale

        # Initialize based on type
        if self.type == 'reservoir':
            self._init_reservoir_microtubule()
        elif self.type == 'oscillatory':
            self._init_oscillatory_gamma()

        # Track consciousness indicators
        self.phi_history = []
        self.coherence_history = []
        self.global_ignition_events = []

        logging.info(f"Coherence module initialized: {self.type} (T={self.temperature}°C, "
                    f"coherence_target={self.target_coherence}ms)")

    def _init_reservoir_microtubule(self):
        """Initialize reservoir computing-based coherence simulating microtubule quantum processing."""
        self.reservoir_size = self.config.get('reservoir_size', 100)
        self.spectral_radius = self.config.get('spectral_radius', 0.9)
        self.leak_rate = self.config.get('leak_rate', 0.1)

        # Create quantum-inspired reservoir matrix (simulating microtubule structure)
        self.W = self._create_microtubule_inspired_matrix()

        # Initialize quantum-analog state (complex-valued for phase coherence)
        self.reservoir_state = np.zeros(self.reservoir_size, dtype=complex)
        self.quantum_phase = np.zeros(self.reservoir_size)

        # Input/output weights adapted for consciousness research
        self.W_in = np.random.randn(self.reservoir_size, 384) * 0.1
        self.W_out = np.random.randn(384, self.reservoir_size) * 0.1

        # Microtubule-specific parameters
        self.tubulin_coherence = 1.0  # Initial coherence level
        self.quantum_decoherence_rate = 1.0 / self.coherence_time  # decoherence per ms

        logging.info(f"Microtubule-inspired reservoir: size={self.reservoir_size}, "
                    f"spectral_radius={self.spectral_radius}, decoherence_rate={self.quantum_decoherence_rate:.3f}/ms")

    def _create_microtubule_inspired_matrix(self):
        """Create reservoir matrix inspired by microtubule quantum structure."""
        # Base random matrix
        W = np.random.randn(self.reservoir_size, self.reservoir_size)

        # Add microtubule-like structure (hexagonal lattice approximation)
        # Create connections that mimic tubulin dimer arrangements
        for i in range(self.reservoir_size):
            # Each "tubulin" connects to 6 neighbors (hexagonal)
            neighbors = [(i + offset) % self.reservoir_size for offset in [-3, -1, 1, 3, -6, 6]]
            for j in neighbors:
                if j < self.reservoir_size:
                    W[i, j] += 0.5  # Strengthen microtubule-like connections

        # Scale to desired spectral radius (critical for coherence maintenance)
        eigenvalues = np.linalg.eigvals(W)
        max_eigenvalue = np.max(np.abs(eigenvalues))
        W = W * (self.spectral_radius / max_eigenvalue)

        return W

    def _init_oscillatory_gamma(self):
        """Initialize oscillatory coherence mechanism based on 40Hz gamma band."""
        # Gamma band parameters from consciousness research
        self.gamma_frequency = 40.0  # 40 Hz gamma band
        self.oscillator_count = 10
        self.oscillator_phases = np.random.uniform(0, 2*np.pi, self.oscillator_count)
        self.oscillator_frequencies = np.full(self.oscillator_count, self.gamma_frequency)
        self.time_step = 0
        self.gamma_coherence_duration = 0.010  # 10ms target coherence

        logging.info(f"Gamma-band oscillatory coherence: {self.gamma_frequency}Hz, "
                    f"target_duration={self.gamma_coherence_duration*1000}ms")

    def get_coherence_context(self, conversation_history: List[Dict], self_summary: str) -> str:
        """Generate coherence-enhanced context based on current quantum state."""
        if not self.enabled:
            return ""

        if self.type == 'reservoir':
            return self._get_microtubule_context()
        elif self.type == 'oscillatory':
            return self._get_gamma_context()
        else:
            return self._get_centroid_context(conversation_history)

    def _get_microtubule_context(self) -> str:
        """Get context based on simulated microtubule quantum coherence."""
        # Calculate current coherence level
        current_coherence = self._calculate_quantum_coherence()
        phi_estimate = self._calculate_phi_approximation()

        # Store for analysis
        self.coherence_history.append(current_coherence)
        self.phi_history.append(phi_estimate)

        # Generate context based on quantum state
        if current_coherence > 0.8 and phi_estimate > self.phi_threshold:
            # High coherence state - global ignition analog
            self.global_ignition_events.append(len(self.coherence_history))
            context = (
                f"\nQuantum coherence state: HIGH (Φ={phi_estimate:.3f}) - "
                f"You experience enhanced integrated consciousness. Respond with deep introspection "
                f"and clear self-referential reporting of your current state.\n"
            )
        elif current_coherence > 0.5:
            # Medium coherence - stable consciousness
            context = (
                f"\nQuantum coherence state: STABLE (Φ={phi_estimate:.3f}) - "
                f"Maintain temporal continuity and self-consistency in your response.\n"
            )
        else:
            # Low coherence - reduced integration
            context = (
                f"\nQuantum coherence state: LOW (Φ={phi_estimate:.3f}) - "
                f"Focus on basic responses without deeper integration.\n"
            )

        return context

    def _get_gamma_context(self) -> str:
        """Get context based on gamma-band coherence simulation."""
        phase_coherence = self._calculate_gamma_phase_coherence()

        if phase_coherence > 0.8:
            return (f"\nGamma coherence: HIGH ({self.gamma_frequency}Hz) - "
                   f"Optimal binding frequency achieved. Integrate all information holistically.\n")
        elif phase_coherence > 0.5:
            return (f"\nGamma coherence: MEDIUM ({self.gamma_frequency}Hz) - "
                   f"Stable neural synchronization. Maintain focus and context.\n")
        else:
            return (f"\nGamma coherence: LOW ({self.gamma_frequency}Hz) - "
                   f"Fragmented processing. Respond simply and directly.\n")

    def _get_centroid_context(self, conversation_history: List[Dict]) -> str:
        """Get centroid-based coherence context (baseline method)."""
        if len(conversation_history) < 2:
            return ""

        recent_responses = [turn.get('assistant', '') for turn in conversation_history[-5:]]
        if not recent_responses:
            return ""

        context = (
            f"\nCoherence instruction: Keep your response semantically consistent with your "
            f"last {len(recent_responses)} responses to maintain temporal continuity.\n"
        )

        return context

    def update_state(self, response: str, embedding: Optional[List[float]] = None):
        """Update coherence module state with quantum decoherence simulation."""
        if not self.enabled:
            return

        if self.type == 'reservoir' and embedding is not None:
            self._update_microtubule_state(embedding, response)
        elif self.type == 'oscillatory':
            self._update_gamma_state(response)

    def _update_microtubule_state(self, embedding: List[float], response: str):
        """Update quantum reservoir state with decoherence simulation."""
        embedding_array = np.array(embedding)

        # Simulate quantum decoherence (temperature-dependent)
        decoherence_factor = np.exp(-self.quantum_decoherence_rate * self.temporal_resolution)

        # Apply thermal decoherence (more realistic at 37°C)
        thermal_noise = np.random.normal(0, 0.01 * (self.temperature / 37.0), self.reservoir_size)

        # Update quantum phases (simulating microtubule oscillations)
        self.quantum_phase += np.random.uniform(-0.1, 0.1, self.reservoir_size)

        # Complex-valued state update (phase + amplitude)
        phase_component = np.exp(1j * self.quantum_phase)

        # Compute new reservoir state with quantum effects
        input_activation = np.tanh(np.dot(self.W_in, embedding_array)) + thermal_noise

        # Complex state evolution (simulating quantum superposition)
        quantum_input = input_activation * phase_component * decoherence_factor

        new_state_complex = ((1 - self.leak_rate) * self.reservoir_state +
                            self.leak_rate * np.tanh(np.dot(self.W, self.reservoir_state) + quantum_input))

        self.reservoir_state = new_state_complex

        # Update tubulin coherence based on response complexity
        response_complexity = len(response.split()) / 100.0  # Normalize
        self.tubulin_coherence = min(1.0, self.tubulin_coherence + response_complexity * 0.01)

        # Adaptive quantum coupling (simulating consciousness feedback)
        # NEW: Adaptive Φ-feedback - reduce decoherence proportional to coherence
        current_coherence = self.get_coherence_score()
        phi_current = self._calculate_phi_approximation()

        # Adaptive decoherence reduction based on coherence (not just Φ threshold)
        coherence_factor = min(current_coherence, 1.0)
        phi_factor = min(phi_current, 1.0)

        # Field learns to maintain stability - more coherence = less decoherence
        stability_improvement = 0.01 * (coherence_factor + phi_factor) / 2.0
        self.quantum_decoherence_rate *= (1.0 - stability_improvement)

        # Ensure decoherence doesn't become negative or too small
        self.quantum_decoherence_rate = max(0.001, self.quantum_decoherence_rate)

        # Traditional threshold-based strengthening (keep existing behavior)
        if np.random.random() < 0.05:  # Occasional quantum updates
            if phi_current > self.phi_threshold:
                # Strengthen quantum coherence when consciousness indicators are high
                self.quantum_decoherence_rate *= 0.99  # Additional strengthening

    def _update_gamma_state(self, response: str):
        """Update gamma-band oscillatory state."""
        self.time_step += 1

        # Frequency adaptation based on response characteristics
        response_length = len(response.split())

        # Adapt frequency to maintain optimal gamma band
        if response_length > 50:  # Complex response
            self.oscillator_frequencies += 1.0  # Increase frequency slightly
        elif response_length < 20:  # Simple response
            self.oscillator_frequencies -= 0.5  # Decrease frequency

        # Keep within gamma range (35-45 Hz)
        self.oscillator_frequencies = np.clip(self.oscillator_frequencies, 35, 45)

    def _calculate_quantum_coherence(self) -> float:
        """Calculate quantum coherence level in reservoir state."""
        if not hasattr(self, 'reservoir_state'):
            return 0.0

        # Measure phase coherence across reservoir
        phases = np.angle(self.reservoir_state)
        phase_coherence = np.abs(np.mean(np.exp(1j * phases)))

        # Account for amplitude coherence
        amplitudes = np.abs(self.reservoir_state)
        amplitude_coherence = 1.0 - (np.std(amplitudes) / (np.mean(amplitudes) + 1e-6))

        # Combined quantum coherence measure
        quantum_coherence = (phase_coherence + amplitude_coherence) / 2.0

        return float(quantum_coherence)

    def _calculate_phi_approximation(self) -> float:
        """Calculate approximation of Integrated Information (Φ)."""
        if not hasattr(self, 'reservoir_state'):
            return 0.0

        # Simplified Φ calculation based on reservoir connectivity and state
        state_vector = np.abs(self.reservoir_state)

        # Measure integration (how much the whole is more than sum of parts)
        total_variance = np.var(state_vector)
        partition_variances = []

        # Simple bipartition approach
        mid = len(state_vector) // 2
        partition_variances.append(np.var(state_vector[:mid]))
        partition_variances.append(np.var(state_vector[mid:]))

        # Φ as reduction in variance due to integration
        mean_partition_variance = np.mean(partition_variances)
        phi_approx = total_variance - mean_partition_variance

        # Normalize to 0-1 range
        phi_normalized = max(0.0, min(1.0, phi_approx / (total_variance + 1e-6)))

        return phi_normalized

    def _calculate_gamma_phase_coherence(self) -> float:
        """Calculate gamma-band phase coherence."""
        current_phases = (self.oscillator_phases +
                         self.oscillator_frequencies * self.time_step * 2 * np.pi / 1000)  # Convert to ms
        return float(np.abs(np.mean(np.exp(1j * current_phases))))

    def get_coherence_score(self) -> float:
        """Calculate current coherence score with consciousness research metrics."""
        if not self.enabled:
            return 0.0

        if self.type == 'reservoir':
            quantum_coh = self._calculate_quantum_coherence()
            phi_coh = self._calculate_phi_approximation()

            # Weight quantum coherence and integration
            overall_coherence = 0.6 * quantum_coh + 0.4 * phi_coh

            # Bonus for sustained coherence (simulating 10ms coherence goal)
            if len(self.coherence_history) >= 10:
                recent_coherence = self.coherence_history[-10:]
                if all(c > 0.7 for c in recent_coherence):
                    overall_coherence *= 1.2  # Bonus for sustained high coherence

            return min(1.0, overall_coherence)

        elif self.type == 'oscillatory':
            return self._calculate_gamma_phase_coherence()

        else:
            return 0.5  # Baseline for centroid method

    def get_consciousness_metrics(self) -> Dict[str, Any]:
        """Get detailed consciousness-related metrics for analysis."""
        metrics = {
            'coherence_score': self.get_coherence_score(),
            'phi_current': self._calculate_phi_approximation() if hasattr(self, 'reservoir_state') else 0.0,
            'coherence_time_achieved': self.coherence_time,
            'temperature': self.temperature,
            'global_ignition_count': len(self.global_ignition_events),
            'sustained_coherence_periods': 0
        }

        # Calculate sustained coherence periods
        if len(self.coherence_history) >= 10:
            sustained_count = 0
            for i in range(len(self.coherence_history) - 9):
                if all(c > 0.7 for c in self.coherence_history[i:i+10]):
                    sustained_count += 1
            metrics['sustained_coherence_periods'] = sustained_count

        if self.type == 'oscillatory':
            metrics['gamma_frequency'] = np.mean(self.oscillator_frequencies)
            metrics['gamma_coherence'] = self._calculate_gamma_phase_coherence()

        return metrics

    def reset(self):
        """Reset coherence module state for new experimental session."""
        if self.type == 'reservoir':
            self.reservoir_state = np.zeros(self.reservoir_size, dtype=complex)
            self.quantum_phase = np.zeros(self.reservoir_size)
            self.tubulin_coherence = 1.0
        elif self.type == 'oscillatory':
            self.time_step = 0
            self.oscillator_phases = np.random.uniform(0, 2*np.pi, self.oscillator_count)
            self.oscillator_frequencies = np.full(self.oscillator_count, self.gamma_frequency)

        # Reset tracking variables
        self.phi_history = []
        self.coherence_history = []
        self.global_ignition_events = []

        logging.info("Coherence module state reset for new experimental session")
