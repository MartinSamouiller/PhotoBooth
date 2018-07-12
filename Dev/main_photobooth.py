
# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
import cv2
import os

from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera.array

import time
from time import sleep
from datetime import datetime

from gpiozero import Button
from gpiozero import LED

from signal import pause

import threading
import pygame


pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/Photobooth/sound/iphonesound.mp3")

btn_next = Button(26)
btn_presc = Button(19)
btn_snap = Button(13)

led = LED(21)

current_frame = 1
path_filter = 'frames/'
MAX_FRAMES = 3
path_frame = path_filter + 'Frame{}.jpg'.format(current_frame)
frame_type = 1
frameMS = cv2.imread(path_frame)



def process_image(img_cam, frame, frame_type):

    (h_frame, w_frame, d_frame) = frameMS.shape
    (h_img, w_img, d_img) = img_cam.shape

    pox_x = 0
    pox_y = 0

    if frame_type == 1:
        pox_x = int((w_frame - w_img) / 2.0)
        pox_y = int((h_frame - h_img) / 2.0)

    frame[pox_y:pox_y+h_img, pox_x:pox_x+w_img] = img_cam

    return frame

def next_frame():
    global current_frame
    current_frame = current_frame + 1
    if current_frame > MAX_FRAMES:
	    current_frame = 1
    
    global frameMS
    frameMS = cv2.imread(path_filter + 'Frame{}.jpg'.format(current_frame))
    
def previous_frame():
    global current_frame
    current_frame = current_frame - 1
    if current_frame < 1:
	    current_frame = MAX_FRAMES
    
    global frameMS
    frameMS = cv2.imread(path_filter + 'Frame{}.jpg'.format(current_frame))
    
def snap():
    print("Snap")
    #clignote 3 fois, fonction blonquante
    #led.blink(n=3, background= False)
    print("Take a shooot")
    pygame.mixer.music.play()

    datetime_str = datetime.now().isoformat()
    image_path = path_save_images + '%s.jpg' % datetime_str

    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        # At this point the image is available as stream.array        
        cv2.imwrite(image_path, process_image(stream.array, frameMS, frame_type))


btn_next.when_pressed = previous_frame
btn_presc.when_pressed = next_frame
btn_snap.when_pressed = snap

if __name__=="__main__":
    # initialize the camera and grab a reference to the raw camera capture


    #test hard disk at startup : 
    path_save_images = 'media/martindisk/'
    default_path = '/home/pi/Desktop/Capture/'

    #si le disk dure n'est pas monté utilise la carte mémoire par defaut
    if not os.path.exists(path_save_images):
        path_save_images = default_path
        #os.makedirs(path_save_images)

    
    w_flux = 1216
    h_flux = 1920
    size_screen = (w_flux,h_flux)
    
    camera = PiCamera()
    camera.resolution = size_screen
    camera.framerate = 32
    camera.rotation = 180
    rawCapture = PiRGBArray(camera, size=size_screen)
	
    time.sleep(2)
    
    cv2.namedWindow('Faces', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Faces', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        cv2.imshow('Faces', process_image(frame.array, frameMS, frame_type))
        
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
       
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
    
    cv2.destroyAllWindows()



