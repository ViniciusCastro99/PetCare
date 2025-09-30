##Esse menu faz a interface com o usuário para cadastro e login utilizando as funções do arquivo "login".
import os
import time
from login import login
from login import create_user
from menus.initial_menu import initial_menu

def login_menu():
    def reload():
        os.system('cls')
        login_menu()

    print('*** Bem-vindo(a) ao PetCare, seu sistema de gestão veterinário! ***\n')
    option = int(input('Escolha:\n 1 - Login \n 2 - Cadastro de Usuário\n '))

    if option == 1:
        username = input("Digite seu usuário: ")
        password = input("Digite sua senha: ")

        success, role = login(username, password)

        if success:
            os.system('cls')
            initial_menu(role)
        else:
            print("Acesso negado!")
            time.sleep(3)
            reload()
    elif option == 2:
        username = input('\nEscolha um nome de usuário:\n ')
        role = input('\nQual nível de privilégio do usuário?\n admin \n receptionist\n veterinarian?\n')
        password = input('\nDigite sua senha de preferência:\n ')
        password2 = input('\nRepita sua senha:\n ')
            
        if password == password2:
            create_user(username,password, role)
            print('\nUsuário criado com sucesso!')
            reload()
        else:
            print('\nSenhas não combinam!')
            time.sleep(3)
            reload()
    else:
        print('\nOpção inválida')
        time.sleep(3)
        reload()
