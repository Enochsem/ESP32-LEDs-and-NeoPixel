# in this program data pin 2, Gnd and 5v on ws28112B was connected
#to  pin 22, Gnd and 5v of the esp32

from time import sleep
from machine import Pin
import neopixel


d2=Pin(22)
np = neopixel.NeoPixel(d2, 8)



def offrgb(np):
    np[0]=(0,0,0)
    np.write()
    print('off')
        

if __name__ == '__main__':
    try:
        offrgb(np)
    except KeyboardInterrupt:
        
        print('ended')
