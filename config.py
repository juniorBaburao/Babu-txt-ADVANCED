import os

API_ID = API_ID = 22435461

API_HASH = os.environ.get("API_HASH", "fe62b0736218400bf1209d831b6af1a7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "> Wow Tapatap:
6995524576:AAEVCEcEbEvdk1eGoZ46FyrEH9rCyTCxCjU
")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5651162572))

LOG = -1002090024849

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


