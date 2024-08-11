import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_AUTH_TOKEN'])

    def send_sms(self, msg):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_ALLOTTED_NUMBER"],
            body=msg,
            to=os.environ["TWILIO_PERSONAL_NUMBER"]
        )

        print(message.sid)
