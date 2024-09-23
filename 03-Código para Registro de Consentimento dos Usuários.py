3. Código para Registro de Consentimento dos Usuários
import json
from datetime import datetime

class ConsentManager:
    def __init__(self, file_path="consent_records.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as file:
                self.consent_records = json.load(file)
        except FileNotFoundError:
            self.consent_records = {}

    def record_consent(self, user_id, terms_version):
        consent_record = {
            "user_id": user_id,
            "terms_version": terms_version,
            "consent_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.consent_records[user_id] = consent_record
        self._save_to_file()

    def get_consent_record(self, user_id):
        return self.consent_records.get(user_id, None)

    def _save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.consent_records, file, indent=4)

# Exemplo de uso
consent_manager = ConsentManager()
consent_manager.record_consent("user_123", "1.1.0")
print(consent_manager.get_consent_record("user_123"))
