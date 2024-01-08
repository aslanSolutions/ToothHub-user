from flask import Flask
from apifairy import APIFairy
from .mqtt import mqtt_client
from flask_mail import Mail
from .marsh_schema import ma
from .config import get_config

flask_app = None
mail = Mail()

def create_app():
    global flask_app
    apifairy = APIFairy()
    app = Flask(__name__)
    flask_app = app

    # Load configurations from the dynamically selected class
    app.config.from_object(get_config())

    # Initialize APIFairy, Marshmallow, and Mail
    apifairy.init_app(app)
    ma.init_app(app)

    # Register the notification blueprint
    from .routes import bp as notification_bp
    app.register_blueprint(notification_bp)

    # Add the MQTT client to the app context
    app.mqtt_client = mqtt_client

    # Start the MQTT client loop in a separate thread
    # Connecting the MQTT client
    mqtt_client.connect(app.config['MQTT_BROKER_ADDRESS'], app.config['MQTT_PORT'])
    mqtt_client.loop_start()

    # Initialize Flask-Mail with the app
    mail.init_app(app)

    return app
