import errno
import time
import globals
from time import sleep


try:
    while True:
        print('motor up for 2 seconds')
        globals.desk_motor.up()
        sleep(2)
        print('stop for 2 secs')
        globals.desk_motor.stop()
        sleep(2)
        print('motor down for 2 seconds')
        globals.desk_motor.down()
        sleep(2)
        print('stop for 2 secs')
        globals.desk_motor.stop()
        sleep(2)
except OSError as exc:
    if exc.args[0] == errno.EAGAIN: 
        print ('EAGAIN')
        globals.desk_motor.stop()
        time.sleep(3)           # short delay, no tight loops
except:
    globals.desk_motor.stop()
    


