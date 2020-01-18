import os
import sys
import datetime
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# load environment variables from the .env file
load_dotenv()

# Account SID and Auth Token from twilio.com/console
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

# to/from numbers
from_number = os.getenv("FROM_NUMBER")
to_number = os.getenv("TO_NUMBER")

# search parameters
city = "East Boston"  # city where you want to have your interview
date_limit  = '2020-10-01' # max date to search for i.e. if you already have an interview but want an earlier one
location_id = -1 # id of the city

def get_location_id(city):
    location_id = -1
    LOCATIONS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations?limit=1000"

    locations = requests.get(LOCATIONS_URL).json()
    for loc in locations:
        if loc['city'] == city:
            location_id = loc['id']

    return location_id

def check_appointments(city, location_id, date_limit):
    APPOINTMENTS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=2&asLocations={}&minimum=1"
    url = APPOINTMENTS_URL.format(location_id)
    appointments = requests.get(url).json()
    result = {'appointment': False, 'city': city, 'time': None}
    if appointments:
        if appointments[0]['startTimestamp'][:10] < date_limit:
            result['appointment'] = True
            result['time'] = appointments[0]['startTimestamp']
        else:
            result['appointment'] = False

    return result

def send_text(account_sid, auth_token, to_number, from_number, message_params):
    """Send text message from twilio account a one-line log message."""
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body="Global Entry interview opportunity in {} at {} opened up just now!".format(message_params['city'], message_params['time'])
    )

    return

def log(text):
    """Write a one-line log message."""
    print("{dt}\t{msg}".format(
        dt=datetime.datetime.now(),
        msg=text))

    return

def main():
    location_id = get_location_id(city)
    result = check_appointments(city, location_id, date_limit)

    if result['appointment']:
        send_text(account_sid, auth_token, to_number, from_number, result)
        log("text message sent")
        sys.exit(0)
    else:
        log("{}: No appointments available".format(city))
        sys.exit(1)

if __name__ == '__main__':
    main()