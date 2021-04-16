import time
from machine import Pin


led = Pin(19,Pin.OUT)
offtime=200

    

def s():
    for i in range(0,3,1):
        led.on()
        time.sleep_ms(300)
        led.off()
        time.sleep_ms(offtime)


def l():
    for i in range(0,3,1):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep_ms(offtime)

try:
    while True:
        s()
        l()
        s()
        time.sleep(1)
except KeyboardInterrupt:
    led.off()
    print('end')


