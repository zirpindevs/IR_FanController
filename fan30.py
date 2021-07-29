#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import MySQLdb
import requests
import json

api_key = "o.fUycrvSsqihUVsNCgj0MWDOwIxitAKLb"


def pushbullet(cfg, msg):
    try:
        data_send = {"type": "note", "title": "FANbot", "body": msg}
        requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data=json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + cfg,
                     'Content-Type': 'application/json'})
    except (KeyboardInterrupt, SystemExit):
        raise


def main():
    os.system('arduino-cli compile --fqbn arduino:avr:uno FanController_30Min/FanController_30Min.ino')

    time.sleep(1) #segundos

    os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_30Min')

    print("fan set to 30MIN")

    pushbullet(api_key, "FAN| 30MIN ")
