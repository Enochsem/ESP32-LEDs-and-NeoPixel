# in this program data pin 0, Gnd and 5v on ws28112B was connected
#to  pin 26, Gnd and 5v of the esp32

from time import sleep
from machine import Pin, PWM
import neopixel


d2=Pin(26)
np = neopixel.NeoPixel(d2, 8)





def offlights():
    np[0] = (0,0,0)
    np[1] = (0,0,0)
    np[2] = (0,0,0)
    np[3] = (0,0,0)
    np[4] = (0,0,0)
    np[5] = (0,0,0)
    np[6] = (0,0,0)
    np.write()


def rgb(np):
    red=0
    green=0
    blue = 0
    color=255
    for cycle in range(0,3,1):
        if cycle == 1:
            red =0
            green =color
        elif cycle == 2:
            red=0
            green=0
            blue=color
        else:
            red=color
        for address in range(0,7,1):
             np[address] = (red, green, blue)# set
             print('At index {} => color address of {}'.format(address,np[address]))
             np.write()
             colors=0
             sleep(5)
        
        #off
        offlights()


#start
rgb(np)
