import numpy as np
import cv2
severity = 5
def load_image(severity):
    img = np.zeros((128,128), dtype=np.uint8)
    radius = severity * 5
    cv2.circle(img,(64,64),radius,200,-1)
    return img

def extract_features(img):
    mean_intensity = img.mean()
    return {
        "mean_intensity" : float(mean_intensity)
    }