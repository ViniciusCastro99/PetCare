from models.customer import Customer
from utils.db import create_connection
import os

def customer_menu():
    import os
    print('\n***MENU - CLIENTES:***: \n')
    print('\n***ESCOLHA O NÚMERO DA OPÇÃO***\n')

    customer_option = int(input('\n 1 - Registrar cliente \n 2 - Editar dados do Cliente\n 3 - Listar clientes\n'))
   
    match(customer_option):
        case 1:
            import os
            print('\n***CADASTRO DE CLIENTE***\n')
            cpf = input('\nQual o CPF do cliente?\n')
            name = input('\nQual o nome do cliente?\n')
            phone = input('\nQual o telefone de contato?\n')
            street = input('\nQual a rua do cliente?\n')
            neighborhood = input('\nQual o bairro do cliente?\n')
            address_number = input('\nQual o número da casa do cliente?\n')
            city = input('\nQual a cidade do cliente?\n')
            state = input('\nQual o estado do cliente?\n')
            postal_code = input('\nQual o CEP do cliente?\n')
            country = input('\nQual o país do cliente?\n')
            address_complement = input('\nO endereço tem algum complemento?\n')
            birth_input = input('\nQuando é o aniversário do cliente?\n')
            
            from datetime import datetime
            birth_date = datetime.strptime(birth_input, "%d/%m/%Y").date()

            new_customer = Customer(cpf, name, phone, street,neighborhood, address_number, city, state,
            postal_code, country, address_complement, birth_date)
            
            conn = create_connection()
            new_customer.register_customer(conn)
            conn.close()
        case 2: 
            import os
            print('\n***EDIÇÃO DE DADOS DO CLIENTE***\n')
            conn = create_connection()
            Customer.edit_data(conn)
            conn.close()
        case 3:
            import os
            conn = create_connection()
            Customer.list_customer(conn)
            conn.close()

   
   
