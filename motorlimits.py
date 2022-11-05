from machine import Pin
import machine
from deskmotormock import DeskMotor
from pinconfig import LimitSwitchesPinConfig
from state import MotorLimitsState, ActiveState

class MotorLimits:
    def __init__(self, pin_config: LimitSwitchesPinConfig, desk_motor: DeskMotor, active_state: ActiveState) -> None:
        self._desk_motor = desk_motor
        self._pin_config = pin_config
        self._limits_state = MotorLimitsState(pin_config)
        self._active_state = active_state
        self._pin_config.limit_up_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._limit_upper_INT)
        self._pin_config.limit_low_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._limit_lower_INT)

    def _limit_lower_INT(self, pin):
        self._pin_config.limit_low_pin.irq(handler=None)

        limit_lower_state = self._limits_state.limit_low_state
        self._active_state.extend_active_state()

        if(self._pin_config.limit_low_pin.value() == 1 and limit_lower_state == 0):
            # lower limit switch from low => high
            self._limits_state.limit_low_state = 1
            self._desk_motor.stop()
        elif(self._pin_config.limit_low_pin.value() == 0 and limit_lower_state == 1):
            # lower limit switch from high => low
            self._limits_state.limit_low_state = 0
        self._pin_config.limit_low_pin.irq(handler=self._limit_lower_INT)

    def _limit_upper_INT(self, pin):
        self._pin_config.limit_up_pin.irq(handler=None)
        
        limit_upper_state = self._limits_state.limit_up_state
        self._active_state.extend_active_state()

        if(self._pin_config.limit_up_pin.value() == 1 and limit_upper_state == 0):
            # upper limit switch from low => high
            self._limits_state.limit_up_state = 1
            self._desk_motor.stop()
        elif(self._pin_config.limit_up_pin.value() == 0 and limit_upper_state == 1):
            # upper limit switch from high => low
            self._limits_state.limit_up_state = 0

        self._pin_config.limit_up_pin.irq(handler=self._limit_upper_INT)
    
    @property
    def limits_state(self) -> MotorLimitsState:
        return self._limits_state

    def __str__(self) -> str:
        return f'MotorLimits( limit_up_state={self._limits_state.limit_up_state}, limit_low_state={self._limits_state.limit_low_state})'
