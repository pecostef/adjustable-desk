from machine import Pin 
from deskmotor import DeskMotor
from pinconfig import MotorLimitPinConfig, MotorButtonsPinConfig
from state import ActiveState, MotorLimitState, MotorButtonsState
led = Pin("LED", Pin.OUT)
INACTIVE_UNTIL_SLEEP_MS = 3 * 60 * 1000 # 3 minutes

# pins config
buttons_pin_config = MotorButtonsPinConfig(btn_up_pin=16, btn_down_pin=15)
limit_switch_pin_config = MotorLimitPinConfig(limit_pin=0)
desk_motor = DeskMotor(pwm_pin=18, dir_pin=19)

# state init
limit_state = MotorLimitState(limit_switch_pin_config)
buttons_state = MotorButtonsState(buttons_pin_config)
active_state = ActiveState(INACTIVE_UNTIL_SLEEP_MS)


