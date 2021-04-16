# in this program data pin 2, Gnd and 5v on ws28112B was connected
#to  pin 22, Gnd and 5v of the esp32

import time
from machine import Pin,PWM
import neopixel
#from repmtexercise5 import offrgb


d2=Pin(5)
pwm=PWM(d2)#freq=1000, duty=512
np = neopixel.NeoPixel(d2, 8)

#pwm.duty(1023)


def offrgb(np):
    np[0]=(0,0,0)
    np.write()
    
def rgb(np):
    for red in range(0,510,255):
        pwm.freq(500)
        for green in range(0,510,255):
            for blue in range(0,510,255):
                 np[0] = (red, green, blue)
                 np.write()
                 print(np[0])
                 time.sleep(1)







    


try:
    rgb(np)
    offrgb(np)
except KeyboardInterrupt:
    offrgb(np)
    print('ended')