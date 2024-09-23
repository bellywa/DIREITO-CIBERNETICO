5. Código para Auditar Registros de Consentimento

import json

class AuditManager:
    def __init__(self, file_path="consent_records.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as file:
                self.consent_records = json.load(file)
        except FileNotFoundError:
            self.consent_records = {}

    def audit_consent_records(self):
        for user_id, record in self.consent_records.items():
            print(f"User ID: {user_id}")
            print(f"Accepted Terms Version: {record['terms_version']}")
            print(f"Consent Date: {record['consent_date']}")
            print("-" * 30)

# Exemplo de uso
audit_manager = AuditManager()
audit_manager.audit_consent_records()
