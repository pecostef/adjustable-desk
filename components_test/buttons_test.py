from machine import Pin, deepsleep
from utime import sleep_ms
from deskmotormock import DeskMotor
from pinconfig import MotorButtonsPinConfig, LimitSwitchesPinConfig
from motorbuttons import MotorButtons
from motorlimits import MotorLimits
from state import ActiveState

import micropython
micropython.alloc_emergency_exception_buf(100)

led = Pin("LED", Pin.OUT)
INACTIVE_UNTIL_SLEEP_MS = 3 * 60 * 1000 # 3 minutes

buttons_pin_config = MotorButtonsPinConfig(14, 15)
limit_switches_pin_config = LimitSwitchesPinConfig(0, 1)

desk_motor = DeskMotor(21, 20)

active_state = ActiveState(INACTIVE_UNTIL_SLEEP_MS)
motor_limits = MotorLimits(limit_switches_pin_config, desk_motor, active_state)
motor_buttons = MotorButtons(buttons_pin_config, desk_motor, motor_limits.limits_state, active_state)

while True:
    print(str(motor_buttons))
    print(str(motor_limits))

    if(not active_state.is_active()):
        print('deepsleep() awake from Pins is not implemented :(')
    else:
        sleep_ms(500)
    


