from models.veterinarian import Veterinarian
from utils.db import create_connection
import os

def veterinarian_menu():
    os.system('cls')
    print('***MENU - VETERINÁRIOS***')

    option = int(input('1 - Cadastro de veterinário\n2 - Edição de dados\n3 - Listar especialidade\n'))

    match(option):
        case 1:
            os.system('cls')
            professional_registration = input('\nQual o CRMV do veterinário? \n')
            user_id = int(input('\nQual o ID de usuário do veterinário?\n'))
            name = input('\nQual o nome do veterinário? \n')
            specialty = input('\nQual a especialidade do vetinário? \n')

            new_veterinarian = Veterinarian(professional_registration, user_id, name, specialty)

            conn = create_connection()
            new_veterinarian.register_veterinarian(conn)
            conn.close()
        case 2:
            os.system('cls')
            conn = create_connection()
            Veterinarian.update_data(conn)
            conn.close()
        case 3:
            os.system('cls')
            conn = create_connection()
            print('Especialidade:')
            Veterinarian.list_specialty(conn)
            conn.close()