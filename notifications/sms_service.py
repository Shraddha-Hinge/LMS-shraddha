from twilio.rest import Client
from django.conf import settings

def send_sms_notification(user, message):
    if user.notification_preferences.receive_sms:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=user.phone_number
        )
print("Twilio is working!")