import os
import time

#os.system('arduino-cli compile --fqbn arduino:avr:uno FanController_OFF/FanController_OFF.ino')
#time.sleep(1) #segundos

os.system('arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_OFF')


# arduino-cli compile --fqbn arduino:avr:uno FanController_OFF.ino

# arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno FanController_OFF
