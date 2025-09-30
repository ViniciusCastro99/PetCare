##Esse é o menu inicial apresentado após login.

from menus.customer_menu import customer_menu  # Importa função que exibe o menu de clientes
from menus.animal_menu import animal_menu
from menus.appointment_menu import appointment_menu
from menus.veterinarian_menu import veterinarian_menu
import os  # Importa o módulo os para interagir com o sistema operacional
import time

def reload(role):
    option = input('\nVoltar ao menu inicial?\nDigite "S" para sim e "N" para não:\n')
    if option == 'S':
        print('Voltando ao menu inicial...')
        os.system('cls')  # Limpa a tela do terminal (no Windows)
        initial_menu(role)  # Chama o menu inicial novamente para permitir outra escolha
    else:
        print('Encerrando programa...')
        time.sleep(3)
        exit()

def initial_menu(role):
    # Exibe o menu inicial para o usuário escolher uma opção
    print('Bem-vindo(a) ao PetCare, seu sistema de gestão veterinário!\n')
    print('\n***MENU - INICIAL***\n')
    print('\nEscolha uma opção:\n')
    
    if role =='admin':
        option = input('\n Clientes \n Animais \n Veterinários \n Agendamentos \n')
    elif role == 'veterinarian':
        option = input('Animais\n')
    elif role == 'receptionist':
        option = input('\n Clientes \n Animais')
    

    match(option):
        case 'Clientes':
            customer_menu() 
            reload(role)
        case 'Animais':
            animal_menu()
            reload(role)
        case 'Veterinários':
            veterinarian_menu() 
            reload(role)
        case 'Agendamentos':
            appointment_menu()
            reload(role)