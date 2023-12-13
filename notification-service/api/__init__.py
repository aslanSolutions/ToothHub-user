from flask import Flask
from apifairy import APIFairy
from .mqtt import mqtt_client



brokerAdress = "0169ad6feac84c25b5b11b5157be1bd8.s2.eu.hivemq.cloud"
brokerPort = 8883
flask_app = None
def create_app():
    global flask_app
    apifairy = APIFairy()
    app = Flask(__name__)
    flask_app = app
    app.config['APIFAIRY_TITLE'] = 'Notification API'
    app.config['APIFAIRY_VERSION'] = '1.0'
    # Initialize APIFairy, Marshmallow, and Mail
    from .marsh_schema import ma
    apifairy.init_app(app)
    ma.init_app(app)
    

    # Register the notification blueprint
    from .routes import bp as notification_bp
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
