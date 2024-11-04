from multiprocessing import Value
from datos import *
from validaciones import *
import time
from colorama import init, Fore, Back, Style

init()

def mostrar_opciones(opciones): #Funcion para mostrar las listas de opciones de los menus
    print(Fore.RED + Back.BLACK + "-----------------------------------------" + Style.RESET_ALL)
    for i, opcion in enumerate(opciones, start=1):
        print(Fore.YELLOW + f"{i})" + Fore.CYAN + f"{opcion}" + Style.RESET_ALL)
        time.sleep(0.5) 
    print(Fore.RED + Back.BLACK + "-----------------------------------------" + Style.RESET_ALL)

def agregar_carrito(producto, cantidad, precio): #Funcion para agregar productos al carrito y que se almacene en una lista
    carrito.append({"producto": producto, "cantidad": cantidad, "precio": precio})

def agregar_productos_comida(productos_diccionario): #Funcion para agregar un producto al diccionario Frios o Carnes
    ultimo_indice = max(productos_diccionario.keys())
    nuevo_indice = ultimo_indice + 1
    while True:
        try:
            nombre = str(input(Fore.BLACK + Back.WHITE + "Ingrese el nombre del producto que quiere agregar: " + Style.RESET_ALL)).strip()
            contenido = str(input(Fore.BLACK + Back.WHITE + "Ingrese el contenido del producto (separe los ingredientes por comas): " + Style.RESET_ALL)).strip()
            precio = float(input(Fore.BLACK + Back.WHITE + "Ingrese su precio: " + Style.RESET_ALL))
            
            nombre, contenido, precio = validar_entrada(nombre, contenido, precio)
            
            productos_diccionario[nuevo_indice] = {'nombre': nombre, 'contenido': contenido, 'precio': precio}
            print(Fore.YELLOW + Back.BLACK + "Producto agregado: " + Fore.GREEN + f"{nombre} - " + Fore.YELLOW + "Ingredientes/Contenido: " + Fore.GREEN + f"{', '.join(contenido)} - " + Fore.YELLOW + "Precio: " + Fore.GREEN + f"{precio:.2f}" + Style.RESET_ALL)


            while True:
                opcion = input(Fore.BLACK + Back.WHITE + "¿Desea ver la lista actualizada? Si/No: " + Style.RESET_ALL).strip().lower()
                if opcion == "si":
                    for key, value in productos_diccionario.items():
                        print(Fore.YELLOW + Back.BLACK + f"{key}:" + Fore.GREEN + f"{value['nombre']} - {', '.join(value['contenido'])} - ${value['precio']}" + Style.RESET_ALL)
                    return productos_diccionario
                elif opcion == "no":
                    return productos_diccionario
                else:
                    print(Fore.BLACK + Back.RED + "Opción inválida. Por favor, ingrese " + Fore.YELLOW + "'Si' o 'No'." + Style.RESET_ALL)

        except Exception as ve:
            print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}." + Fore.BLACK + " Por favor, ingrese los datos nuevamente." + Style.RESET_ALL)


def agregar_productos_bebida(productos_diccionario): #Funcion para agregar un producto al diccionario Bebidas
        ultimo_indice = max(productos_diccionario.keys())
        nuevo_indice = ultimo_indice + 1
        while True:
            try:
                nombre = str(input(Fore.BLACK + Back.WHITE + "Ingrese el nombre del producto que quiere agregar: " + Style.RESET_ALL)).strip()
                contenido = float(input(Fore.BLACK + Back.WHITE + "Ingrese el contenido del producto: " + Style.RESET_ALL))
                precio = float(input(Fore.BLACK + Back.WHITE + "Ingrese su precio: " + Style.RESET_ALL))
                nombre, contenido, precio = validar_entrada(nombre, contenido, precio)
                productos_diccionario[nuevo_indice] = {'nombre': nombre, 'contenido': contenido, "precio": precio}
                print(Fore.YELLOW + Back.BLACK + "Producto agregado: " + Fore.GREEN + f"{nombre} - " + Fore.YELLOW + "Ingredientes/Contenido: " + Fore.GREEN + f"Contenido: {contenido}L - " + Fore.YELLOW + "Precio: " + Fore.GREEN + f"{precio:.2f}" + Style.RESET_ALL)
                while True:
                    opcion = input(Fore.BLACK + Back.WHITE + "Desea ver la lista actualizada? " + Fore.YELLOW + "Si/No: " + Style.RESET_ALL).strip().lower()
                    if opcion == "si":
                        for key, value in productos_diccionario.items():
                            print(Fore.YELLOW + Back.BLACK + f"{key}:"+ Fore.GREEN +f"{value['nombre']} - {value['contenido']}L - ${value['precio']}" + Style.RESET_ALL)
                        return productos_diccionario
                    elif opcion == "no":
                        return productos_diccionario
                    else:
                        print(Fore.BLACK + Back.RED + "Opción inválida. Por favor, ingrese " + Fore.BLUE + "'Si' o 'No'." + Style.RESET_ALL)
            
            except Exception as ve:
                print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}." + Fore.BLACK + " Por favor, ingrese los datos nuevamente." + Style.RESET_ALL)
                
def editar_productos(productos_diccionario, categoria): #Funcion para editar los productos de un diccionario
    print(Fore.BLACK + Back.WHITE + "Productos en la categoría " + Fore.BLUE + f"{categoria}:" + Style.RESET_ALL)
    for key, value in productos_diccionario.items():
        print(Fore.YELLOW + Back.BLACK + f"{key}:" + Fore.GREEN + f"{value['nombre']} - {value['contenido']} - ${value['precio']}" + Style.RESET_ALL)
    
    nombre_producto = int(input(Fore.BLACK + Back.WHITE + "Ingrese el número del producto que desea editar en la categoría " + Fore.BLUE + f"{categoria}: " + Style.RESET_ALL))
    
    for key, producto in productos_diccionario.items():
        if key == nombre_producto:
            print(Fore.GREEN + Back.BLACK + "Producto encontrado:" + Style.RESET_ALL)
            print(Fore.YELLOW + Back.BLACK + "Nombre actual: " + Fore.GREEN + f"{producto['nombre']}" + Style.RESET_ALL)
            print(Fore.YELLOW + Back.BLACK + "Contenido actual: " + Fore.GREEN + f"{producto['contenido']}" + Style.RESET_ALL) 
            print(Fore.YELLOW + Back.BLACK + "Precio actual: " + Fore.GREEN + f"{producto['precio']}" + Style.RESET_ALL)
            print(Fore.BLACK + Back.WHITE + "¿Qué desea editar?" + Style.RESET_ALL)
            mostrar_opciones(opcioneseditarproductos_f)
            opcion = input(Fore.BLACK + Back.WHITE + "Ingrese la opción que desea editar: " + Style.RESET_ALL)
            
            try:
                opcion = validar_opcion(opcion, opciones_validar_funcion_editar)
                if opcion == 1:
                    nombre = input(Fore.BLACK + Back.WHITE + "Ingrese el nuevo nombre del producto (presione Enter para mantener el actual): " + Style.RESET_ALL)
                    if nombre:
                        producto["nombre"] = nombre
                elif opcion == 2:
                    contenido = input(Fore.BLACK + Back.WHITE + "Ingrese el nuevo contenido del producto (separe los ingredientes por comas, presione Enter para mantener el actual): " + Style.RESET_ALL)
                    if categoria == "Bebidas":
                        contenido_float = float(contenido)
                        if contenido:
                            nombre, contenido_float, precio = validar_entrada(producto['nombre'], contenido_float, producto['precio'])
                            producto["contenido"] = contenido_float
                    elif categoria == "Frios" or categoria == "Carnes":
                        contenido_str = str(contenido)
                        if contenido:
                            nombre, contenido_str, precio = validar_entrada(producto['nombre'], contenido_str, producto['precio'])
                            producto["contenido"] = contenido_str
                elif opcion == 3:
                    menu_interactivo = True
                    while menu_interactivo:
                        try:
                            precio_nuevo = input(Fore.BLACK + Back.WHITE + "Ingrese el nuevo precio del producto (presione Enter para mantener el actual): " + Style.RESET_ALL)
                            if not precio_nuevo:
                                menu_interactivo = False

                            precio_nuevo = float(precio_nuevo)
                            producto["precio"] = precio_nuevo
                            menu_interactivo = False
                        except ValueError:
                            print(Fore.RED + Back.BLACK + "Error: El precio debe ser un número decimal. Por favor, ingrese el precio nuevamente." + Style.RESET_ALL)

                print(Fore.GREEN + Back.BLACK + "Producto " + Fore.MAGENTA + f"{nombre_producto}" + Fore.GREEN + " editado con éxito!" + Style.RESET_ALL)
                
                while True:
                    opcion = input(Fore.BLACK + Back.WHITE + "¿Desea ver la lista actualizada? " + Fore.BLUE + "Si/No: ").lower()
                    if opcion == "si":
                        for key, value in productos_diccionario.items():
                            print(Fore.YELLOW + Back.BLACK + f"{key}:" + Fore.GREEN + f"{value['nombre']} - {value['contenido']} - ${value['precio']}" + Style.RESET_ALL)
                        return productos_diccionario
                    elif opcion == "no":
                        return productos_diccionario
                    else:
                        print(Fore.BLACK + Back.RED + "Opción inválida. Por favor, ingrese " + Fore.YELLOW + "'Si' o 'No'." + Style.RESET_ALL)
            
            except Exception as ve:
                print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}." + Fore.BLACK + " Por favor, ingrese los datos nuevamente." + Style.RESET_ALL)

    print(Fore.RED + Back.BLACK + "No se encontró el producto con número " + Fore.YELLOW + f"{nombre_producto}" + Fore.RED + " en la categoría " + Fore.YELLOW + f"{categoria}" + Style.RESET_ALL)
    return productos_diccionario

def eliminar_producto(productos_diccionario, categoria): #Funcion para eliminar un producto de un diccionario
    try:
        menu_interactivo = True
        while menu_interactivo:
            mostrar_menu(productos_diccionario)
            producto_d_id = int(input(Fore.BLACK + Back.WHITE + "Seleccione el producto que desea eliminar de " + Fore.BLUE + f"{categoria}: " + Style.RESET_ALL))
            if producto_d_id in productos_diccionario:
                del productos_diccionario[producto_d_id]
                print(Fore.GREEN + Back.BLACK + "Producto eliminado correctamente de " + Fore.BLUE + f"{categoria}" + Style.RESET_ALL)
                menu_interactivo = False
            else:
                print(Fore.RED + Back.BLACK + "No se encontró el producto " + Fore.YELLOW + f"{producto_d_id}" + Fore.RED + " en " + Fore.YELLOW + f"{categoria}" + Style.RESET_ALL)
                continuar()
                    
        while True:
            opcion = input(Fore.BLACK + Back.WHITE + "¿Desea ver la lista actualizada? " + Fore.BLUE + "Si/No: ").lower()
            if opcion == "si":
                for key, value in productos_diccionario.items():
                    print(Fore.YELLOW + Back.BLACK + f"{key}:" + Fore.GREEN + f"{value['nombre']} - {value['contenido']} - ${value['precio']}" + Style.RESET_ALL)
                return productos_diccionario
            elif opcion == "no":
                return productos_diccionario
            else:
                print(Fore.BLACK + Back.RED + "Opción inválida. Por favor, ingrese " + Fore.YELLOW + "'Si' o 'No'." + Style.RESET_ALL)

    except Exception as ve:
        print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}." + Fore.BLACK + " Por favor, ingrese los datos nuevamente." + Style.RESET_ALL)

def calcular_costo_total(): #Funcion para calcular el costo total de los productos en carrito
    costo_total = 0
    for item in carrito:
        costo_total += item['cantidad'] * item['precio']
    return costo_total

def mostrar_carrito(): #Funcion para mostrar el contenido de la lista carrito
    print(Fore.RED + Back.BLACK + "-----------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA + Back.BLACK + "Carrito: " + Style.RESET_ALL)
    for item in carrito:
        print(Fore.GREEN+ f"{item['cantidad']} x {item['producto']} - ${item['precio']}" + Style.RESET_ALL)
        time.sleep(0.5) 
    print(Fore.GREEN + Back.BLACK + "Costo total: " + Fore.YELLOW + f"${calcular_costo_total()}" + Style.RESET_ALL)

def continuar(): #Funcion para elegir si continuar o no un ciclo while
    try:
        while True:
            respuesta = input(Fore.BLACK + Back.WHITE + "¿Desea continuar? " + Fore.BLUE + "(Si/No): " + Style.RESET_ALL)
            if respuesta.lower() == "si":
                return True
            elif respuesta.lower() == "no":
                return False
            else:
                print(Fore.BLACK + Back.RED + "Ingrese una respuesta válida " + Fore.YELLOW + "(Si/No)" + Style.RESET_ALL)
    except Exception as ve:
        print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}."+ Style.RESET_ALL)

def contador_carrito(menu, producto_id): #Funcion para agregar cierta cantidad de productos al carrito
        salir = True
        while salir:
            try:
                cantidad = int(input(Fore.BLACK + Back.WHITE + "Ingrese la cantidad que quiere llevar: " + Style.RESET_ALL))
                if validar_numero(cantidad):
                    producto = menu[producto_id]["nombre"]
                    precio = menu[producto_id]["precio"]
                    agregar_carrito(producto, cantidad, precio)
                    print(Fore.GREEN + Back.BLACK + "Agregado correctamente, usted tiene: " + Fore.BLUE +f"{cantidad}" + Fore.GREEN + " unidades de " + Fore.BLUE +  f"{producto}" + Fore.GREEN + " en su carrito" + Style.RESET_ALL)
                    salir = False
                else:
                    print(Fore.RED + Back.BLACK + "Opcion Invalida" + Style.RESET_ALL)
            except ValueError as ve:
                print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}."+ Style.RESET_ALL)
                continue

def vaciar_carrito():
    global carrito
    carrito = []
    return print(Fore.GREEN + Back.BLACK + "Carrito vaciado correctamente" + Style.RESET_ALL)
          
def mostrar_menu(opciones): #Funcion para mostrar los diccionarios
    if opciones is None:
        print(Fore.RED + Back.BLACK + "No hay opciones disponibles" + Style.RESET_ALL)
        return   
    print(Fore.RED + Back.BLACK + "-----------------------------------------" + Style.RESET_ALL)
    for key, value in opciones.items():
        print(Fore.YELLOW + Back.BLACK + f"{key}: " + Fore.GREEN + f"{value['nombre']} - ${value['precio']}" + Style.RESET_ALL)
        time.sleep(0.5) 
    print(Fore.RED + Back.BLACK + "-----------------------------------------" + Style.RESET_ALL)

class Tarjeta(): #Clase para manejar las tarjetas
    def __init__(self, tarjeta, fondo) -> None:
        self.tarjeta = tarjeta
        self.fondo = fondo

class Pago:
    def __init__(self, nombreusuario, pagar, total_dinero): #Clase para manejar el pago del carrito
        self.nombre = nombreusuario
        self.pagar = pagar
        self.total_dinero = total_dinero
    
    def pay(self):
        try: 
            costo_total = 0
            for item in carrito:
                costo_total += item['cantidad'] * item['precio']
            payflag = True
            while payflag:
                tarjeta_credito = input(Fore.BLACK + Back.WHITE + "Por favor, ingrese el número de su tarjeta de crédito: " + Style.RESET_ALL)
                if any(tarjeta_credito == tarjeta["numero"] for tarjeta in tarjetas.values()):
                    saldo_disponible = next(tarjeta["fondos"] for tarjeta in tarjetas.values() if tarjeta["numero"] == tarjeta_credito)
                    if saldo_disponible >= costo_total:
                        for tarjeta in tarjetas.values():
                            if tarjeta["numero"] == tarjeta_credito:
                                tarjeta["fondos"] -= costo_total
                        self.pagar = "yes"
                        payflag = False
                    else:
                        print(Fore.RED + Back.BLACK + "Fondos insuficientes" + Style.RESET_ALL)
                else:
                    print(Fore.BLACK + Back.RED + "Numero de tarjeta no valido, intentelo denuevo" + Style.RESET_ALL)
        except Exception as ve:
            print(Fore.BLACK + Back.RED + "Error: " + Fore.YELLOW + f"{ve}."+ Style.RESET_ALL)

    def status(self): #Funcion para saber si se realizo el pago
        try:
            if self.pagar == "yes":
                global carrito
                carrito = []
                return print(Fore.GREEN + Back.BLACK + f"{self.nombre} ha pagado $" + Fore.YELLOW + f"{self.total_dinero}" + Style.RESET_ALL)
            else:
                return print(Fore.RED + Back.BLACK + f"No ha pagado el total de: $" + Fore.YELLOW + f"{self.total_dinero}" + Style.RESET_ALL)
        except Exception as ve:
            print(Fore.BLACK + Back.RED + "Error: " + Fore.BLUE + f"{ve}."+ Style.RESET_ALL)
            

tickets = 0
def tickets_contador(): #Funcion para aumentar en 1 los tickets al vender
    global tickets
    tickets += 1

recaudacion = []
def total_recaudado(costo_total):
    global recaudacion
    recaudacion.append(costo_total)
    recaudacion = [sum(recaudacion)]

def pago_realizado(nombre): #Funcion para realizar un pago
    nombre_cliente = nombre 
    costo_total = calcular_costo_total()
    nombreusuario = Pago(nombre_cliente, "no", calcular_costo_total()) 
    nombreusuario.pay() 
    nombreusuario.status() 
    tickets_contador()
    total_recaudado(costo_total)

def tickets_mostrar(): #Funcion para mostrar la cantidad de tickets que se tiene
    print(Fore.BLACK + Back.WHITE + "Usted tiene "+ Fore.BLUE + f"{tickets}" + Fore.BLACK +" tickets"+ Style.RESET_ALL)
    print(Fore.BLACK + Back.WHITE + "Total recaudado: $" + Fore.YELLOW + f"{sum(recaudacion):.2f}" + Style.RESET_ALL)