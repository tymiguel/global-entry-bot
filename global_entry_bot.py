import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv("ACCOUNT_SID")

# Your Auth Token from twilio.com/console
auth_token  = os.getenv("AUTH_TOKEN") 

# to/from numbers
from_number = os.getenv("FROM_NUMBER")
to_number1 = os.getenv("NUMBER1")
to_number2 = os.getenv("NUMBER2")

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=to_number1, 
    from_=from_number,
    body="Hello from Python!")

message = client.messages.create(
    to=to_number2, 
    from_=from_number,
    body="Hello from Python!")