from datos import *
from func import *
from validaciones import *
from colorama import init, Fore, Back, Style
import time
init()

menuprincipal = True
nombreusuario = str(input(Fore.BLACK + Back.WHITE + "Ingrese su nombre de usuario: " + Style.RESET_ALL))
while not nombreusuario.strip():  
    print(Fore.BLACK + Back.RED + "Debe ingresar un nombre de usuario válido" + Style.RESET_ALL)
    nombreusuario = str(input(Fore.BLACK + Back.WHITE + "Ingrese su nombre de usuario: " + Style.RESET_ALL))
time.sleep(0.5)

while menuprincipal:
    try: 
        print(Fore.RED + Back.BLACK + "-----------------------------------------")
        print(Fore.MAGENTA + Back.BLACK + "Bienvenido " + Fore.GREEN + nombreusuario.strip() + Fore.MAGENTA + ", que desea hacer hoy?:" + Style.RESET_ALL)
        time.sleep(0.5)
        mostrar_opciones(opcionesmenu1)
        opcion = int(input(Fore.BLACK + Back.WHITE + "Elija una opción: " + Style.RESET_ALL))
        opcion = validar_opcion(opcion, validar_mostrar_opciones)
        if opcion == 1: #Seleccionar para llevar
            menu_interactivo = True
            while menu_interactivo:
                try:
                    mostrar_opciones(opcionesmenu2)
                    elegir_producto = int(input(Fore.BLACK + Back.WHITE + "Elija que producto quiere ver: " + Style.RESET_ALL))
                    elegir_producto = validar_opcion(elegir_producto, opciones_elegir_producto)
                    if elegir_producto == 1: #Menu Frios
                        mostrar_menu(frios)
                        producto_id = int(input(Fore.BLACK + Back.WHITE + "Selecciona qué quiere llevar" + Fore.YELLOW + Back.BLACK + "(1, 2, 3, etc.): " + Style.RESET_ALL))
                        if producto_id in frios:
                            contador_carrito(frios, producto_id)
                            if not continuar():
                                menu_interactivo = False
                    elif elegir_producto == 2: #Menu Carnes
                        mostrar_menu(carnes)
                        producto_id = int(input(Fore.BLACK + Back.WHITE + "Selecciona qué quiere llevar" + Fore.YELLOW + Back.BLACK + "(1, 2, 3, etc.): " + Style.RESET_ALL))
                        if producto_id in carnes:
                            contador_carrito(carnes, producto_id)
                            if not continuar():
                                menu_interactivo = False
                    elif elegir_producto == 3: #Menu Bebidas
                        mostrar_menu(bebidas)
                        producto_id = int(input(Fore.BLACK + Back.WHITE + "Selecciona qué quiere llevar"  + Fore.YELLOW + Back.BLACK + "(1, 2, 3, etc.): " + Style.RESET_ALL))
                        if producto_id in bebidas:
                            contador_carrito(bebidas, producto_id)
                            if not continuar():
                                menu_interactivo = False
                    elif elegir_producto == 4: #Salir
                        menu_interactivo = False
                except ValueError:
                    print(Fore.BLACK + Back.RED + "Ingrese un numero valido" + Style.RESET_ALL)
        elif opcion == 2: #Mostrar Carrito
            salir_carrito = True
            while salir_carrito:
                mostrar_carrito()
                mostrar_opciones(opcionesmenucarrito)
                opcion_carrito = str(input(Fore.MAGENTA + Back.BLACK + "Ingrese una opcion: "+ Style.RESET_ALL))
                opcion_carrito = validar_opcion(opcion_carrito, opciones_validas_carrito)
                if opcion_carrito == 1: #Pagar Ahora
                    pagar = str(input(Fore.BLACK + Back.WHITE + "Desea pagar ahora?:" + Fore.YELLOW + Back.BLACK + "Si/No: " + Style.RESET_ALL)).lower()
                    if pagar == "si":
                        if calcular_costo_total() == 0: #Chequear que el carrito no este vacio
                            print(Fore.RED + Back.BLACK + "El carrito esta vacio" + Style.RESET_ALL)
                            salir_carrito = False
                        elif calcular_costo_total() > 0: #Carrito no vacio
                            pago_realizado(nombreusuario)
                            if not continuar():
                                limpieza()
                                menuprincipal = False
                            salir_carrito = False
                    elif pagar == "no":
                        salir_carrito = False
                    else:
                        print(Fore.BLACK + Back.RED + "Ingrese una opcion valida" + Style.RESET_ALL)  
                elif opcion_carrito == 2: #Vaciar Carrito
                    vaciar_carrito()
                    salir_carrito = False
                elif opcion_carrito == 3: #Salir
                    salir_carrito = False
                else:
                    print(Fore.BLACK + Back.RED + "Ingrese una opcion valida" + Style.RESET_ALL)           
        elif opcion == 3: #Pagar Carrito
            pago_realizado(nombreusuario)
            if not continuar():
                limpieza()
                menuprincipal = False
        elif opcion == 4: #Menu Administrador
            contraseña = str(input(Fore.BLACK + Back.WHITE +"Ingrese su contraseña para continuar: " + Style.RESET_ALL))
            salir = True
            while salir:
                if contraseña == password:
                    print(Fore.MAGENTA + Back.BLACK + "Bienvenido al panel de administrador, que desea?: " + Style.RESET_ALL)
                    mostrar_opciones(opcionesmenuadmin)
                    opcionadmin = int(input(Fore.BLACK + Back.WHITE + "Ingrese una opcion: " + Style.RESET_ALL))
                    opcionadmin = validar_opcion(opcionadmin, opciones_validas_admin)
                    if opcionadmin == 1: #Ver cantidad de tickets entregados
                        tickets_mostrar()
                        if not continuar():
                            salir = False
                    elif opcionadmin == 2: #Agregar producto a diccionario
                        mostrar_opciones(opcionesmenuagregar)
                        opcionagregar = int(input(Fore.BLACK + Back.WHITE + "Elija una opcion: " + Style.RESET_ALL))
                        opcionagregar = validar_opcion(opcionagregar, opciones_validas_agregar)
                        salir_agregar = True
                        while salir_agregar:
                            if opcionagregar == 1: #Agregar Frios
                                frios = agregar_productos_comida(frios)
                                if not continuar():
                                    salir_agregar = False
                            elif opcionagregar == 2: #Agregar Carnes
                                carnes = agregar_productos_comida(carnes)
                                if not continuar():
                                    salir_agregar = False
                            elif opcionagregar == 3: #Agregar Bebidas
                                bebidas = agregar_productos_bebida(bebidas)
                                if not continuar():
                                    salir_agregar = False
                            elif opcionagregar == 4: #Salir
                                salir_agregar = False
                    elif opcionadmin == 3: #Editar producto
                        mostrar_opciones(opcionesmenueditar)
                        opcioneditar = int(input(Fore.BLACK + Back.WHITE + "Elija donde se encuentra el producto que quiere editar: " + Style.RESET_ALL))
                        opcioneditar = validar_opcion(opcioneditar, opciones_validas_editar)
                        salir_editar = True
                        while salir_editar:
                            if opcioneditar == 1: #Editar Frios
                                editar_productos(frios, "Frios")
                                if not continuar():
                                    salir_editar = False
                            elif opcioneditar == 2: #Editar Carnes
                                editar_productos(carnes, "Carnes")
                                if not continuar():
                                    salir_editar = False
                            elif opcioneditar == 3: #Editar Bebidas
                                editar_productos(bebidas, "Bebidas")
                                if not continuar(): 
                                    salir_editar = False
                            elif opcioneditar == 4: #Salir
                                salir_editar = False
                    elif opcionadmin == 4: #Eliminar producto
                        mostrar_opciones(opcionesmenueliminar)
                        opcioneliminar = int(input(Fore.BLACK + Back.WHITE + "Elija donde se encuentra el producto que quiere eliminar: " + Style.RESET_ALL))
                        opcioneliminar = validar_opcion(opcioneliminar, opciones_validas_eliminar)
                        salir_eliminar = True
                        while salir_eliminar:
                            if opcioneliminar == 1: #Eliminar Frios
                                eliminar_producto(frios, "Frios")
                                if not continuar():
                                    salir_eliminar = False
                            elif opcioneliminar == 2: #Eliminar Carnes
                                eliminar_producto(carnes, "Carnes")
                                if not continuar():
                                    salir_eliminar = False
                            elif opcioneliminar == 3: #Eliminar Bebidas
                                eliminar_producto(bebidas, "Bebidas")
                                if not continuar():
                                    salir_eliminar = False
                            elif opcioneliminar == 4: #Salir
                                salir_eliminar = False
                    elif opcionadmin == 5: #Salir
                        salir = False
                    else:
                        print(Fore.BLACK + Back.RED + "Opcion Invalida" + Style.RESET_ALL)
                elif contraseña != password:
                    print(Fore.RED + "Contraseña incorrecta, intente de nuevo" + Style.RESET_ALL)
                    salir = False
        elif opcion == 5: #Salir
            print(Fore.RED + Back.BLACK + "Saliendo..." + Style.RESET_ALL)
            time.sleep(1)
            limpieza()
            menuprincipal = False
    except Exception as ve:
        print(Fore.BLACK + Back.RED + "Error: " + Fore.BLUE + f"{ve}."+ Style.RESET_ALL)