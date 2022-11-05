from machine import Pin
import machine
from state import MotorButtonsState, MotorLimitsState, ActiveState
from pinconfig import MotorButtonsPinConfig
from deskmotormock import DeskMotor

class MotorButtons():
    def __init__(self, pin_config: MotorButtonsPinConfig, desk_motor: DeskMotor, limits_state: MotorLimitsState, active_state: ActiveState):
        self._desk_motor = desk_motor
        self._pin_config = pin_config
        self._buttons_state = MotorButtonsState(self._pin_config)
        self._limits_state = limits_state
        self._active_state = active_state
        self._pin_config.btn_down_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._btn_up_INT)
        self._pin_config.btn_up_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._btn_down_INT)

    def _btn_up_INT(self):
        self._pin_config.btn_up_pin.irq(handler=None)

        limit_upper_state = self._limits_state.limit_up_state
        btn_up_state = self._buttons_state.btn_up_state
        btn_down_state = self._buttons_state.btn_down_state
       
        self._active_state.extend_active_state()

        if(btn_down_state == 0 and limit_upper_state == 0):
            if(self._pin_config.btn_up_pin.value() == 1 and btn_up_state == 0):
                # btn_up from low => high
                self._buttons_state.btn_up_state = 1
                self.desk_motor.up()
            elif(self._pin_config.btn_up_pin.value() == 0 and btn_up_state == 1):
                # btn_up from high => low
                self._buttons_state.btn_up_state = 0
                self.desk_motor.stop()
        else:
            # stop if another button is already being pressed or upper limit is reached
            self._desk_motor.stop()

        self._pin_config.btn_up_pin.irq(handler=self._btn_up_INT)

    def _btn_down_INT(self):
        self._pin_config.btn_down_pin.irq(handler=None)

        limit_lower_state = self._limits_state.limit_low_state
        btn_down_state = self._buttons_state.btn_down_state
        btn_up_state = self._buttons_state.btn_up_state
        
        self._active_state.extend_active_state()

        if(btn_up_state == 0 and limit_lower_state == 0):
            # ignore if another button is already being pressed or lower limit is reached
            if(self._pin_config.btn_down_pin.value() == 1 and btn_down_state == 0):
                # btn_down from low => high
                self._buttons_state.btn_down_state = 1
                self.desk_motor.down()
            elif(self._pin_config.btn_down_pin.value() == 0 and btn_down_state == 1):
                # btn_down from high => low
                self._buttons_state.btn_down_state = 0
                self.desk_motor.stop()
        else:
            # stop if another button is already being pressed or upper limit is reached
            self._desk_motor.stop()
        
        self._pin_config.btn_down_pin.irq(handler=self._btn_down_INT)

    def __str__(self) -> str:
        return f'MotorButtons( btn_up_state={self._buttons_state.btn_up_state}, btn_down_state={self._buttons_state.btn_down_state})'
