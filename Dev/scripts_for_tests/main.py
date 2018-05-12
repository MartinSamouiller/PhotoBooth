# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
import cv2
from trackers import FaceTracker
import os

def create_mask(img):
  
  if img.shape[2] != 4:
    print("Need png image with alpha channel")
    return False

  mask = np.zeros(img.shape[:2], np.uint8)
  mask[img[:,:,3] == 255] = 255 #supprimer les bords a alpha > 0
  
  return mask

#img_mask : image noir et blanc (0 - 255)
def apply_mask(img_background, img_foreground, img_mask):
  # I want to put logo on top-left corner, So I create a ROI
  rows,cols,channels = img_foreground.shape
  roi = img_background[0:rows, 0:cols ]
  mask_inv = cv2.bitwise_not(img_mask)
  cv2.imshow('Mask',mask_inv)
  
  # Take only region of logo from logo image.
  img2_fg = cv2.bitwise_and(img_foreground,img_foreground,mask = img_mask)
  cv2.imshow('Foreground',img2_fg)
  
  # Now black-out the area of logo in ROI
  img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
  cv2.imshow('Background',img1_bg)
  
  # Put logo in ROI and modify the main image
  dst = cv2.add(img1_bg,img2_fg)
  img_background[0:rows, 0:cols ] = dst
  cv2.imshow('Addition',dst)
  cv2.imshow('Final',img_background)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  

if __name__=="__main__":
  arr = os.listdir('faces/')
  path = 'faces/'
  
  for img_path in arr:
  
    img = cv2.imread(path + img_path)
    
    _faceTracker = FaceTracker()
    _faceTracker.update(img)
    faces = _faceTracker.faces
    
    _faceTracker.drawDebugRects(img)
    
    cv2.imshow('Faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  



#overlays 
"""sunglasses_img = cv2.imread('overlays/blackhat.png')
mask_sungla = create_mask(cv2.imread('overlays/blackhat.png', -1))

path = 'faces/'
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

if face_cascade.empty():
  raise IOError('Unable to load the face cascade classifier xml file')
if eye_cascade.empty():
  raise IOError('Unable to load the face cascade classifier xml file')

#if eye_cascade.empty():
#  raise IOError('Unable to load the eye cascade classifier xml file')

img = cv2.imread(path + 'image1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_cop = img.copy()

apply_mask(img, sunglasses_img, mask_sungla)

centers = []"""

"""
face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in face_rects:
  cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
  roi_gray = gray[y:y+h, x:x+w]
  roi_color = img[y:y+h, x:x+w]
  cv2.imshow('Face ROI', roi_color)
  eyes = eye_cascade.detectMultiScale(roi_gray)
  for (ex,ey,ew,eh) in eyes:
      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
      centers.append((x + int(ex + 0.5*ew), y + int(ey + 0.5*eh)))

centers_glass = []
centers_glass.append((76,54))
centers_glass.append((247,54))


inter_eye = centers_glass[1][0] - centers_glass[0][0]
inter_eye_pra = centers[1][0] - centers[0][0]
scale_facto = inter_eye_pra / inter_eye
overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scale_facto, fy=scale_facto, interpolation=cv2.INTER_AREA)
cv2.imshow('Sunglasse resize', overlay_sunglasses)

h, w = overlay_sunglasses.shape[:2]
img[0:h, 0:w] = overlay_sunglasses
"""



"""
if len(centers) > 0:# Overlay sunglasses; the factor 2.12 is customizable depending on the sizeof the face
  sunglasses_width = 2.12 * abs(centers[1][0] - centers[0][0])
  overlay_img = np.ones(img.shape, np.uint8) * 255
  h, w = sunglasses_img.shape[:2]
  scaling_factor = sunglasses_width / w
  
  overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scaling_factor,
  fy=scaling_factor, interpolation=cv2.INTER_AREA)
  x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0]
  # customizable X and Y locations; depends on the size of the face
  x -= (int)(overlay_sunglasses.shape[1])
  y += (int)(overlay_sunglasses.shape[0])
  h, w = overlay_sunglasses.shape[:2]
  overlay_img[y:y+h, x:x+w] = overlay_sunglasses
  # Create mask
  gray_sunglasses = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(gray_sunglasses, 110, 255, cv2.THRESH_BINARY)
  mask_inv = cv2.bitwise_not(mask)
  temp = cv2.bitwise_and(img_cop, img_cop, mask=mask)
  temp2 = cv2.bitwise_and(overlay_img, overlay_img, mask=mask_inv)
  final_img = cv2.add(temp, temp2)
  cv2.imshow('Eye Detector', img)
  cv2.imshow('Sunglasses', final_img)
  cv2.waitKey()
  cv2.destroyAllWindows()

"""



"""
cv2.imshow('Face Detector', frame)
c = cv2.waitKey(1)
if c == 27:
break
cap.release()
cv2.destroyAllWindows()"""







