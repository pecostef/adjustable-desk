from machine import Pin
class MotorButtonsPinConfig():
    def __init__(self, btn_up_pin, btn_down_pin):
        self.btn_up_pin = Pin(btn_up_pin, Pin.IN)
        self.btn_down_pin = Pin(btn_down_pin, Pin.IN)

class MotorLimitPinConfig():
    def __init__(self, limit_pin):
        self.limit_pin = Pin(limit_pin, Pin.IN)