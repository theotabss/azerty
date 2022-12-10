import json
from os import getenv
from dotenv import load_dotenv
load_dotenv("config.env") 



COMMAND_PREFIXES = dict(prefixes=json.loads(getenv("COMMAND_PREFIXES")))
prefixes=COMMAND_PREFIXES

OWNER_USERID = json.loads(getenv("OWNER_USERID"))
SUDO_USERID = OWNER_USERID #
try: SUDO_USERID += json.loads(getenv("SUDO_USERID")) 
except: pass

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

print(SUDO_USERID)
