import cv2
import os
import csv
import sys
import numpy as np
#sys.path.insert(0, "/home/olivier/scripts")


#create csv file with list 
"""arr = os.listdir('overlays')
print('arrrrrr ------', arr)

with open("overlays/overlays.csv",'w') as f:
    wr = csv.writer(f, delimiter="\n")
    wr.writerow(arr)
   """
class Overlay(object):
    """Data on facial features: face, eyes, nose, mouth."""
    
    def __init__(self):
        return 
    
    
    
    

arr = os.listdir('overlays')
#print(arr)

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



foreground = cv2.imread('overlays/testchat.png')
background = cv2.imread("faces/image1.jpg")
alpha = create_mask(cv2.imread('overlays/testchat.png' ,-1))

cv2.imshow('foreground',foreground)
cv2.imshow('background',background)
cv2.imshow('alpha',alpha)

cv2.waitKey(0)
cv2.destroyAllWindows()

apply_mask(background, foreground, alpha)




