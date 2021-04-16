# in this program data pin 2, Gnd and 5v on ws28112B was connected
#to  pin 22, Gnd and 5v of the esp32

import time
from machine import Pin
import neopixel
#from repmtexercise5 import offrgb


d2=Pin(22)
np = neopixel.NeoPixel(d2, 8)



def offrgb():
    np[0]=(0,0,0)
    np.write()
    
def rgb(np):
    for red in range(0,255,1):
        for green in range(0,255,1):
            for blue in range(0,255,1):
                 np[0] = (red, green, blue)
                 np.write()
                 print('color {}'.format(np[0]))
                 time.sleep_ms(20)



if __name__ =="__main__":
    try:
        rgb(np)
        offrgb()
    except KeyboardInterrupt:
        offrgb()
        print('ended')





