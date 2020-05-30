# Global Entry Bot

The project contains code to access the Trusted Travel Program website [https://ttp.dhs.gov/] to notify you when an interview spot opens up at your local interview location.

The is NOT affliated with the United Stated Government or any of it's departments.

# References

I saw a few references out on the web that I used to build this. Shout out to the folks below for doing some of the early work to stand up these projects.

- [Global Entry Interview Openings Checker](https://github.com/mvexel/next_global_entry)
- [Real World APIs: Snagging a Global Entry Interview](https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/)

# Production

## 1. Sign up for Twillo
Create a free account on [Twilio](https://www.twilio.com/). 

Twilio is a platform that will allow us to create a phone number that we can use to send SMS messages to our personal cell phone through Twilio's REST API. We will use this platform to alert us when a new global entry slot has opened up.

After createing an account, go through the process of creating a trail number on their website. They will give you credits that you can use to get started. Generally, this should be enough, but if you need more credits, a few dollars will go along way.

Additionally, add the phone number that will be recieving the messages to the Verified Caller IDs list on your Twilio account. You will have to confirm that the number is allowed to recieve messages.

## 2. Set up credentials
In the root directory of the project `global-entry-bot/`, create a `.env` file. This will store your Twillio credentials and the phone number you want to send the bot messages to.

The file should contain `FROM_NUMBER`, `TO_NUMBER`, 'ACCOUNT_SID`, and `AUTH_TOKEN`. See below for an example of the `.env` file structure.

```
FROM_NUMBER=<twilio phone number>
TO_NUMBER=<recieving phone>

ACCOUNT_SID=<twilio account id>
AUTH_TOKEN=<twilio auth token>
```

Note: Be sure to include the country code in your phone number. For example, the U.S. is "+1".

## 3. Update search parameters

Go into the `global_entry_bot.py` file and replace the `city` variable with the city you want to search and the `date_limit` variable with the maximum date that you want to search out in advance.

The city you put in the slot must be the exact global entry location. This can be found on their website. For example, in Massachusetts, "East Boston" is the city location for the global entry offices at Boston's Logan Airport.

What I have done in the past is actually go onto the global entry site and book a date for an interview. Then, I use that date as my maximum date to search for with the thought that I will rebook any interview slot that is earlier than my current one.

## 4. Run it once to test

Once you have done that we can finally test it out!

Open your terminal and `cd` into your global-entry-bot directoy and run the program from the shell using:

```
$ python -m global_entry_bot
```

You should see a response within seconds.

## 5. Run automatically 24/7

This is great to run once, but we didn't create this to keep doing manually every few seconds. To have this run automatically, you need to create a cron job [see example](https://phoenixnap.com/kb/set-up-cron-job-linux) or something like that. You have a few options on where to run this job, but ultimately, it's up to you on how comfortable you feel and what makes the most sense to you.

More robust version: 
- Find a remote computer that is always on, such as an AWS EC2 instance, and set up the oode and cron job on that computer. 

Simple verison:
- Use your computer, keep it on it's charger and don't let it go to sleep. Then, you can run the cron job on your computer.

Regardless of what you decide to do, I recommend creating a `logs/` directory in the root `global-entry-bot` directory so that you can capture all the logs from the cron job. If there are errors, you will notice immediately.

I set mine up to run every 10 minutes, but you can adjust this to what you think is most appropriate.
