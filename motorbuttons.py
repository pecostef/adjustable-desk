from machine import Pin
from  globals import buttons_pin_config, limit_state, buttons_state, active_state, desk_motor

def motor_btn_up_INT(pin):
    global buttons_pin_config
    global limit_state
    global buttons_state
    global active_state
    global desk_motor
    
    buttons_pin_config.btn_up_pin.irq(handler=None)

    limit_state_value =limit_state.limit_state
    btn_up_state = buttons_state.btn_up_state
    btn_down_state = buttons_state.btn_down_state
    
    active_state.extend_active_state()

    if(btn_down_state == 0 and limit_state_value == 0):
        if(buttons_pin_config.btn_up_pin.value() == 1 and btn_up_state == 0):
            # btn_up from low => high
            buttons_state.btn_up_state = 1
            desk_motor.up()
        elif(buttons_pin_config.btn_up_pin.value() == 0 and btn_up_state == 1):
            # btn_up from high => low
            buttons_state.btn_up_state = 0
            desk_motor.stop()
    buttons_pin_config.btn_up_pin.irq(handler=motor_btn_up_INT)

def motor_btn_down_INT(pin):
    global buttons_pin_config
    global limit_state
    global buttons_state
    global active_state
    global desk_motor
    
    buttons_pin_config.btn_down_pin.irq(handler=None)

    limit_state_value = limit_state.limit_state
    btn_down_state = buttons_state.btn_down_state
    btn_up_state = buttons_state.btn_up_state
    
    active_state.extend_active_state()

    if(btn_up_state == 0 and limit_state_value == 0):
        # ignore if another button is already being pressed or lower limit is reached
        if(buttons_pin_config.btn_down_pin.value() == 1 and btn_down_state == 0):
            # btn_down from low => high
            buttons_state.btn_down_state = 1
            desk_motor.down()
        elif(buttons_pin_config.btn_down_pin.value() == 0 and btn_down_state == 1):
            # btn_down from high => low
            buttons_state.btn_down_state = 0
            desk_motor.stop()

    buttons_pin_config.btn_down_pin.irq(handler=motor_btn_down_INT)

buttons_pin_config.btn_up_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=motor_btn_up_INT)
buttons_pin_config.btn_down_pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=motor_btn_down_INT)