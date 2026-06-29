from flask import Flask, jsonify
from email_sender import enviar_correo_inseguro

app = Flask(__name__)

@app.route('/enviar-alerta', methods=['POST'])
def enviar_alerta():
    try:
        enviar_correo_inseguro(
            destinatario="prueba@correo.com",
            asunto="Alerta",
            mensaje="Pruebas de seguridad."
        )
        return jsonify({"status": "success", "message": "Correo enviado al SMTP local"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=False)