from time import sleep
from picamera import PiCamera
import time
import picamera


with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    camera.start_preview()
    time.sleep(2)
    camera.capture_sequence([
        'faces/image1_ms.jpg',
        'faces/image2_ms.jpg',
        'faces/image3_ms.jpg',
        'faces/image4_ms.jpg',
        'faces/image5_ms.jpg',
        ])