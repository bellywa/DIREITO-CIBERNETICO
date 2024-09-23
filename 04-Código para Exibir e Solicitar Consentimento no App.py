4. Código para Exibir e Solicitar Consentimento no App
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.TextView;
import android.widget.Button;
import android.view.View;

public class TermsActivity extends AppCompatActivity {

    private TextView termsTextView;
    private Button acceptButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_terms);

        termsTextView = findViewById(R.id.termsTextView);
        acceptButton = findViewById(R.id.acceptButton);

        // Exibir os termos e condições atualizados
        String termsText = "Versão 1.1.0: Aqui estão os novos termos e condições de uso...";
        termsTextView.setText(termsText);

        // Registrar o consentimento quando o usuário aceita
        acceptButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Código para registrar o consentimento
                recordConsent("user_123", "1.1.0");
                // Redirecionar o usuário para a tela principal
                finish();
            }
        });
    }

    private void recordConsent(String userId, String termsVersion) {
        // Código para registrar consentimento, pode ser integração com ConsentManager em backend
        // Exemplo simples:
        System.out.println("Usuário " + userId + " aceitou os termos da versão " + termsVersion);
    }
}
