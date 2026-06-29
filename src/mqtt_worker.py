import paho.mqtt.client as mqtt
from email_sender import enviar_correo_inseguro

MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "servidor/notas"

MQTT_USER = "auditor_mqtt"
MQTT_PASS = "ClaveSegura1234!"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Conectado exitosamente. Suscribiendose a: {MQTT_TOPIC}...")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Error de conexion. Codigo: {rc}")

def on_message(client, userdata, msg):
    nota_recibida = msg.payload.decode("utf-8")
    print(f"Mensaje MQTT recibido en [{msg.topic}]: '{nota_recibida}'")
    try:
        print("Reenviando nota via SMTP a Mailpit...")
        enviar_correo_inseguro(
            destinatario="pruebas_mqtt@correo.com",
            asunto="Nueva Nota Sincronizada por MQTT",
            mensaje=f"Nota recibida desde MQTT:\n\n{nota_recibida}"
        )
        print("Correo enviado con exito.")
    except Exception as e:
        print(f"Fallo el envio del correo: {e}")

if __name__ == '__main__':
    cliente = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    cliente.username_pw_set(MQTT_USER, MQTT_PASS)

    cliente.on_connect = on_connect
    cliente.on_message = on_message

    print("Conectando al Broker MQTT...")
    cliente.connect(MQTT_BROKER, MQTT_PORT, 60)
    cliente.loop_forever()

cliente = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="worker_notas",
    clean_session=True
)