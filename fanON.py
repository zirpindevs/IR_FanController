#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

os.system('/home/pi/bin/arduino-cli compile --fqbn arduino:avr:uno /home/pi/IR_FanController/FanController_ON/FanController_ON.ino')
time.sleep(1) #segundos

os.system('/home/pi/bin/arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno /home/pi/IR_FanController/FanController_ON')

print("fan off")

# arduino-cli compile --fqbn arduino:avr:uno FanController_ON.ino

# arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_ON