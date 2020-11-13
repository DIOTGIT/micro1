import wifiLIB
import DHT2G




from machine import Timer

tim = Timer(-1)
tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
# tim.init(period=5000, mode=Timer.PERIODIC, callback=lambda t:repeat5())

import time
start = time.ticks_ms() # get millisecond counter
delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
start = time.ticks_ms()
while False:
    TS = int(time.ticks_diff(time.ticks_ms(), start)/1000)
    print(TS)
    time.sleep(2)


def repeat5():
    print(5)

