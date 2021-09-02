import requests
import subprocess
import time
from datetime import datetime
import os

def ret(arg):
    return subprocess.run(
        ['rhythmbox-client', '--no-start', '--print-playing-format', arg], stdout=subprocess.PIPE).stdout.decode("utf-8").replace('\n', '')

token = os.environ.get('token')
prev = ""

alt_activity = input("Enter ur status: ")

while True:
    artist = ret("%ta")
    title = ret("%tt")
    album_title = ret("%at")
    dur = ret("%td")
    elapsed = ret("%te")

    activity = title + " - " + elapsed

    if prev == elapsed:
        print("paused")

        activity = alt_activity


    payload = '{"custom_status":{"text":"' + \
        activity + \
        '","emoji_name":""}}'
    try:
        requests.patch("https://discordapp.com/api/v6/users/@me/settings", payload.encode("utf-8",),
                       headers={
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB",
            "authority": "discordapp.com",
            "authorization": token,
            "content-type": "application/json",
            "origin": "https://discordapp.com",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.9 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
        },
        )
    except Exception as e:
        print(e)
    time.sleep(3)
    prev = elapsed
