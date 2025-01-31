from .base_agent import BaseAgent
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import asyncio
import time
import numpy as np
import matplotlib.pyplot as plt
import io
from datetime import datetime

@dataclass
class SimulationMetrics:
    latency_ms: float
    cpu_usage: float
    memory_mb: float
    bandwidth_mbps: float
    timestamp: str

@dataclass
class SimulationScenario:
    name: str
    description: str
    parameters: Dict
    duration_seconds: int

class SimulationController(BaseAgent):
    def __init__(self):
        super().__init__("agent_zeta")
        self.scenarios = {}
        self.metrics_history = []
        self.reasoning_log = []
        self._initialize_scenarios()
    
    def _initialize_scenarios(self):
        """Initialize simulation scenarios."""
        self.scenarios = {
            "secure_communication": SimulationScenario(
                name="secure_communication",
                description="End-to-end secure communication with PQC",
                parameters={
                    "message_size_kb": 256,
                    "num_messages": 1000,
                    "encryption": "hybrid"
                },
                duration_seconds=300
            ),
            "quantum_attack": SimulationScenario(
                name="quantum_attack",
                description="Simulate quantum computer attack on classical vs PQC",
                parameters={
                    "quantum_bits": 4098,
                    "target_algorithm": "RSA-2048",
                    "simulation_speed": "fast"
                },
                duration_seconds=600
            )
        }
    
    def initialize(self):
        self.log_action("Initialization", "Starting Simulation Controller initialization")
        self._setup_simulation_environment()
        return self.explain_reasoning()
    
    def _setup_simulation_environment(self):
        """Initialize simulation environment."""
        self.reasoning_log.append(
            "Setting up simulation environment for PQC demonstrations"
        )
        self.reasoning_log.append(
            "Preparing performance monitoring and metrics collection"
        )
    
    async def process(self, input_data: Dict) -> Dict:
        """Process simulation requests."""
        action = input_data.get('action', 'run')
        scenario = input_data.get('scenario', 'secure_communication')
        
        if action == 'run':
            return await self._run_simulation(scenario)
        elif action == 'analyze':
            return self._analyze_results(scenario)
        
        return {"error": f"Unsupported action: {action}"}
    
    async def _run_simulation(self, scenario_name: str) -> Dict:
        """Run a simulation scenario."""
        if scenario_name not in self.scenarios:
            return {"error": f"Unknown scenario: {scenario_name}"}
        
        scenario = self.scenarios[scenario_name]
        self.reasoning_log.append(f"Running simulation: {scenario_name}")
        
        # Initialize metrics collection
        start_time = time.time()
        metrics = []
        
        try:
            while time.time() - start_time < scenario.duration_seconds:
                # Collect metrics
                current_metrics = await self._collect_metrics(scenario)
                metrics.append(current_metrics)
                
                # Simulate processing time
                await asyncio.sleep(1)
            
            self.metrics_history.extend(metrics)
            
            return {
                "scenario": scenario_name,
                "status": "completed",
                "duration": scenario.duration_seconds,
                "metrics_collected": len(metrics),
                "summary": self._generate_summary(metrics)
            }
            
        except Exception as e:
            return {
                "scenario": scenario_name,
                "status": "failed",
                "error": str(e)
            }
    
    async def _collect_metrics(self, scenario: SimulationScenario) -> SimulationMetrics:
        """Collect performance metrics during simulation."""
        # Simulate metric collection - in real implementation, would measure actual system
        return SimulationMetrics(
            latency_ms=np.random.normal(50, 5),  # Simulate ~50ms latency
            cpu_usage=np.random.uniform(20, 40),  # Simulate 20-40% CPU usage
            memory_mb=np.random.uniform(100, 200),  # Simulate 100-200MB memory usage
            bandwidth_mbps=np.random.uniform(50, 100),  # Simulate 50-100 Mbps bandwidth
            timestamp=datetime.now().isoformat()
        )
    
    def _generate_summary(self, metrics: List[SimulationMetrics]) -> Dict:
        """Generate summary statistics from collected metrics."""
        latencies = [m.latency_ms for m in metrics]
        cpu_usages = [m.cpu_usage for m in metrics]
        memory_usages = [m.memory_mb for m in metrics]
        bandwidths = [m.bandwidth_mbps for m in metrics]
        
        return {
            "latency_ms": {
                "mean": np.mean(latencies),
                "std": np.std(latencies),
                "min": np.min(latencies),
                "max": np.max(latencies)
            },
            "cpu_usage": {
                "mean": np.mean(cpu_usages),
                "std": np.std(cpu_usages)
            },
            "memory_mb": {
                "mean": np.mean(memory_usages),
                "std": np.std(memory_usages)
            },
            "bandwidth_mbps": {
                "mean": np.mean(bandwidths),
                "std": np.std(bandwidths)
            }
        }
    
    def _analyze_results(self, scenario_name: str) -> Dict:
        """Analyze simulation results."""
        if not self.metrics_history:
            return {"error": "No metrics available for analysis"}
        
        analysis = {
            "scenario": scenario_name,
            "performance_impact": self._analyze_performance_impact(),
            "security_assessment": self._analyze_security_metrics(),
            "recommendations": self._generate_recommendations()
        }
        
        return analysis
    
    def _analyze_performance_impact(self) -> Dict:
        """Analyze performance impact of PQC implementation."""
        # Calculate performance metrics
        latencies = [m.latency_ms for m in self.metrics_history]
        
        return {
            "latency_overhead": {
                "mean_ms": np.mean(latencies),
                "percentile_95": np.percentile(latencies, 95),
                "assessment": "Acceptable" if np.mean(latencies) < 100 else "High"
            }
        }
    
    def _analyze_security_metrics(self) -> Dict:
        """Analyze security-related metrics from simulation."""
        return {
            "quantum_resistance": "Strong",
            "classical_security": "Maintained",
            "key_exchange_overhead": "Moderate"
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on simulation results."""
        recommendations = []
        
        # Analyze latency
        mean_latency = np.mean([m.latency_ms for m in self.metrics_history])
        if mean_latency > 100:
            recommendations.append(
                "Consider optimizing key exchange protocol to reduce latency"
            )
        
        # Analyze resource usage
        mean_cpu = np.mean([m.cpu_usage for m in self.metrics_history])
        if mean_cpu > 30:
            recommendations.append(
                "Implement caching strategy to reduce CPU usage during key generation"
            )
        
        return recommendations
    
    def generate_performance_graph(self) -> bytes:
        """Generate visualization of performance metrics."""
        if not self.metrics_history:
            return b""
        
        timestamps = [i for i in range(len(self.metrics_history))]
        latencies = [m.latency_ms for m in self.metrics_history]
        
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, latencies, label='Latency (ms)')
        plt.xlabel('Time (s)')
        plt.ylabel('Latency (ms)')
        plt.title('PQC Implementation Performance')
        plt.legend()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        
        return buf.getvalue()
    
    def explain_reasoning(self) -> str:
        """Provide detailed reasoning for simulation decisions."""
        reasoning = "\nSimulation Controller Reasoning:\n"
        reasoning += "\n".join(f"- {log}" for log in self.reasoning_log)
        return reasoning
