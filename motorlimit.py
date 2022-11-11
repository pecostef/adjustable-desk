from machine import Pin
from  globals import limit_switch_pin_config, limit_state, active_state, desk_motor

def limit_INT(pin):
    global limit_switch_pin_config
    global limit_state
    global active_state
    global desk_motor

    limit_switch_pin_config.limit_pin.irq(handler=None)
    
    limit_state_value = limit_state.limit_state
    active_state.extend_active_state()

    if(limit_switch_pin_config.limit_pin.value() == 1 and limit_state_value == 0):
        # upper limit switch from low => high
        limit_state.limit_state = 1
        desk_motor.stop()
    elif(limit_switch_pin_config.limit_pin.value() == 0 and limit_state_value == 1):
        # upper limit switch from high => low
        limit_state.limit_state = 0

    limit_switch_pin_config.limit_pin.irq(handler=limit_INT)

limit_switch_pin_config.limit_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=limit_INT)