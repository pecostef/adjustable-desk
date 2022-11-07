from machine import Pin 
from deskmotor import DeskMotor
from pinconfig import LimitSwitchesPinConfig, MotorButtonsPinConfig
from state import ActiveState, MotorLimitsState, MotorButtonsState
led = Pin("LED", Pin.OUT)
INACTIVE_UNTIL_SLEEP_MS = 3 * 60 * 1000 # 3 minutes

buttons_pin_config = MotorButtonsPinConfig(btn_up_pin=14, btn_down_pin=15)
limit_switches_pin_config = LimitSwitchesPinConfig(limit_up_pin=0, limit_low_pin=1)
limits_state = MotorLimitsState(limit_switches_pin_config)
buttons_state = MotorButtonsState(buttons_pin_config)
active_state = ActiveState(INACTIVE_UNTIL_SLEEP_MS)

desk_motor = DeskMotor(pwm_pin=16, dir_pin=17)

