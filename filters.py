#this file contains 3 different filters

import numpy as np

def apply_warm_filter(image):
    warm = image.copy()
    warm[:, :, 2] = np.clip(warm[:, :, 2] + 30, 0, 255) #red
    warm[:, :, 2] = np.clip(warm[:, :, 0] - 30, 0, 255) #blue
    return warm

def apply_pastel_filter(image):
    import cv2
    pastel = image.copy()
    pastel = cv2.cvtColor(pastel, cv2.COLOR_BGR2HSV)
    pastel[:, :, 1] = pastel[:, :, 1] * 0.5 #lower saturation
    pastel[:, :, 2] = np.clip(pastel[:, :, 2] + 40, 0, 255) #brighten
    pastel = cv2.cvtColor(pastel, cv2.COLOR_HSV2BGR)
    return pastel

def apply_bw_with_grain(image):
    import cv2
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grain = np.random.randint(0, 50, gray.shape, dtype='uint8')
    noisy = cv2.add(gray, grain)
    return cv2.cvtColor(noisy, cv2.COLOR_GRAY2BGR)

