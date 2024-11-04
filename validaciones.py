import os

def validar_numero(numero):
    try:
        int(numero)
        return True
    except ValueError:
        print("Error, ingrese un numero entero")
        return False

def validar_opcion(opcion, opciones_validas):
    try:
        opcion = int(opcion)
        if opcion not in opciones_validas:
            raise ValueError(f"Opción inválida. Por favor, seleccione una de las siguientes opciones: {', '.join(map(str, opciones_validas))}.")
        return opcion
    except ValueError:
        raise ValueError("Opción inválida. Por favor, ingrese un número válido.")
    
def validar_entrada(nombre, contenido=None, precio=None):
    try:
        if not isinstance(nombre, str) or nombre.strip() == '':
            raise ValueError("El nombre del producto no es válido.")
        
        if contenido is not None:
            if isinstance(contenido, (str, float)):
                if isinstance(contenido, str):
                    contenido = contenido.strip()  
                    if contenido == '':
                        raise ValueError("El contenido no puede estar vacío.")
                    contenido = contenido.split(',')  
                    contenido = [item.strip() for item in contenido]  
            else:
                raise ValueError("El contenido debe ser una cadena de texto o un número decimal.")
        
        if precio is not None:
            if isinstance(precio, str):
                precio = precio.strip()  
                if precio == '':
                    raise ValueError("El precio no puede estar vacío.")
                precio = float(precio)  
        
        return nombre, contenido, precio
    
    except ValueError as e:
        raise ValueError("Error de validación:", str(e))
    
def limpieza():
    os.system('cls' if os.name == 'nt' else 'clear')