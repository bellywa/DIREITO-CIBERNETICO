9. Código de Integração de Backend para Termos de Uso

from flask import Flask, request, jsonify

app = Flask(__name__)

terms_conditions = {
    "version": "1.1.0",
    "content": "Aqui estão os novos termos e condições de uso..."
}

@app.route('/terms', methods=['GET'])
def get_terms():
    return jsonify(terms_conditions)

@app.route('/accept_terms', methods=['POST'])
def accept_terms():
    user_id = request.json.get('user_id')
    terms_version = request.json.get('terms_version')
    # Registro do consentimento (poderia chamar ConsentManager aqui)
    return jsonify({"message": f"User {user_id} accepted terms version {terms_version}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
