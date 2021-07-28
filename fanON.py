#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from datetime import time

os.system('arduino-cli compile --fqbn arduino:avr:uno FanController_ON.ino')

time.sleep(2) #segundos

os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_ON')


# arduino-cli compile --fqbn arduino:avr:uno FanController_ON.ino

# arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_ON