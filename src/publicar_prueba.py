import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "servidor/notas"
MQTT_USER = "auditor_mqtt"
MQTT_PASS = "ClaveSegura1234!"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(MQTT_USER, MQTT_PASS)

client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

time.sleep(2)

client.publish(MQTT_TOPIC, "Nota: Canal MQTT seguro.")

time.sleep(1)
client.loop_stop()
client.disconnect()
print("Mensaje enviado.")