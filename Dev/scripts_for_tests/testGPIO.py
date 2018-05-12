from gpiozero import Button
from signal import pause
from time import sleep
import time
from gpiozero import LED
from picamera import PiCamera
from datetime import datetime

btn_next = Button(26)
btn_presc = Button(19)
btn_snap = Button(13)

led = LED(21)

cam = PiCamera()

def next():
    print("Next pressed")
    
def presc():
    print("Pesc pressed")
    
def snap():
    print("Snap")
    #clignote 3 fois, fonction blonquante
    led.blink(n=3, background= False)
    print("Take a shooot")
    datetime_str = datetime.now().isoformat()
    cam.capture('/home/pi/Desktop/Capture/%s.jpg' % datetime_str)    
    
btn_next.when_pressed = presc
btn_presc.when_pressed = next
btn_snap.when_pressed = snap

#led.blink()
#cam.start_preview
#pause()
  
while True:
    time.sleep(0.5)
    
        
