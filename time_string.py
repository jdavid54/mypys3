import time
once = False
repeat = not once

while once or repeat:
    txt = time.strftime('%H:%M:%S')    
    print('\r'+txt,end='')
    once = not once
    if repeat:
        time.sleep(1)
