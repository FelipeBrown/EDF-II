

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

def filtrar_productos(precios, umbral, operacion='mayor'):
    
    productos_filtrados = []
    
    if operacion == 'mayor':
        productos_filtrados = [producto for producto, precio in precios.items() if precio > umbral]
    elif operacion == 'menor':
        productos_filtrados = [producto for producto, precio in precios.items() if precio < umbral]
    else:
        return "Lo sentimos, no es una operación válida"
    
    return ', '.join(productos_filtrados)

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        print("Los productos mayores al umbral son:", filtrar_productos(precios, umbral))
    elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        operacion = sys.argv[2]
        print("Los productos", operacion, "al umbral son:", filtrar_productos(precios, umbral, operacion))
    else:
        print("Por favor, ingrese el umbral y opcionalmente la operación (mayor o menor).")
