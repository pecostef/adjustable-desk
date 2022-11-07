from machine import Pin
from  globals import limit_switches_pin_config, limits_state, buttons_state, active_state, desk_motor

def limit_upper_INT(pin):
    global limit_switches_pin_config
    global limits_state
    global active_state
    global desk_motor

    limit_switches_pin_config.limit_up_pin.irq(handler=None)
    
    limit_upper_state = limits_state.limit_up_state
    active_state.extend_active_state()

    if(limit_switches_pin_config.limit_up_pin.value() == 1 and limit_upper_state == 0):
        # upper limit switch from low => high
        limits_state.limit_up_state = 1
        desk_motor.stop()
    elif(limit_switches_pin_config.limit_up_pin.value() == 0 and limit_upper_state == 1):
        # upper limit switch from high => low
        limits_state.limit_up_state = 0

    limit_switches_pin_config.limit_up_pin.irq(handler=limit_upper_INT)

def limit_lower_INT(pin):
    global limit_switches_pin_config
    global limits_state
    global active_state
    global desk_motor
    limit_switches_pin_config.limit_low_pin.irq(handler=None)

    limit_lower_state = limits_state.limit_low_state
    active_state.extend_active_state()

    if(limit_switches_pin_config.limit_low_pin.value() == 1 and limit_lower_state == 0):
        # lower limit switch from low => high
        limits_state.limit_low_state = 1
        desk_motor.stop()
    elif(limit_switches_pin_config.limit_low_pin.value() == 0 and limit_lower_state == 1):
        # lower limit switch from high => low
        limits_state.limit_low_state = 0
    limit_switches_pin_config.limit_low_pin.irq(handler=limit_lower_INT)

limit_switches_pin_config.limit_up_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=limit_upper_INT)
limit_switches_pin_config.limit_low_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=limit_lower_INT)