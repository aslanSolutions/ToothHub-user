import json
from .mqtt import mqtt_client
from . import flask_app


def publishPostNot(payload):
    try:
        mqtt_client.publish("notification", json.dumps(payload))
        return
    except Exception as e:
        return json({'error': str(e)}), 500

def on_message(client, userdata, msg): # Just printing the message resived for now.
    try:
        # Deserialize the outer JSON string to an inner JSON string
        inner_json_string = json.loads(msg.payload)

        # Deserialize the inner JSON string to a Python dictionary
        middle_json_string = json.loads(inner_json_string)
        payload_dict = json.loads( middle_json_string)
        app = flask_app
        with app.app_context():
            from .mail import send_email
            send_email(payload_dict)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

mqtt_client.on_message = on_message
