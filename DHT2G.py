# a hőmérőt elküldi a google sheetre


from machine import Pin
from time import sleep
import dht
import urequests


def get_sensor():
    # from machine import Pin
    # from time import sleep
    # import dht
    try:
        sensor = dht.DHT22(Pin(14))
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print('...reading DHT22 sensor : Temperature:{}, Humidity:{}'.format(temp, hum))
        return {'Temperature': temp, 'Humidity': hum}
    except OSError as e:
        print('Failed to read DHT22 sensor.')
        return None


def send_to_gsheet(tag='', value=''):
    ret = True
    urlbase = 'https://script.google.com/macros/s/AKfycbyzfi17i1DmQZD9jWI40K_3AHkPJX8C4wwLcC6Ozk2QBGJeFow/exec?'
    url = urlbase + 'tag={}&value={}'.format(tag, value)
    try:
        response = urequests.get(url)
        if response.status_code != 200:
            print("Google sheet error")
            ret = False
        else:
            print("Google OK")
        response.close()
    except:
        print("Google sheet error")
        ret = False

    return ret


def call_google_script(param=''):
    ret = True
    urlbase = 'https://script.google.com/macros/s/AKfycbwYb8khluV17_6_J3inUU7rKR9UK2fCb8o5hXRwQ7ncbQjVvADz/exec'
    url = urlbase + param
    try:
        response = urequests.get(url)
        if response.status_code != 200:
            print("Google sheet error1")
            ret = False
        else:
            print("Google OK")
        response.close()
    except:
        print("Google sheet error2")
        ret = False

    return ret







