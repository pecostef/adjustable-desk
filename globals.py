from deskmotormock import DeskMotor
from pinconfig import LimitSwitchesPinConfig, MotorButtonsPinConfig
from state import ActiveState, MotorLimitsState, MotorButtonsState
from machine import Pin 
led = Pin("LED", Pin.OUT)
INACTIVE_UNTIL_SLEEP_MS = 3 * 60 * 1000 # 3 minutes

buttons_pin_config = MotorButtonsPinConfig(14, 15)
limit_switches_pin_config = LimitSwitchesPinConfig(0, 1)
limits_state = MotorLimitsState(limit_switches_pin_config)
buttons_state = MotorButtonsState(buttons_pin_config)
active_state = ActiveState(INACTIVE_UNTIL_SLEEP_MS)

desk_motor = DeskMotor(21, 20)

