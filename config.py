import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Agent API Keys
    AGENT_ALPHA_API_KEY = os.getenv('AGENT_ALPHA_API_KEY')
    AGENT_BETA_API_KEY = os.getenv('AGENT_BETA_API_KEY')
    AGENT_GAMMA_API_KEY = os.getenv('AGENT_GAMMA_API_KEY')
    AGENT_DELTA_API_KEY = os.getenv('AGENT_DELTA_API_KEY')
    AGENT_EPSILON_API_KEY = os.getenv('AGENT_EPSILON_API_KEY')
    AGENT_ZETA_API_KEY = os.getenv('AGENT_ZETA_API_KEY')

    # Cryptographic Parameters
    DEFAULT_KEM_ALGORITHM = "Kyber768"
    DEFAULT_SIGNATURE_SCHEME = "Dilithium3"
    DEFAULT_SYMMETRIC_CIPHER = "AES-256-GCM"
    DEFAULT_HASH_FUNCTION = "SHA3-256"

    # Performance Settings
    BENCHMARK_ITERATIONS = 1000
    SIMULATION_DURATION = 300  # seconds

    # Security Parameters
    MIN_KEY_SIZE = 256
    QUANTUM_SECURITY_LEVEL = 5  # Level 5 security (highest)

    @staticmethod
    def validate_environment():
        """Validate that all required environment variables are set."""
        required_vars = [
            'AGENT_ALPHA_API_KEY',
            'AGENT_BETA_API_KEY',
            'AGENT_GAMMA_API_KEY',
            'AGENT_DELTA_API_KEY',
            'AGENT_EPSILON_API_KEY',
            'AGENT_ZETA_API_KEY'
        ]
        
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
