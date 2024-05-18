import time
timer = 60 
while timer:
    mins, secs = divmod(timer, 60)
    timer_display = '{:02d}:{:02d}'.format(mins, secs)
    print(timer_display, end='\r')
    time.sleep(1)
    timer -= 1