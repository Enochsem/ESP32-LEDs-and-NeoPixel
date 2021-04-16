# in this program data pin 2, Gnd and 5v on ws28112B was connected
#to  pin 22, Gnd and 5v of the esp32
#exercise 5 for WS2812B

from time import sleep
from machine import Pin, PWM
import neopixel


d2=Pin(22)
np = neopixel.NeoPixel(d2, 8)


def address():
    pass


def rgb(duration):
    for led in range(0,duration,1):
        np[0] = (255, 0, 0) # set to red, full brightness
        np.write()
        sleep(5)
        np[0] = (0, 255, 0) # set to green, half brightness
        np.write()
        sleep(5)
        np[0] = (0, 0, 255)# set to blue, half brightness
        np.write()
        sleep(5)
        
def offrgb(np):
    np[0]=(0,0,0)
    np.write()

try:
    rgb(1)
    offrgb(np)
except KeyboardInterrupt:
    offrgb(np)
    print('ended')