from datetime import datetime
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
        # Format the datetime object
        appointment_datetime_str = data['appointment_datetime']
        parsed_datetime = datetime.fromisoformat(appointment_datetime_str)
        formatted_datetime = parsed_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')
        
        try:
            if data['topic'] == 'create/booking':
                try:
                    json_body = {"message": f"You have an appointment scheduled for you on {formatted_datetime}. Appointment ID: {data['correlation_id']}"}
                    msg = Message(subject='Appointment scheduled', recipients=[data['dentist_email'], data['patient_email']])
                    msg.body = json.dumps(json_body['message'])
                    mailObj.send(msg)
                    return "Message sent!"
                except Exception as e:
                    return json({'error': str(e)})
            elif data['topic'] == 'update/booking':
                try:
                    json_body = {"message": f"The appointment scheduled for you was updated to be on {formatted_datetime}. Appointment ID: {data['correlation_id']}"}
                    msg = Message(subject='Appointment scheduled updated', recipients=[data['dentist_email'], data['patient_email']])
                    msg.body = json.dumps(json_body['message'])
                    mailObj.send(msg)
                    return "Message sent!"
                except Exception as e:
                    return json({'error': str(e)})
            elif data['topic'] == 'delete/booking':
                try:
                    json_body = {"message": f"Your appointment scheduled for you on {formatted_datetime} was deleted. Appointment ID: {data['correlation_id']}"}
                    msg = Message(subject='Appointment scheduled deleted', recipients=[data['dentist_email'], data['patient_email']])
                    msg.body = json.dumps(json_body['message'])
                    mailObj.send(msg)
                    return "Message sent!"
                except Exception as e:
                    return json({'error': str(e)})
            else:
                try:
                    json_body = {"message": f"You have an appointment scheduled for you on {formatted_datetime}. Appointment ID: {data['correlation_id']}"}
                    msg = Message(subject='Appointment scheduled', recipients=[data['dentist_email'], data['patient_email']])
                    msg.body = json.dumps(json_body['message'])
                    mailObj.send(msg)
                    return "Message sent!"
                except Exception as e:
                    return json({'error': str(e)})
        except Exception as e:
                return json({'error': str(e)})
