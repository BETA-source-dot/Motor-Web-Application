from .db import get_connection

def obtener_motos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT p.id, p.nombre, p.descripcion, p.precio, p.imagen_url
        FROM productos p
        JOIN categorias c ON p.categoria_id = c.id
        WHERE c.nombre = 'Motos';
    """

    cursor.execute(query)
    motos = cursor.fetchall()

    cursor.close()
    conn.close()

    return motos
