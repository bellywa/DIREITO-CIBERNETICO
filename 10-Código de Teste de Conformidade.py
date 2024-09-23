10. Código de Teste de Conformidade

import unittest

class TestTermsConditions(unittest.TestCase):
    def test_update_terms(self):
        manager = TermsConditionsManager()
        manager.update_terms("1.2.0", "Atualização com novos requisitos de conformidade.")
        self.assertEqual(manager.get_current_version(), "1.2.0")
        self.assertIn("1.2.0", [log["version"] for log in manager.get_update_log()])

    def test_record_consent(self):
        consent_manager = ConsentManager()
        consent_manager.record_consent("user_123", "1.2.0")
        record = consent_manager.get_consent_record("user_123")
        self.assertIsNotNone(record)
        self.assertEqual(record["terms_version"], "1.2.0")

if __name__ == '__main__':
    unittest.main()
