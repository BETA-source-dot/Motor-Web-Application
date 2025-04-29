import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",      # cambia por tu usuario
        password="",  # cambia por tu contraseña
        database="VOLTDB"  # cambia por el nombre de la base de datos
    )
    return connection
