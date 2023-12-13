import paho.mqtt.client as mqtt
from flask_socketio import SocketIO

mqtt_client = mqtt.Client(client_id="patient_noti", protocol=mqtt.MQTTv311)
mqtt_client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
socketio = SocketIO()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code " + str(rc))
        client.subscribe("notification")
    else:
        print("Connection failed with code " + str(rc))


mqtt_client.on_connect = on_connect
mqtt_client.username_pw_set("group7", "Group777")