from machine import PWM, Pin


class DeskMotor():
    '''
    The desk motor has a duty cycle of 10%
    The duty cycle for the Pico PWM pins is expressed in the 0 - 65535 range
    Therefore a duty cycle of 10% => 6553.5 ~ 6554
    We will use a period of 1ms => 1000 Hz
    '''
    def __init__(self, pwm_pin, dir_pin) :
        self.__DUTY_CYCLE_10_U16 = 6554
        self.__DUTY_CYCLE_0_U16 = 0
        self.__pwm_pin = PWM(Pin(pwm_pin))
        self.__dir_pin = Pin(dir_pin)

        self.__pwm_pin.freq(1000)
        self.stop()

    def up(self):
        self.__dir_pin.low()
        self.__pwm_pin.duty_u16(self.__DUTY_CYCLE_10_U16)
    
    def down(self):
        self.__dir_pin.high()
        self.__pwm_pin.duty_u16(self.__DUTY_CYCLE_10_U16)
    
    def stop(self):
        self.__dir_pin.low()
        self.__pwm_pin.duty_u16(self.__DUTY_CYCLE_0_U16)
    