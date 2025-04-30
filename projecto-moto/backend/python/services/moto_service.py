import mysql.connector

def obtener_motos():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='VOLTDB'
    )

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombre, marca, modelo, precio, imagen_url FROM motos")
    resultados = cursor.fetchall()

    cursor.close()
    conexion.close()

    return [
        {
            'name': f"{fila['marca']} {fila['nombre']} {fila['modelo']}",
            'description': f"Marca: {fila['marca']} | Modelo: {fila['modelo']}",
            'price': fila['precio'],
            'image': fila['imagen_url']
        }
        for fila in resultados
    ]
