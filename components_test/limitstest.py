import globals
from time import sleep_ms

import motorlimits

while True:
    print(str(globals.limits_state))
    if(not globals.active_state.is_active()):
        print('deepsleep() awake from Pins is not implemented :(')
    else:
        sleep_ms(500)
    


