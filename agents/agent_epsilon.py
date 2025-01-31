from .base_agent import BaseAgent
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ComplianceRequirement:
    standard: str
    version: str
    requirements: List[str]
    implementation_status: str  # Compliant, Partially Compliant, Non-Compliant
    notes: Optional[str] = None

@dataclass
class StandardReference:
    name: str
    version: str
    publication_date: str
    url: str
    key_requirements: List[str]

class ComplianceAdvisor(BaseAgent):
    def __init__(self):
        super().__init__("agent_epsilon")
        self.standards = {}
        self.compliance_status = {}
        self.reasoning_log = []
        self._initialize_standards()
    
    def _initialize_standards(self):
        """Initialize PQC-related standards and requirements."""
        self.standards = {
            "NIST-PQC": StandardReference(
                name="NIST Post-Quantum Cryptography Standardization",
                version="Round 3",
                publication_date="2022-07-05",
                url="https://csrc.nist.gov/Projects/post-quantum-cryptography",
                key_requirements=[
                    "Use NIST-approved PQC algorithms",
                    "Implement proper key sizes and parameters",
                    "Follow NIST SP 800-208 guidelines"
                ]
            ),
            "FIPS-140-3": StandardReference(
                name="FIPS 140-3",
                version="2019",
                publication_date="2019-03-22",
                url="https://csrc.nist.gov/publications/detail/fips/140/3/final",
                key_requirements=[
                    "Use approved cryptographic algorithms",
                    "Implement proper key management",
                    "Maintain security boundaries"
                ]
            )
        }
    
    def initialize(self):
        self.log_action("Initialization", "Starting Compliance Advisor initialization")
        self._setup_compliance_framework()
        return self.explain_reasoning()
    
    def _setup_compliance_framework(self):
        """Initialize compliance tracking framework."""
        self.reasoning_log.append(
            "Setting up compliance framework for PQC implementation"
        )
        self.reasoning_log.append(
            "Loading latest NIST PQC standards and guidelines"
        )
    
    def process(self, input_data: Dict) -> Dict:
        """Process compliance check requests."""
        action = input_data.get('action', 'check')
        standard = input_data.get('standard', 'NIST-PQC')
        
        if action == 'check':
            return self._check_compliance(standard)
        elif action == 'update':
            return self._update_compliance_status(standard, input_data.get('status', {}))
        
        return {"error": f"Unsupported action: {action}"}
    
    def _check_compliance(self, standard: str) -> Dict:
        """Check compliance with specified standard."""
        if standard not in self.standards:
            return {"error": f"Unknown standard: {standard}"}
        
        std_ref = self.standards[standard]
        self.reasoning_log.append(f"Checking compliance with {standard}")
        
        requirements = []
        for req in std_ref.key_requirements:
            status = self._evaluate_requirement(standard, req)
            requirements.append({
                "requirement": req,
                "status": status.implementation_status,
                "notes": status.notes
            })
        
        return {
            "standard": standard,
            "version": std_ref.version,
            "date_checked": datetime.now().isoformat(),
            "requirements": requirements,
            "overall_status": self._calculate_overall_status(requirements)
        }
    
    def _evaluate_requirement(self, standard: str, requirement: str) -> ComplianceRequirement:
        """Evaluate compliance with a specific requirement."""
        # This is a simulation - in real implementation, would check actual system
        if "NIST-approved" in requirement:
            return ComplianceRequirement(
                standard=standard,
                version=self.standards[standard].version,
                requirements=[requirement],
                implementation_status="Compliant",
                notes="Using approved Kyber and Dilithium implementations"
            )
        elif "key management" in requirement.lower():
            return ComplianceRequirement(
                standard=standard,
                version=self.standards[standard].version,
                requirements=[requirement],
                implementation_status="Partially Compliant",
                notes="Key management procedures need enhancement for full compliance"
            )
        
        return ComplianceRequirement(
            standard=standard,
            version=self.standards[standard].version,
            requirements=[requirement],
            implementation_status="Compliant"
        )
    
    def _calculate_overall_status(self, requirements: List[Dict]) -> str:
        """Calculate overall compliance status."""
        statuses = [req["status"] for req in requirements]
        
        if all(status == "Compliant" for status in statuses):
            return "Compliant"
        elif any(status == "Non-Compliant" for status in statuses):
            return "Non-Compliant"
        else:
            return "Partially Compliant"
    
    def _update_compliance_status(self, standard: str, status: Dict) -> Dict:
        """Update compliance status for a standard."""
        if standard not in self.standards:
            return {"error": f"Unknown standard: {standard}"}
        
        self.compliance_status[standard] = status
        self.reasoning_log.append(f"Updated compliance status for {standard}")
        
        return {
            "standard": standard,
            "status": "updated",
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_compliance_report(self) -> Dict:
        """Generate comprehensive compliance report."""
        report = {
            "timestamp": datetime.now().isoformat(),
            "standards_checked": [],
            "overall_status": "Compliant",
            "recommendations": []
        }
        
        for standard in self.standards:
            compliance_check = self._check_compliance(standard)
            report["standards_checked"].append(compliance_check)
            
            if compliance_check.get("overall_status") != "Compliant":
                report["overall_status"] = "Partially Compliant"
                report["recommendations"].extend(
                    self._generate_recommendations(standard, compliance_check)
                )
        
        return report
    
    def _generate_recommendations(self, standard: str, compliance_check: Dict) -> List[str]:
        """Generate recommendations based on compliance check results."""
        recommendations = []
        for req in compliance_check["requirements"]:
            if req["status"] != "Compliant":
                recommendations.append(
                    f"[{standard}] {req['requirement']}: {req['notes']}"
                )
        return recommendations
    
    def explain_reasoning(self) -> str:
        """Provide detailed reasoning for compliance decisions."""
        reasoning = "\nCompliance Advisor Reasoning:\n"
        reasoning += "\n".join(f"- {log}" for log in self.reasoning_log)
        return reasoning
