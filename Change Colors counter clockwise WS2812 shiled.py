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
        for address in range(6,-1,-1):
             #print('s')
             np[address] = (red, green, blue)# set
             #print(address)
             np.write()
             colors=0
             sleep(1)
        
        #off
        offlights()




def duration(duration):
    for numtimes in range(0,duration):
        #start
        rgb(np)
        print('Going {}\'s'.format(numtimes))
        
try:
    duration(2)
except KeyboardInterrupt:
    offlights()
    print('ended')