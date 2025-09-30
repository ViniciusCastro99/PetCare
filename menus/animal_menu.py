from models.animal import Animal
from utils.db import create_connection
import os

def animal_menu():
    os.system('cls')
    print('\n***MENU - ANIMAIS \n')
    print('\n***ESCOLHA O NÚMERO DA OPÇÃO***\n')

    animal_option = int(input('\n 1 - Cadastrar animal \n 2 - Editar dados do animal \n '))

    match(animal_option):
        case 1:
            os.system('cls')
            animal_owner = input('\nQual o CPF do dono do animal?\n')
            animal_name = input('\nQual o nome do animal: \n')
            animal_specie = input('\nQual a espécie do animal? \n')
            animal_race = input('\nQual a raça do animal?\n')
            animal_birthday = input('\nQual a data de aniversario do animal?\n')
            from datetime import datetime
            birth_date = datetime.strptime(animal_birthday, "%d/%m/%Y").date()
            new_animal = Animal(animal_owner, animal_name, animal_specie, animal_race,birth_date)
            
            conn = create_connection()
            new_animal.register_animal(conn)
            conn.close()

        case 2:
            os.system('cls')
            print('\n***EDIÇÃO DE DADOS DO ANIMAL***\n')
            
            conn = create_connection()
            Animal.update_data(conn)