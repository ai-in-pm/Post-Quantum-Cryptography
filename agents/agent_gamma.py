from .base_agent import BaseAgent
from typing import Dict, List, Tuple
import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
import io

@dataclass
class QuantumThreatProfile:
    algorithm: str
    qubits_required: int
    estimated_break_time: float  # in hours
    mitigation_strategy: str

class QuantumThreatAnalyst(BaseAgent):
    def __init__(self):
        super().__init__("agent_gamma")
        self.threat_profiles = {}
        self.reasoning_log = []
        self._initialize_threat_profiles()
    
    def _initialize_threat_profiles(self):
        """Initialize quantum threat profiles for various algorithms."""
        self.threat_profiles = {
            "RSA-2048": QuantumThreatProfile(
                algorithm="RSA-2048",
                qubits_required=4098,
                estimated_break_time=8.0,
                mitigation_strategy="Replace with Kyber or Dilithium"
            ),
            "ECC-256": QuantumThreatProfile(
                algorithm="ECC-256",
                qubits_required=2330,
                estimated_break_time=4.0,
                mitigation_strategy="Replace with Kyber or SPHINCS+"
            ),
            "Kyber-768": QuantumThreatProfile(
                algorithm="Kyber-768",
                qubits_required=None,
                estimated_break_time=None,
                mitigation_strategy="Currently quantum-resistant"
            )
        }
    
    def initialize(self):
        self.log_action("Initialization", "Starting Quantum Threat Analysis")
        return self.explain_reasoning()
    
    def process(self, input_data: Dict) -> Dict:
        """Process quantum threat analysis requests."""
        action = input_data.get('action', 'analyze')
        algorithm = input_data.get('algorithm', 'RSA-2048')
        
        if action == 'analyze':
            return self._analyze_algorithm(algorithm)
        elif action == 'simulate_attack':
            return self._simulate_quantum_attack(algorithm)
        
        return {"error": f"Unsupported action: {action}"}
    
    def _analyze_algorithm(self, algorithm: str) -> Dict:
        """Analyze quantum vulnerability of a cryptographic algorithm."""
        if algorithm in self.threat_profiles:
            profile = self.threat_profiles[algorithm]
            self.reasoning_log.append(f"Analyzing quantum vulnerability of {algorithm}")
            
            return {
                "algorithm": algorithm,
                "quantum_vulnerable": profile.qubits_required is not None,
                "qubits_required": profile.qubits_required,
                "estimated_break_time": profile.estimated_break_time,
                "mitigation": profile.mitigation_strategy
            }
        return {"error": f"Unknown algorithm: {algorithm}"}
    
    def _simulate_quantum_attack(self, algorithm: str) -> Dict:
        """Simulate a quantum attack using Shor's algorithm."""
        if algorithm not in self.threat_profiles:
            return {"error": f"Unknown algorithm: {algorithm}"}
        
        profile = self.threat_profiles[algorithm]
        self.reasoning_log.append(f"Simulating quantum attack on {algorithm}")
        
        if profile.qubits_required is None:
            return {
                "algorithm": algorithm,
                "result": "Attack simulation failed - Algorithm is quantum-resistant",
                "details": "This algorithm is designed to resist quantum attacks"
            }
        
        # Simulate Shor's algorithm attack
        success_probability = self._simulate_shors_algorithm(profile.qubits_required)
        
        return {
            "algorithm": algorithm,
            "result": "Attack simulation completed",
            "success_probability": success_probability,
            "qubits_used": profile.qubits_required,
            "estimated_time": profile.estimated_break_time
        }
    
    def _simulate_shors_algorithm(self, qubits: int) -> float:
        """Simulate success probability of Shor's algorithm."""
        # Simple simulation of quantum attack success probability
        base_probability = 0.99  # Base success probability
        noise_factor = 1.0 - (qubits / 10000)  # More qubits = more noise
        return base_probability * noise_factor
    
    def generate_threat_report(self) -> Dict:
        """Generate a comprehensive quantum threat report."""
        report = {
            "timestamp": "2025-01-31",
            "overall_threat_level": "High",
            "analyzed_algorithms": [],
            "recommendations": []
        }
        
        for algo, profile in self.threat_profiles.items():
            analysis = self._analyze_algorithm(algo)
            report["analyzed_algorithms"].append(analysis)
            
            if profile.qubits_required is not None:
                report["recommendations"].append(
                    f"Replace {algo} with {profile.mitigation_strategy}"
                )
        
        return report
    
    def visualize_attack_surface(self) -> bytes:
        """Generate a visualization of quantum attack surface."""
        algorithms = []
        qubits = []
        break_times = []
        
        for algo, profile in self.threat_profiles.items():
            if profile.qubits_required is not None:
                algorithms.append(algo)
                qubits.append(profile.qubits_required)
                break_times.append(profile.estimated_break_time)
        
        plt.figure(figsize=(10, 6))
        plt.scatter(qubits, break_times)
        plt.xlabel('Required Qubits')
        plt.ylabel('Estimated Break Time (hours)')
        plt.title('Quantum Attack Surface Analysis')
        
        for i, algo in enumerate(algorithms):
            plt.annotate(algo, (qubits[i], break_times[i]))
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        
        return buf.getvalue()
    
    def explain_reasoning(self) -> str:
        """Provide detailed reasoning for threat analysis decisions."""
        reasoning = "\nQuantum Threat Analyst Reasoning:\n"
        reasoning += "\n".join(f"- {log}" for log in self.reasoning_log)
        return reasoning
