from .db import notification
from flask import current_app as app
from datetime import datetime
from flask_mail import Message
import json
from . import mail


def create_notification(data):
    """Create a notification"""
    print("Topic: ", data['topic'])
    try:
        data["created_at"] = datetime.utcnow()
        print("Step 3")
        with app.app_context():
            send_email(app, data)
        result = notification.insert_one(data)
        return result
    except Exception as e:
        print(f"Error in create_notification: {e}")
        return None


def send_email(app, data):

    with app.app_context():
        # Format the datetime object
        appointment_datetime_str = data['appointment_datetime']
        parsed_datetime = datetime.fromisoformat(appointment_datetime_str)
        formatted_datetime = parsed_datetime.strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        try:

            # Create a message object
            msg = Message()

            # Set the subject, recipients, and body of the email based on the data
            if data['topic'] == 'booking/confirm':
                msg.subject = 'Appointment Scheduled'
                msg.recipients = [data['dentist_email'], data['patient_email']]
                msg.body = f"You have an appointment scheduled for {formatted_datetime}. Appointment ID: {data['correlation_id']}"
                mail.send(msg)
            elif data['topic'] == 'booking/update':
                msg.subject = 'Appointment Updated'
                msg.recipients = [data['dentist_email'], data['patient_email']]
                msg.body = f"The appointment scheduled for {formatted_datetime} was updated. Appointment ID: {data['correlation_id']}"
                mail.send(msg)
            elif data['topic'] == 'booking/delete':
                msg.subject = 'Appointment Cancelled'
                msg.recipients = [data['dentist_email'], data['patient_email']]
                msg.body = f"Your appointment scheduled for {formatted_datetime} was cancelled. Appointment ID: {data['correlation_id']}"
                mail.send(msg)
            else:
                # Handle other cases or set a default case
                msg.subject = 'Notification'
                msg.recipients = [data['patient_email']]
                msg.body = "You have a new notification."
                mail.send(msg)

        except Exception as e:
            print(f"Error in sending email: {e}")
            return None
