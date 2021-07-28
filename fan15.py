#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time

os.system('arduino-cli compile --fqbn arduino:avr:uno FanController_15Min/FanController_15Min.ino')

time.sleep(1) #segundos

os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_15Min')