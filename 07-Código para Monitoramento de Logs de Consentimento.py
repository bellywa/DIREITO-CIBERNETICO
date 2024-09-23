7. Código para Monitoramento de Logs de Consentimento

import time
import logging

logging.basicConfig(filename='consent_log.log', level=logging.INFO)

class ConsentLogger:
    def __init__(self):
        self.log_file = "consent_log.log"

    def log_consent(self, user_id, terms_version):
        log_entry = f"User {user_id} accepted version {terms_version} at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        logging.info(log_entry)
        print(log_entry)

# Exemplo de uso
logger = ConsentLogger()
logger.log_consent("user_789", "1.1.0")