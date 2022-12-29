#Github.com/8769Anurag

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24348137
API_HASH = "955715293a25a9f3d5078bb57a4a0110"
BOT_TOKEN = "5863363624:AAEclIjbanQql2q1CWbFVoA_n5Lqe-f8mgE"
SESSION = "AQA-wRo5V3t61okTYdZRlf7xAim-b2HBqjQU_FCN8uzRPAND3TSJmDkcz5xfdSTrofrwgZDaUUZ44gVAkbYJrEMmXooWZicE-LdMRrTsNUB4TPxc4ZNQ1bH8zGcl1DwOqk6ontSb4z-1Qa2Q-phQB9p0VSY2OIJYgbLUbgQD1I3COzhhA7zKXcYq1HZuavLIYRammg5PqK9zmMi9AQJcYRGgORbos_tjwFr-HPXMqLY5_b28vOXkfpjoAFVPaA1clPtEhn6r9ABcFWN1o1B5g1ERy0qNEa-rypn1ijzMzSL0LiIQzdDsY6U2lvz5w6T-MMS8tsKE_H3srWpc6igioQ7-AAAAAUZXrvsA"
FORCESUB = "testsfile_bot"
AUTH = "5475118843"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
