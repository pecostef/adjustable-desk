import errno
from time import sleep_ms
import time
import globals

import motorbuttons
import motorlimit

try:
    while True:
        print(str(globals.buttons_state))
        print(str(globals.limit_state))
        sleep_ms(200)
except OSError as exc:
    if exc.args[0] == errno.EAGAIN: 
        print ('EAGAIN')
        globals.desk_motor.stop()
        time.sleep(3)           # short delay, no tight loops
except:
    globals.desk_motor.stop()
    
    

