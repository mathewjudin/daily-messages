"""
Endpoints for reminders and daily messages
"""
import datetime
import os
import random
from fastapi import FastAPI
from messages import reminders
app = FastAPI()

CURR_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES_PATH = os.path.join(CURR_FILE_PATH, 'messages')
CULTURE_FILE = os.path.join(MESSAGES_PATH, 'culture.txt')
SEP20_INTERNS_FILE = os.path.join(MESSAGES_PATH, 'sep20_interns.txt')

def get_weekday():
    "Return the weekday"
    return datetime.datetime.today().weekday()

def get_messages_from_file(filename):
    "Return a list of culture related messages"
    lines = []
    with open(filename, 'r') as fp:
        lines = fp.readlines()

    return lines

@app.get("/")
def index():
    "The home page"
    return {"msg":"This is the endpoint for the home page. /message \
        and /reminder are more useful starting points."}

@app.get("/message")
def get_message():
    "Return a random message"
    lines = get_messages_from_file(CULTURE_FILE)
    message = random.choice(lines)

    return {'msg':message.strip()}

@app.get("/reminder")
def get_reminder():
    "Return a reminder based on day of the week"
    weekday = get_weekday()
    #Note: Monday is 0 and Sunday is 6
    lines = reminders.messages.get(weekday, [''])
    message = "<b>Reminder:</b> " + random.choice(lines)

    return {'msg':message.strip()}

@app.get("/sep20-interns")
def get_sep20_message():
    "Return a message for the Sep 2020 internship"
    lines = get_messages_from_file(SEP20_INTERNS_FILE)

    return {'msg': random.choice(lines).strip()}
