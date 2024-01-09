import json
from .mqtt import mqtt_client
from . import flask_app
from .util import create_notification


def publishPostNot(payload):
    try:
        mqtt_client.publish("notification", json.dumps(payload))
        return
    except Exception as e:
        return json({'error': str(e)}), 500


def on_message(client, userdata, msg):
    with flask_app.app_context():
        try:
            decoded_payload = msg.payload.decode("utf-8")

            # First parse: Should give you a string if double-encoded
            intermediate_payload = json.loads(decoded_payload)

            # Second parse: Only if intermediate_payload is a string
            if isinstance(intermediate_payload, str):
                json_payload = json.loads(intermediate_payload)
            else:
                json_payload = intermediate_payload

            if isinstance(json_payload, dict):
                acknowledgment = json_payload.get('acknowledgment', False)

            if acknowledgment:
                try:
                    create_notification(json_payload)
                except Exception as e:
                    print("Error in create_notification:", e)
            else:
                print("Acknowledgment is not True.")
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)


mqtt_client.on_message = on_message
