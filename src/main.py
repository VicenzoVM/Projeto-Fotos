import os
import pyzbar
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGES_FOLDER = os.path.join(BASE_DIR, "..", "data", "images")

allowed_extensions = (".jpg", ".jpeg", ".png", ".bmp")

def Check_Files():
    for image in os.listdir(IMAGES_FOLDER):
        if image.lower().endswith(allowed_extensions):
            return 1
            
            
    
def Check_If_QRCODE(image_path):
     image = cv2.imread(str(image_path)) 
     decode(image)