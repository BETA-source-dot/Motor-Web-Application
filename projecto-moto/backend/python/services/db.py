import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Tu usuario de MySQL
            password="",  # Tu contraseña de MySQL
            database="VOLTDB"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar con MySQL", e)
        return None
