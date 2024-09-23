6. Código para Simulação de Testes de Usabilidade
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.Toast;

public class UsabilityTestActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usability_test);

        // Simular um teste de usabilidade onde o usuário tenta aceitar os termos
        performUsabilityTest("user_456");
    }

    private void performUsabilityTest(String userId) {
        boolean success = true; // Sucesso na aceitação dos termos

        if (success) {
            Toast.makeText(this, "Usuário " + userId + " aceitou os termos com sucesso.", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Usuário " + userId + " encontrou problemas ao aceitar os termos.", Toast.LENGTH_SHORT).show();
        }
    }
}