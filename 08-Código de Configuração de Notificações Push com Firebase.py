8. Código de Configuração de Notificações Push com Firebase

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);

        // Verificar se a mensagem contém dados ou notificação
        if (remoteMessage.getNotification() != null) {
            String messageBody = remoteMessage.getNotification().getBody();
            sendNotification(messageBody);
        }
    }

    private void sendNotification(String messageBody) {
        // Código para exibir notificação push
        // Configurar notificação e exibir para o usuário
    }
}
