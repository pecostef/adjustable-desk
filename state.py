from machine import Pin
from pinconfig import LimitSwitchesPinConfig, MotorButtonsPinConfig
from utime import sleep_ms, ticks_ms, ticks_diff

class MotorLimitsState:
    def __init__(self, pin_config: LimitSwitchesPinConfig):
        self._pin_config = pin_config
        self._limit_up_state = pin_config.limit_up_pin.value()
        self._limit_low_state = pin_config.limit_low_pin.value()

    @property
    def limit_up_state(self):
        return self._limit_up_state
    
    @limit_up_state.setter
    def limit_up_state(self, value):
        self._limit_up_state = value

    @property
    def limit_low_state(self):
        return self._limit_low_state

    @limit_low_state.setter
    def limit_low_state(self, value):
        self._limit_low_state = value

class MotorButtonsState:
    def __init__(self, pin_config: MotorButtonsPinConfig):
        self._pin_config = pin_config
        self._btn_up_state = pin_config.btn_up_pin.value()
        self._btn_down_state = pin_config.btn_down_pin.value()
    
    @property
    def btn_up_state(self):
        return self._btn_up_state
    
    @btn_up_state.setter
    def btn_up_state(self, value):
        self._btn_up_state = value

    @property
    def btn_down_state(self):
        return self._btn_down_state

    @btn_down_state.setter
    def btn_down_state(self, value):
        self._btn_down_state = value


class ActiveState:
    def __init__(self, inactive_timeout_ms) -> None:
        self._last_start_or_interrupt_time = ticks_ms()
        self._inactive_timeout_ms = inactive_timeout_ms
    
    def extend_active_state(self):
        self._last_start_or_interrupt_time = ticks_ms()

    def is_active(self):
        diff = ticks_diff(ticks_ms(), self._last_start_or_interrupt_time)
        return  diff < self._inactive_timeout_ms
