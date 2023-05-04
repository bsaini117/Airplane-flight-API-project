from twilio.rest import Client
import requests
import smtplib

ACT_SID = "ACc29cfb9acc94e19b7d7196775d863aba"
AUTH_TOKEN = "403ab48cbc17de3f3a1385f1bad7e135"
SHEETY_ENDPOINT = "https://api.sheety.co/a5b9f38df3cc01445d54b5e990cb5e1d/flightDealsProgram/users"

MY_EMAIL = "bhavesh.sainitestact@gmail.com"
MY_PASSWORD = "lbclywructzplhva"


class NotificationManager:

    def __init__(self):
        self.client = Client(ACT_SID, AUTH_TOKEN)

    def send_sms(self, text):

        message = self.client.messages.create(
              body=text,
              from_="+17262042176",
              to="+12406189060"
            )
        print(message.sid)

    def send_email(self, customer_email, message, link):

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=customer_email,
                                msg=f"{message}\n{link}")



