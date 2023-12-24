import json
from .mqtt import mqtt_client
from . import flask_app


def publishPostNot(payload):
    try:
        mqtt_client.publish("notification", json.dumps(payload))
        return
    except Exception as e:
        return json({'error': str(e)}), 500

def on_message(client, userdata, msg):
    try:
        json_payload = json.loads(msg.payload)
        payload_dict = json.loads(json_payload)
        if payload_dict['acknowledgment'] == 'True':
            app = flask_app
            with app.app_context():
                try:
                    from .routes import create_notification
                    create_notification(payload_dict)
                except Exception as e:
                    print("Error decoding JSON:", e) 
        else:
            pass
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

mqtt_client.on_message = on_message
