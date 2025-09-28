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
    option = int(input('Escolha:\n 1 - Login \n 2 - Cadastro de Usuário '))

    if option == 1:
        username = input("Digite seu usuário: ")
        password = input("Digite sua senha: ")

        if login(username, password):
            os.system('cls')
            initial_menu()
        else:
            print("Acesso negado!")
            time.sleep(3)
            reload()
    elif option == 2:
        username = input('Escolha um nome de usuário: ')
        password = input('Digite sua senha de preferência: ')
        password2 = input('Repita sua senha: ')
            
        if password == password2:
            create_user(username,password)
            print('Usuário criado com sucesso!')
            reload()
        else:
            print('Senhas não combinam!')
            time.sleep(3)
            reload()
    else:
        print('Opção inválida')
        time.sleep(3)
        reload()
