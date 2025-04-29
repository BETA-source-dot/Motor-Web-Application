from backend.python.services.product_service import obtener_motos

motos = obtener_motos()

for moto in motos:
    print(f"{moto['nombre']} - ${moto['precio']} - {moto['descripcion']}")
