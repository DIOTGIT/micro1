import wifiLIB
import DHT2G
import time

ST = time.ticks_ms()

dat = list()

while True:
    # olvassa a szenzort
    time.sleep(10)
    sens = DHT2G.get_sensor()
    TS = int(time.ticks_diff(time.ticks_ms(), ST) / 1000)
    dat.append([TS, 'Temperature', sens['Temperature']])
    dat.append([TS, 'Humidity', sens['Humidity']])
    print('adatbázis hossza: {} adat'.format(len(dat)))

    if len(dat) > 10:  # ha már több mint 10 elküldendő adat van
        wlan = None
        wlan = wifiLIB.get_connection(True)
        if not wlan is None:
            param = ''
            ig = 20
            if len(dat) < ig:
                ig = len(dat)
            for i in range(ig):
                param = param + '&TS={}&T={}&V={}'.format(dat[i][0], dat[i][1], dat[i][2])
            param = '?' + param[1:] + '&CT={}'.format(int(time.ticks_diff(time.ticks_ms(), ST) / 1000))
            print('send...')
            resp = DHT2G.call_google_script(param)
            if resp:
                del dat[0:ig]








