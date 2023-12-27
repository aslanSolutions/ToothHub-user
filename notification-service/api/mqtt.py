import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client(client_id="notification-service",
                          clean_session=True, protocol=mqtt.MQTTv311)
mqtt_client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code " + str(rc))
        mqtt_client.subscribe("booking/delete")
        mqtt_client.subscribe("booking/update")
        mqtt_client.subscribe("booking/confirm")
        client.subscribe("whishList")
    else:
        print("Connection failed with code " + str(rc))


mqtt_client.on_connect = on_connect
mqtt_client.username_pw_set("group7", "Group777")
