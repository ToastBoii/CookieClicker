from pypresence import Presence
from time import time
from utils import numberize
import threading

# Init
start = int(time())
client_id = "1014075598567641129"
RPC = Presence(client_id)
RPC.connect()
updateRPCtime = 30  # How often it updates the labels
Time = updateRPCtime
cookies = 0


# Functions


def updateParameters(cookie, deltaTime):
    global cookies, Time, updateRPCtime
    cookies = cookie
    Time += deltaTime

    if Time >= updateRPCtime:
        Time = 0
        updateRPC()
    print(Time)


def disconectRPC():
    RPC.close()


def updateRPC():
    RPC.update(
        large_image="icon",
        large_text="Cookie Clicker",
        details=str(numberize(cookies)) + " Cookies",
        start=start,
        buttons=[{"label": "Github", "url": "https://github.com/ToastyBoiiiii/CookieClicker"}]
    )
