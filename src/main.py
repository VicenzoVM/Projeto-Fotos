import os
from pyzbar.pyzbar import decode
import cv2
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGES_FOLDER = os.path.join(BASE_DIR, "..", "data", "images")

PROCESSED_IMAGES = os.path.join(BASE_DIR, "..", "data", "processed_images")

allowed_extensions = (".jpg", ".jpeg", ".png", ".bmp")

def Check_Files():
    for image in reversed(os.listdir(IMAGES_FOLDER)):
        if image.lower().endswith(allowed_extensions):
            qr_code_data = Check_If_QRCODE(image) 
            
            if qr_code_data:
                    qr_code_message = (qr_code_data[0][0]).decode("utf-8")
                    os.mkdir(os.path.join(PROCESSED_IMAGES,qr_code_message))
                    os.rename(os.path.join(IMAGES_FOLDER,image),os.path.join(PROCESSED_IMAGES,qr_code_message,image)) 
                    
                    
            else:
                os.rename(os.path.join(IMAGES_FOLDER,image),os.path.join(PROCESSED_IMAGES,qr_code_message,image)) 
                
                    
                
                
                
                
                
            
            
def Check_If_QRCODE(image):
    image_path = os.path.join(IMAGES_FOLDER, image)
    converted_image = Image.open(image_path).convert('L')  # 'L' = Grayscale
    return decode(converted_image)
    


Check_Files()