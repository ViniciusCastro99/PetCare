from utils.db import create_connection


class Customer:

    customer_list = []

    def __init__(self, cpf, name, phone, street, neighborhood, house_number, city, state, postal_code, country, address_complement, birth_date):
        self._cpf = cpf
        self._name = name
        self._phone = phone
        self._street = street
        self._neighborhood = neighborhood
        self._house_number = house_number
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._country = country
        self._address_complement = address_complement
        self._birth_date = birth_date
    
    def register_customer(self, conn):
        cursor = conn.cursor()
        sql = '''INSERT INTO customer 
    (customer_id, customer_name, customer_phone, address_street, address_neighborhood, address_number, address_city, address_state, address_postal_code, address_country, address_complement, birth_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        
        value = (
        self._cpf,
        self._name,
        self._phone,
        self._street,
        self._neighborhood,
        self._house_number, 
        self._city,
        self._state,
        self._postal_code,
        self._country,
        self._address_complement,
        self._birth_date
        )

        cursor.execute(sql,value)
        conn.commit()
        cursor.close()

    def list_customer(conn):
        cursor = conn.cursor()
        sql = '''SELECT customer_id, customer_name FROM customer'''
        cursor.execute(sql)

        valid_rows = [row for row in cursor if row[0] is not None] ##serve para validar se uma linha é válida para ser exibida

        if not valid_rows:
            print('Sem clientes cadastrados')
        else:
            for row in valid_rows:
                print(f'CPF: {row[0]} | Nome: {row[1]}')
        cursor.close()

##FALTA TERMINAR A INTEGRAÇÃO COM O BANCO DE DADOS
    def edit_data(conn):
        customer_id = input('Qual o CPF do cliente?')
        option = int(input(
            "Escolha o número do dado que deseja alterar:\n"
            " 1 - Nome\n"
            " 2 - Telefone\n"
            " 3 - Rua\n"
            " 4 - Bairro\n"
            " 5 - Número da casa\n"
            " 6 - Cidade\n"
            " 7 - Estado\n"
            " 8 - CEP\n"
            " 9 - País\n"
            " 10 - Complemento\n"
            " 11 - Data de nascimento\n"
            "Opção: "
        ))
        cursor = conn.cursor()

        def execute_commit_close_sql(query_sql, values):
            cursor.execute(query_sql,values)
            conn.commit()
            print('\nDados atualizados com sucesso!')
            cursor.close

        match(option):
            ## lembre-se de fazer uma validação para existência do cpf
            ##também deve-se fazer um try exception para atualização dos dados.
            case 1: 
                new_name = input('\nDigite o novo nome do cliente: ')
                sql="""UPDATE customer SET customer_name = %s WHERE customer_id = %s;"""
                val = (new_name, customer_id)

                execute_commit_close_sql(sql, val)

            case 2: 
                new_phone = input('\nDigite o novo número de telefone: ')
                sql = """ UPDATE customer SET customer_phone = %s WHERE customer_id = %s; """
                val = (new_phone, customer_id)

                execute_commit_close_sql(sql, val)

            case 3: 
                new_street = input('\nDigite a nova rua: ')
                sql = """ UPDATE customer SET address_street = %s WHERE customer_id = %s; """
                val = (new_street,customer_id)

                execute_commit_close_sql(sql, val)

            case 4:
                new_neighborhood = input('\nDigite o novo Bairro do cliente: ')
                sql = """UPDATE customer SET address_neighborhood = %s WHERE customer_id = %s;"""
                val = (new_neighborhood,sql)

                execute_commit_close_sql(sql, val)
            case 5:
                new_number = input('\nDigite o novo número da casa: ')
                sql="""UPDATE customer SET address_number = %s WHERE customer_id = %s;"""
                val = (new_number, customer_id)

                execute_commit_close_sql(sql, val) 
            case 6:
                new_city = input('\nDigite a nova cidade do cliente: ')   
                sql = """ UPDATE customer SET address_city = %s WHERE customer_id = %s; """
                val = (new_city, customer_id)         

                execute_commit_close_sql(sql, val)
            case 7: 
                new_state = input('\nDigite o novo estado do cliente no formato de duas letras. Ex(SP): ')
                sql = """ UPDATE customer SET address_state = %s WHERE customer_id = %s; """
                val = (new_state, customer_id)

                execute_commit_close_sql(sql, val)
            case 8:
                new_postal_code = input('\nDigite o novo CEP: ')
                sql = """ UPDATE customer SET address_postal_code = %s WHERE customer_id = %s; """
                val = (new_postal_code, customer_id)

                execute_commit_close_sql(sql, val)
            case 9:
                new_country = input('\nDigite o novo país: ')
                sql = """ UPDATE customer SET address_country = %s WHERE customer_id = %s; """
                val = (new_country, customer_id)

                execute_commit_close_sql(sql, val)
            case 10:
                new_complement = input('\nDigite o novo complemento: ')
                sql = """ UPDATE customer SET address_complement = %s WHERE customer_id = %s; """
                val = (new_complement, customer_id)

                execute_commit_close_sql(sql, val)
            case 11:
                new_birth_date = input('\nDigite a nova data de aniversário: ')
                sql = """ UPDATE customer SET birth_date = %s WHERE customer_id = %s; """
                val = (new_birth_date, customer_id)

                execute_commit_close_sql(sql, val)
            case _:
                print('\nOpção inválida!')