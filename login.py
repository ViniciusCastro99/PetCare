##Esse arquivo estabele a lógica de criação de usuário e login.
import bcrypt
from utils.db import create_connection


def create_user(username,password):
    conn = create_connection()
    cursor = conn.cursor()

    #cria hasg da senha
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    sql = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
    cursor.execute(sql, (username,hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    print('Usuário criado com sucesso!')

def login(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    sql = "SELECT password_hash FROM users WHERE username = %s"
    cursor.execute(sql,(username,))
    result = cursor.fetchone()
    cont = 0

    if result:
        stored_hash = result[0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print('Login bem-sucedido!')
            return True
        else:
            print('Senha incorreta!')

            return False
    else:
        print('Usuário não encontrado!')
        return False
        cursor.close()
        conn.close()
