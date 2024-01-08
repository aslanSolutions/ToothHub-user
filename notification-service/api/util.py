from .db import notification
from flask import current_app as app
from datetime import datetime
from flask_mail import Message
import json
from . import mail


def create_notification(data):
    """Create a notification"""
    try:
        data["created_at"] = datetime.utcnow()
        with app.app_context():
            send_email(app, data)
        result = notification.insert_one(data)
        return result
    except Exception as e:
        print(f"Error in create_notification: {e}")
        return None


def send_email(app, data):

    with app.app_context():
        appointment_datetime_str = data['appointment_datetime']
        parsed_datetime = datetime.fromisoformat(appointment_datetime_str)
        formatted_datetime = parsed_datetime.strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        try:

            msg = Message()

            if data['topic'] == 'booking/create':
                msg.subject = 'Appointment Scheduled'
                msg.recipients = [data['dentist_email'], data['patient_email']]
                msg.body = f"You have an appointment scheduled for {formatted_datetime}."
                mail.send(msg)
            elif data['topic'] == 'booking/update':
                msg.subject = 'Appointment Updated'
                msg.recipients = [data['dentist_email'], data['patient_email']]
                msg.body = f"The appointment scheduled for {formatted_datetime} was updated."
                mail.send(msg)
            elif data['topic'] == 'booking/delete':
                msg.subject = 'Appointment Cancelled'
                msg.recipients = [data['dentist_email'], data['patient_email']]
                msg.body = f"Your appointment scheduled for {formatted_datetime} was cancelled."
                mail.send(msg)
            elif data['topic'] == 'wishList':
                msg.subject = 'Available Time'
                if 'wishLists' in data and isinstance(data['wishLists'], list):
                    msg.recipients = data['wishLists']
                    formatted_datetime = "..."

                    msg.body = f"You deserved time now is available. Data: {formatted_datetime}"
                    try:
                        mail.send(msg)
                        print("Emails sent successfully")
                    except Exception as e:
                        print(f"Failed to send emails: {e}")
                else:
                    print("No valid wishlist data to send emails")
                    msg.subject = 'Notification'
                    msg.recipients = [data['patient_email']]
                    msg.body = "You have a new notification."
                    mail.send(msg)
            else:
                msg.subject = 'Notification'
                msg.recipients = [data['patient_email']]
                msg.body = "You have a new notification."
                mail.send(msg)

        except Exception as e:
            print(f"Error in sending email: {e}")
            return None
