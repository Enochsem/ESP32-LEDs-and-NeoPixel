import time
from machine import Pin

#print('hello')
led = Pin(19,Pin.OUT)
try:
    while True:
        led.value(0)
        time.sleep(0.5)
        led.value(1)
        time.sleep(1)
except KeyboardInterrupt:
    led.off()
    print('end')
