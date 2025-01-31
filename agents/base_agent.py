from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv

class BaseAgent(ABC):
    def __init__(self, agent_name: str):
        self.agent_name = agent_name
        self._load_api_key()
        
    def _load_api_key(self):
        """Load API key from environment variables."""
        load_dotenv()
        api_key_name = f"{self.agent_name.upper()}_API_KEY"
        self.api_key = os.getenv(api_key_name)
        if not self.api_key:
            raise ValueError(f"API key for {self.agent_name} not found in environment variables")
    
    @abstractmethod
    def initialize(self):
        """Initialize agent-specific components."""
        pass
    
    @abstractmethod
    def process(self, input_data: dict) -> dict:
        """Process input data and return results."""
        pass
    
    @abstractmethod
    def explain_reasoning(self) -> str:
        """Provide Chain of Thought reasoning for decisions."""
        pass
    
    def log_action(self, action: str, details: str):
        """Log agent actions with timestamps."""
        print(f"[{self.agent_name}] {action}: {details}")
