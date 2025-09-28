from models.veterinarian import Veterinarian
from utils.db import create_connection

def veterinarian_menu():
    print('***VETERINÁRIOS***')

    option = int(input('1 - Cadastro de veterinário'))

    match(option):
        case 1:
            professional_registration = input('Qual o CRMV do veterinário? \n')
            name = input('Qual o nome do veterinário? \n')
            specialty = input('Qual a especialidade do vetinário? \n')

            new_veterinarian = Veterinarian(professional_registration, name, specialty)

            conn = create_connection()
            new_veterinarian.register_veterinarian(conn)
            conn.close()
        case 2:
            pass #EDIÇÃO DE DADOS
