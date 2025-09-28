##Esse é o menu inicial apresentado após login.

from menus.customer_menu import customer_menu  # Importa função que exibe o menu de clientes
from menus.animal_menu import animal_menu
from menus.appointment_menu import appointment_menu
from menus.veterinarian_menu import veterinarian_menu
import os  # Importa o módulo os para interagir com o sistema operacional
import time

def reload():
    option = input('\nVoltar ao menu inicial?\nDigite "S" para sim e "N" para não:\n')
    if option == 'S':
        print('Voltando ao menu inicial...')
        os.system('cls')  # Limpa a tela do terminal (no Windows)
        initial_menu()  # Chama o menu inicial novamente para permitir outra escolha
    else:
        print('Encerrando programa...')
        time.sleep(3)
        exit()

def initial_menu():
    # Exibe o menu inicial para o usuário escolher uma opção
    print('Bem-vindo(a) ao PetCare, seu sistema de gestão veterinário!\n')
    print('MENU INICIAL\n')
    print('***ESCOLHA O NÚMERO DA OPÇÃO***\n')
    option = int(input('\n 1 - Clientes \n 2 - Animais \n 3 - Veterinários \n'))  # Recebe a opção do usuário e converte para inteiro
    
    match(option):
        case 1:
            customer_menu() 
            reload()
        case 2:
            animal_menu()
            reload()
        case 3:
            veterinarian_menu() 
            reload()