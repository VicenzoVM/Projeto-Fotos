from services.organizer import Check_Files
from services.webcam_service import Read_QR_Code
import os 
import time 

def show_menu():
    
    while True:  
        
        print("\nEscolha uma opção:")
        print("1 - Organizar pasta de imagens")
        print("2 - Ler QR Code via webcam e abrir a pasta correspondente")
        print("3 - Sair do programa")

        option = input("Digite a opção desejada: ").strip()

        if option == "1":
            os.system('cls')
            print(Check_Files())

        elif option == "2":
            os.system('cls')
            Read_QR_Code()

        elif option == "3":
            os.system('cls')
            print("Encerrando o programa... Até mais!")
            break  # Encerra o programa corretamente

        else:
            print("Opção inválida. Tente novamente.")
        
        
        


            