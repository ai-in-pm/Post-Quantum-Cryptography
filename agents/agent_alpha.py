from .base_agent import BaseAgent
from dataclasses import dataclass
from typing import Dict, List, Optional
import json

@dataclass
class CryptoConfig:
    kem_algorithm: str = "Kyber768"
    signature_scheme: str = "Dilithium3"
    symmetric_cipher: str = "AES-256-GCM"
    hash_function: str = "SHA3-256"

class CryptographyArchitect(BaseAgent):
    def __init__(self):
        super().__init__("agent_alpha")
        self.config = CryptoConfig()
        self.reasoning_log = []
    
    def initialize(self):
        self.log_action("Initialization", "Starting Cryptography Architect initialization")
        self._design_crypto_system()
        return self.explain_reasoning()
    
    def _design_crypto_system(self):
        """Design the post-quantum cryptographic system."""
        self.reasoning_log.append(
            "Selected Kyber768 for KEM due to its security level and performance characteristics"
        )
        self.reasoning_log.append(
            "Chose Dilithium3 for signatures as it provides a good balance of security and signature size"
        )
        self.reasoning_log.append(
            "Maintaining AES-256-GCM for symmetric encryption as it remains quantum-resistant"
        )
    
    def process(self, input_data: Dict) -> Dict:
        """Process cryptographic design decisions."""
        action = input_data.get('action', 'validate')
        
        if action == 'validate':
            return self._validate_crypto_params()
        elif action == 'update':
            return self._update_crypto_params(input_data.get('params', {}))
        
        return {"error": "Invalid action specified"}
    
    def _validate_crypto_params(self) -> Dict:
        """Validate current cryptographic parameters."""
        return {
            "kem": {
                "algorithm": self.config.kem_algorithm,
                "security_level": "AES-192 equivalent",
                "status": "NIST Round 3 Winner"
            },
            "signature": {
                "algorithm": self.config.signature_scheme,
                "security_level": "AES-192 equivalent",
                "status": "NIST Round 3 Winner"
            },
            "symmetric": {
                "algorithm": self.config.symmetric_cipher,
                "quantum_resistance": "Maintained with larger key sizes"
            }
        }
    
    def _update_crypto_params(self, params: Dict) -> Dict:
        """Update cryptographic parameters based on new requirements."""
        if 'kem_algorithm' in params:
            self.config.kem_algorithm = params['kem_algorithm']
            self.reasoning_log.append(f"Updated KEM algorithm to {params['kem_algorithm']}")
        
        return self._validate_crypto_params()
    
    def explain_reasoning(self) -> str:
        """Provide detailed reasoning for cryptographic decisions."""
        reasoning = "\nCryptography Architect Reasoning:\n"
        reasoning += "\n".join(f"- {log}" for log in self.reasoning_log)
        return reasoning
