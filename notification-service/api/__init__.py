from flask import Flask
from apifairy import APIFairy
from .mqtt import mqtt_client
from flask_mail import Mail
from flask_mail import Message



brokerAdress = "0169ad6feac84c25b5b11b5157be1bd8.s2.eu.hivemq.cloud"
brokerPort = 8883

def create_app():
    apifairy = APIFairy()
    app = Flask(__name__)
    app.config['APIFAIRY_TITLE'] = 'Notification API'
    app.config['APIFAIRY_VERSION'] = '1.0'
    # Initialize APIFairy, Marshmallow, and Mail
    from .marsh_schema import ma
    apifairy.init_app(app)
    ma.init_app(app)
    
    # Configure the mail settings
    app.config['MAIL_SERVER']='smtp-mail.outlook.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'mohamdaslan5@hotmail.com'
    app.config['MAIL_PASSWORD'] = 'ammaraslan55'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = 'mohamdaslan5@hotmail.com'
    app.config['MAIL_DEBUG'] = True

    mailObj = Mail(app)
    # Register the notification blueprint
    from .routes import bp as notification_bp
    app.register_blueprint(notification_bp)

    @app.route('/notifications/send_email', methods=['POST'])
    def send_email():
        msg = Message(subject='Hello from the other side!', recipients=['nevraskanjo@gmail.com','guskanjona@student.gu.se'])
        msg.body = "Hey, sending you this email from my Flask app, wanna netflix and chill"
        mailObj.send(msg)
        return "Message sent!"

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
