from utils.db import create_connection
class Animal:

    animal_list = []

    def __init__(self, owner, name, specie, race, birthday ):
        self._owner = owner
        self._name = name
        self._specie = specie
        self._race = race
        self._birthday = birthday
        self._id = None

    @property
    def show_informations(self):
        return f'Nome: {self._name} | Espécie: {self._specie} | Raça: {self._race} | Idade: {self._age} | Dono: {self._owner}'

    def register_animal(self,conn):
        cursor = conn.cursor()
        sql = """ INSERT INTO animals (owner_id, animal_name, animal_specie, animal_race, animal_birthday) VALUES (%s, %s, %s, %s, %s); """
        val = (
            self._owner,
            self._name,
            self._specie,
            self._race,
            self._birthday 
        )

        cursor.execute(sql,val)
        conn.commit()
        print('Animal cadastrado com sucesso!')
        cursor.close()

    def update_data(conn):
        animal_id = int(input('\n Qual o ID do animal?\n'))
        print('\nEscolha o número da opção que deseja alterar:\n')
        option = int(input(' 1 - Nome \n 2 - Espécie \n 3 - Raça \n 4 - Idade \n 5 - Dono\n'))
        
        cursor = conn.cursor()

        def execute_commit_close_sql(query,values):
            cursor.execute(query,values)
            conn.commit()
            cursor.close()
            
        match(option):
            case 1: 
                new_name = input('\nDigite o novo nome do seu bichinho: \n')
                sql = """ UPDATE animals SET animal_name = %s WHERE animal_id = %s; """
                val = (new_name, animal_id)
                execute_commit_close_sql(sql,val)
            case 2:
                new_specie = input('\nDigite a espécie correta do seu bichinho: \n')
                sql = """ UPDATE animals SET animal_specie = %s WHERE animal_id = %s; """
                val=(new_specie,animal_id)
                execute_commit_close_sql(sql,val)
            case 3:
                new_race = input('\nDigite a raça correta do seu bichinho: \n')
                sql = """ UPDATE animals SET animal_race = %s WHERE animal_id = %s; """
                val = (new_race, animal_id)
                execute_commit_close_sql(sql,val)
            case 4: 
                new_birthday = input('\nDigite a data de nasciment: \n')
                sql = """ UPDATE animals SET animal_birthday = %s WHERE animal_id = %s; """
                val = (new_birthday, animal_id)
                execute_commit_close_sql(sql,val)
            case 5:
                new_owner = input('\nDigite o CPF do novo dono: \n')
                sql = """ UPDATE animals SET owner_id = %s WHERE animal_id = %s; """
                val = (new_owner, animal_id)
                execute_commit_close_sql(sql,val)
            case _:
                print('\nOpção inválida!\n')
