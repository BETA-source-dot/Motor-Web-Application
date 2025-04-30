from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, nombre, correo, contraseña, direccion, telefono, rol):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.direccion = direccion
        self.telefono = telefono
        self.rol = rol

    @staticmethod
    def get_by_id(user_id):
        from services.db import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        data = cursor.fetchone()
        connection.close()
        return Usuario(**data) if data else None

    @staticmethod
    def get_by_email(correo):
        from services.db import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        data = cursor.fetchone()
        connection.close()
        return Usuario(**data) if data else None

    @staticmethod
    def create(nombre, correo, contraseña):
        from services.db import get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)",
                       (nombre, correo, contraseña))
        connection.commit()
        connection.close()
