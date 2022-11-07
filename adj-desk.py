from time import sleep_ms
import globals
from deskmotormock import DeskMotor
from pinconfig import MotorButtonsPinConfig, LimitSwitchesPinConfig

import motorbuttons
import motorlimits


while True:
    print(str(globals.buttons_state))
    print(str(globals.limits_state))
    sleep_ms(200)
    

