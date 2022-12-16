import numpy as np
import cv2 


def argument_night(img):
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    arr1 = im_rgb*np.array([0.1, 0.2, 0.5])
    # rescales arr so that the maximum value is 255.0
    arr2 = (255*arr1/arr1.max()).astype(np.uint8)
    im_bgr = cv2.cvtColor(arr2.copy(), cv2.COLOR_RGB2BGR)  
    # more gamma more dark
    gamma = 1.5
    gamma_img = np.array(255*(im_bgr/255)**gamma, dtype='uint8')
    return gamma_img