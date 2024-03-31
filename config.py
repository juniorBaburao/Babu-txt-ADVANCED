import os

API_ID = API_ID = 22435461

API_HASH = os.environ.get("API_HASH", "fe62b0736218400bf1209d831b6af1a7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "> Wow Tapatap:
7166121629:AAHLN3Xe548E7BcpmIcn4oqAHmJbWKHM30o
")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5651162572))

LOG = -1002090024849

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1459497376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


