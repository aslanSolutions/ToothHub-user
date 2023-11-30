import json
from .mqtt import mqtt_client

def publishPostNot(payload):
    try:
        mqtt_client.publish(payload.sender, json.dumps(payload))
        return json({'Request send successfully': str(e)}), 201
    except Exception as e:
        return json({'error': str(e)}), 500


def on_message(client, userdata, msg): # Just printing the message resived for now.
    try:
        print("Message resived: ", msg.topic ,", ",msg.payload.decode("utf-8"))
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

mqtt_client.on_message = on_message
