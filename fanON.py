#!/usr/bin/python
# -*- coding: utf-8 -*-
import configparser
import os
import time
import requests
import json


def pushbullet(msg):
    config = configparser.ConfigParser()
    config.read('/home/pi/config.ini')
    cfg = config['default']['api_key']

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
 #   os.system('/home/pi/bin/arduino-cli compile --fqbn arduino:avr:uno /home/pi/IR_FanController/FanController_ON/FanController_ON.ino')

 #   time.sleep(1) #segundos

    os.system('/home/pi/bin/arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/IR_FanController/FanController_ON')

    pushbullet("FAN| ON ")

    print("fan on")

# arduino-cli compile --fqbn arduino:avr:uno FanController_ON.ino

# arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_ON


if __name__ == '__main__':
    main()
