import mysql.connector
from werkzeug.security import generate_password_hash

# Configuración de la base de datos
db_config = {
    'host': 'localhost',  # Cambia esto si tu base de datos está en otro servidor
    'user': 'root',  # Cambia esto por tu usuario de base de datos
    'password': '',  # Cambia esto por tu contraseña de base de datos
    'database': 'VOLTDB'
}

# Conexión a la base de datos
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

def actualizar_contraseñas():
    # Establecer conexión con la base de datos
    connection = get_db_connection()
    cursor = connection.cursor()

    # Obtener todos los usuarios
    cursor.execute("SELECT id, contraseña FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        user_id = usuario[0]
        contraseña_plana = usuario[1]

        # Generar el hash de la contraseña
        contraseña_hash = generate_password_hash(contraseña_plana)

        # Actualizar la contraseña en la base de datos
        cursor.execute(
            "UPDATE usuarios SET contraseña = %s WHERE id = %s", 
            (contraseña_hash, user_id)
        )
        print(f"Contraseña de usuario con ID {user_id} actualizada.")

    # Guardar cambios y cerrar conexión
    connection.commit()
    cursor.close()
    connection.close()
    print("Proceso de actualización de contraseñas finalizado.")

if __name__ == "__main__":
    actualizar_contraseñas()
