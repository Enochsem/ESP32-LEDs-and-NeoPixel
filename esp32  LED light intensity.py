import time
from machine import Pin, PWM
from math import sin, pi

#creating pin object
pin19 = Pin(19)
#creating PWM Object
pwm = PWM(pin19)
pwm.freq(1000)

halfb = 512
fullb = 1023

def intensity(duration,res):
    for i in range(0,res):
        brightness = int((sin(time.ticks_ms()/1000)+1)*halfb)
        print(brightness)
        pwm.duty(round(brightness))
        time.sleep_ms(duration)


#using the defalut frequency
def pwmfrq():
    pwd.freq(1000)
    led = int((sin(time.ticks_ms()/1000)+1)*halfb)
    pwm.duty(led)
    time.sleep_ms(200)


def muldulate():
    for up in range(0,100,1):
        pwm.duty(up)
        time.sleep_ms(20)
    for down in range(100,0,-1):
        pwm.duty(down)
        time.sleep_ms(20)
        
        

try:
    while True:
        pwmfrq()
        
        #intensity(20,100)#this takes duration and range
        
        #muldulate()#uses two loop to ulternate the intensity
except KeyboardInterrupt:
    
    print('end')


