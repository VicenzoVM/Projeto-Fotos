import cv2
from pyzbar.pyzbar import decode
import os 
from config import * 


def open_folder(path):
    """Abre a pasta correspondente no sistema operacional"""
    if os.path.exists(path):
        if os.name == 'nt':  # Windows
            os.startfile(path)
    else:
        print(f" Pasta não encontrada: {path}")




def Read_QR_Code() -> str:
    stream = cv2.VideoCapture(0)
    print("Captura iniciada")

    if not stream.isOpened():
        return (" Erro ao acessar a webcam.")
    
    while True:
        
        ret, frame = stream.read()
        if not ret:
            return ("Erro ao capturar imagem da webcam.")
            
        
        qr_codes = decode(frame)
        
        if qr_codes:
            qr_data = qr_codes[0].data.decode('utf-8').strip()  # Apenas o primeiro QR Code
            folder_path = os.path.join(PROCESSED_IMAGES, qr_data)    

            print(f" QR Code detectado: {qr_data}")
            open_folder(folder_path)
            break   # Fecha o loop imediatamente após encontrar 1 QR Code

        # Exibe a imagem da webcam
        cv2.imshow("Webcam - Leitor de QR Code", frame)
        
         

        # Pressione 'Q' para sair manualmente (se necessário)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return "Captura cancelada manualmente"   

    stream.release()
    cv2.destroyAllWindows()
    return "encerrado"
    