import configparser
import os
import time
import MySQLdb
import requests
import json


# Function insert luz and vent , alarma and calentador status to table
def set_status_fan(status):
    config = configparser.ConfigParser()
    config.read('/home/pi/config.ini')

    host = config['default']['host']
    username = config['default']['username']
    password = config['default']['password']
    db_fan = config['default']['db_fan']

    # connect to db
    db = MySQLdb.connect(host, username, password, db_fan)
    # setup cursor
    cursor = db.cursor()
    try:
        cursor.execute(
            """INSERT INTO status_fan (estado) VALUES (%s)""",
            status)
        db.commit()
        print("insert OK")
    except:
        db.rollback()
        print("error inserting status gpio")


def pushbullet(msg):
    try:
        config = configparser.ConfigParser()
        config.read('/home/pi/config.ini')
        cfg = config['default']['api_key']

        data_send = {"type": "note", "title": "FANbot", "body": msg}
        requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data=json.dumps(data_send),
            headers={'Authorization': 'Bearer ' + cfg,
                     'Content-Type': 'application/json'})
    except (KeyboardInterrupt, SystemExit):
        raise


def main():
    #os.system('/home/pi/bin/arduino-cli compile --fqbn arduino:avr:uno /home/pi/IR_FanController/FanController_OFF/FanController_OFF.ino')

    #time.sleep(1)  # segundos

    os.system('/home/pi/bin/arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/IR_FanController/FanController_OFF')

    print("fan off")

    pushbullet("FAN| OFF ")

    set_status_fan("APAGADO")


# arduino-cli compile --fqbn arduino:avr:uno FanController_OFF.ino

# arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_OFF


if __name__ == '__main__':
    main()
