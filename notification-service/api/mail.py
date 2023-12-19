import json
from flask_mail import Mail
from flask_mail import Message
from flask import current_app as app

with app.app_context():
    # Configure the mail settings
    app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'mohamdaslan5@hotmail.com'
    app.config['MAIL_PASSWORD'] = 'ammaraslan55'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = 'mohamdaslan5@hotmail.com'
    app.config['MAIL_DEBUG'] = True

    # Create the Mail object within the application context
    mailObj = Mail(app)


def send_email(data):
    with app.app_context():
        try:
            if data['topic'] == 'booking/create':
                pass
            elif data['topic'] == 'booking/update':
                pass
            elif data['topic'] == 'booking/delete':
                pass
            else:
                print("The data got to send_email(): ", data)
                msg = Message(subject=data['subject'], recipients=[data['receiver'][0], data['receiver'][1]])
                msg.body = data['description']
                mailObj.send(msg)
                print("Message sent!")
                return "Message sent!"
        except Exception as e:
                print("Error sending emails: ", e)
                return f"Error sending emails: {str(e)}"
