import esp
esp.osdebug(None)

import gc
gc.collect()

# ha nincs WIFI, leáll
# wlan = wifiLIB.get_connection(True)
# if wlan is None:
#     print("Could not initialize the network connection.")
#     import sys
#     sys.exit()

# print(wlan.config('essid'))
# print(wlan.ifconfig())