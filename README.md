# Post-Quantum Cryptography (PQC) Demonstration System

## Overview
This project demonstrates a comprehensive Post-Quantum Cryptography implementation using a team of six specialized AI agents. The system showcases quantum-resistant cryptographic protocols and their real-world applications through interactive simulations and detailed analysis.

![image](https://github.com/user-attachments/assets/33f4996f-cb64-4d2f-999d-ade80fe310f2)
![image](https://github.com/user-attachments/assets/753cafd2-59a5-46b8-bab6-372d87328bdd)


## Team Composition

### Agent Alpha (Cryptography Architect)
- Designs the PQC system architecture
- Selects and validates quantum-resistant algorithms
- Coordinates cryptographic protocol integration

### Agent Beta (Implementation Engineer)
- Implements PQC algorithms in communication protocols
- Manages hybrid cryptographic systems
- Handles protocol integration (TLS, SSH)

### Agent Gamma (Quantum Threat Analyst)
- Analyzes quantum attack vectors
- Simulates quantum threats
- Develops mitigation strategies

### Agent Delta (Security Auditor)
- Conducts security analysis
- Tests for vulnerabilities
- Performs cryptographic validation

### Agent Epsilon (Compliance & Standards Advisor)
- Ensures NIST PQC standards compliance
- Monitors regulatory requirements
- Maintains documentation standards

### Agent Zeta (Simulation Controller)
- Manages real-time demonstrations
- Controls simulation scenarios
- Reports performance metrics

## Features
- Quantum-resistant Key Exchange (Kyber)
- Post-quantum Digital Signatures (Dilithium)
- Hybrid Cryptographic Implementation
- Real-time Attack Simulations
- Performance Analysis and Benchmarking
- Compliance Verification

## Requirements
- Python 3.8+
- OpenSSL 3.0+
- liboqs (Open Quantum Safe)
- pqcrypto libraries

## Installation
1. Clone the repository
2. Activate the virtual environment:
   ```
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Each agent can be activated independently or as part of the complete system:

```python
python main.py --agent alpha  # Run Cryptography Architect
python main.py --all         # Run full simulation
```

## Output after running the full simulation
![image](https://github.com/user-attachments/assets/eb7f8d3f-26e0-4fcf-9291-25464d48d825)
![image](https://github.com/user-attachments/assets/d75ff168-0c89-4d78-9b38-f7412c8ffc9e)

## Security Considerations
- This system implements NIST-approved PQC algorithms
- Hybrid cryptographic approach ensures backward compatibility
- Regular security audits and updates recommended

## License
MIT License

## Contributors
- Cryptography Architect (Agent Alpha)
- Implementation Engineer (Agent Beta)
- Quantum Threat Analyst (Agent Gamma)
- Security Auditor (Agent Delta)
- Compliance Advisor (Agent Epsilon)
- Simulation Controller (Agent Zeta)
