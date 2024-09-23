2. Código para Envio de Notificações Automáticas

import smtplib
from email.mime.text import MIMEText

class NotificationSystem:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        self.server = smtplib.SMTP(smtp_server, smtp_port)
        self.server.starttls()
        self.server.login(smtp_user, smtp_password)

    def send_notification(self, recipient_email, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = "noreply@reidopitaco.com"
        msg['To'] = recipient_email

        self.server.sendmail("noreply@reidopitaco.com", recipient_email, msg.as_string())

    def close_connection(self):
        self.server.quit()

# Exemplo de uso
notification_system = NotificationSystem("smtp.gmail.com", 587, "your_email@gmail.com", "your_password")
notification_system.send_notification("usuario@exemplo.com", "Atualização dos Termos de Uso",
                                      "Os termos de uso foram atualizados para a versão 1.1.0. Por favor, revise e aceite.")
notification_system.close_connection()