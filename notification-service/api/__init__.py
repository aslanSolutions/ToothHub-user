from flask import Flask
from apifairy import APIFairy
from flask_marshmallow import Marshmallow
from .routes import bp as notification_bp
from .mqtt import mqtt_client
from .marsh_schema import ma

brokerAdress = "0169ad6feac84c25b5b11b5157be1bd8.s2.eu.hivemq.cloud"
brokerPort = 8883

def create_app():
    apifairy = APIFairy()
    app = Flask(__name__)
    app.config['APIFAIRY_TITLE'] = 'Notification API'
    app.config['APIFAIRY_VERSION'] = '1.0'

    # Initialize APIFairy, Marshmallow
    apifairy.init_app(app)
    ma.init_app(app)

    # Register the notification blueprint
    app.register_blueprint(notification_bp)

    # Set the MQTT broker address and port
    app.config['MQTT_BROKER_ADDRESS'] = brokerAdress
    app.config['MQTT_PORT'] = brokerPort

    # Add the MQTT client to the app context
    app.mqtt_client = mqtt_client

    # Start the MQTT client loop in a separate thread
    # Connecting the MQTT client
    mqtt_client.connect(app.config['MQTT_BROKER_ADDRESS'], app.config['MQTT_PORT'])
    mqtt_client.loop_start()

    return app
