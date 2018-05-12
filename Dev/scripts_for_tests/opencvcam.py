# import the necessary packages
"""from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)
 
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
 
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)"""


# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt

    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    
    if face_cascade.empty():
      raise IOError('Unable to load the face cascade classifier xml file')
    if eye_cascade.empty():
      raise IOError('Unable to load the eye cascade classifier xml file')
  
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
     
    # allow the camera to warmup
    time.sleep(0.1)
    
    centers = []
    sunglasses_img = cv2.imread('overlays/sunglasses.png')
     
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        img = frame.array
        img_cop = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)  
        
        t = time.clock()
        
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
          roi_gray = gray[y:y+h, x:x+w]
          roi_color = img[y:y+h, x:x+w]
          cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
          
          eyes = eye_cascade.detectMultiScale(roi_gray)
          for (x_eye,y_eye,w_eye,h_eye) in eyes:
            centers.append((x + int(x_eye + 0.5*w_eye), y + int(y_eye + 0.5*h_eye)))
            
            center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
            radius = int(0.3 * (w_eye + h_eye))
            color = (0, 255, 0)
            thickness = 2
            cv2.circle(roi_color, center, radius, color, thickness)
            
            for cnt in centers:
              print('x center = %d ; y center = %d' % (cnt[0],cnt[1]))  
        
        if len(centers) > 0:
            
            
            overlay_img = np.ones(img.shape, np.uint8) * 255
            pts1 = np.float32([[76,54],[247,54]])
            pts2 = np.float32([[202,120],[250,120]])
            M = cv2.getPerspectiveTransform(pts1,pts2)
            overlay_img = cv2.warpPerspective(sunglasses_img,M, overlay_img.shape[:2])
            
            
            
            
            # Overlay sunglasses; the factor 2.12 is customizable depending on the size of the face
            #sunglasses_width = 2.12 * abs(centers[1][0] - centers[0][0])
            
            #h, w = sunglasses_img.shape[:2]
            
            #scaling_factor = sunglasses_width / w
            #overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
            
            #x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0]
            # customizable X and Y locations; depends on the size of the face
            #x -= int(overlay_sunglasses.shape[1])
            #y += int(overlay_sunglasses.shape[0])
            #h, w = overlay_sunglasses.shape[:2]
            #h_i, w_i = overlay_img.shape[:2]
            #if x < w_i and y < h_i: 
            #  overlay_img[y:y+h, x:x+w] = overlay_sunglasses
            
            # Create mask
            gray_sunglasses = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_sunglasses, 110, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            temp = cv2.bitwise_and(img_cop, img_cop, mask=mask)
            temp2 = cv2.bitwise_and(overlay_img, overlay_img, mask=mask_inv)
            final_img = cv2.add(temp, temp2)
            cv2.imshow('Sunglasses', final_img)
            
            

        dt = time.clock() - t
        print('time: %.1f ms' % (dt*1000))            
        cv2.imshow('Eye Detector', img)
        key = cv2.waitKey(1) & 0xFF
        # show the frame
        #cv2.imshow("Frame", image)
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
       
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
          break
    
    
    cv2.destroyAllWindows()




"""

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
          roi_gray = gray[y:y+h, x:x+w]
          roi_color = image[y:y+h, x:x+w]
          eyes = eye_cascade.detectMultiScale(roi_gray)
          for (x_eye,y_eye,w_eye,h_eye) in eyes:
              center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
              radius = int(0.3 * (w_eye + h_eye))
              color = (0, 255, 0)
              thickness = 3
              cv2.circle(roi_color, center, radius, color, thickness)
        
        cv2.imshow('Eye Detector', image)
        
        """


