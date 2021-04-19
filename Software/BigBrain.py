# BigBrain.py
# OS-BL Raspberry Pi control
# Imaad Syed
# 4/19/2021

from picamera import PiCamera
from time import sleep
import keyboard
import serial

invert = 0

port = serial.Serial('/dev/ttyACM0')

a = True
x = 0
y = 0
z = 0
i = 1

cam = PiCamera()

cam.start_preview()

while(a):
    if keyboard.is_pressed('q'): # capture when q pressed
        cam.capture('/home/pi/Desktop/laserView%s.jpg' % i)
        i = i + 1
    
    if keyboard.is_pressed('i'): # toggle inverted color scheme with i
        if(invert == 0):
            cam.image_effect = 'negative'
            invert = 1
        else:
            cam.image_effect = 'none'
            invert = 0
        sleep(0.3)
    
    if keyboard.is_pressed('x'):
        a = False
    
    # w is up (Y=1), s is down (Y=-1), otherwise set Y to 0
    # a is left (X=-1), d is right (X=1), otherwise set X to 0
    if keyboard.is_pressed('w'):
        y = 1
    elif keyboard.is_pressed('s'):
        y = -1
    else:
        y = 0
    
    if keyboard.is_pressed('a'):
        x = -1
    elif keyboard.is_pressed('d'):
        x = 1
    else:
        x = 0
        
    # raising and lowering arm
    if keyboard.is_pressed('o'):
        z = 1
    elif keyboard.is_pressed('l'):
        z = -1
    else:
        z = 0
    
    # serial transfer to Arduino
    port.write(x)
    port.write(y)
    port.write(z)
    
    # space for future AI integration

cam.stop_preview()
