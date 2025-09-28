import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="250616Sabado*",
        database="petcare"
    )
    return conn