opcionesmenu1 = [
    "Seleccionar producto",
    "Mostrar carrito",
    "Pagar",
    "Panel de Administrador",
    "Salir",
]

opcionesmenu2 = [
    "Frios",
    "Carnes",
    "Bebidas",
    "Salir"
]
opcionesmenucarrito = [
    "Pagar",
    "Vaciar carrito",
    "Salir"
]
opcionesmenuadmin = [
    "Ver cantidad de ventas",
    "Agregar producto",
    "Editar producto",
    "Eliminar producto",
    "Salir",
]
opcionesmenuagregar = [
    "Agregar a Frios",
    "Agregar a Carnes",
    "Agregar a Bebidas",
    "Salir",
]
opcioneseditarproductos_f= [
    "Nombre",
    "Contenido",
    "Precio",
    "Salir",
]
opcionesmenueditar = [
    "Frios",
    "Carnes",
    "Bebidas",
    "Salir",
]
opcionesmenueliminar = [
    "Frios", 
    "Carnes", 
    "Bebidas", 
    "Salir"]

frios = {
        1: {"nombre": "Pizza Congelada", "contenido": ["queso", "masa", "tomate"], "precio": 20.0},
        2: {"nombre": "Ramen", "contenido": ["fideos tipo Spaghetti", "Salsa", "verduras"], "precio": 15.5},
        3: {"nombre": "Tarta", "contenido": ["tapa de hojaldre"], "precio": 30.0},
        4: {"nombre": "Ravioles", "contenido": ["ravioles, salsa roja/blanca, queso rallado"], "precio": 15.0},
        5: {"nombre": "Canelones", "contenido": ["panqueque, jamon, queso, acelga"], "precio": 20.0},
        }
carnes = {
        1: {"nombre": "Hamburguesa", "contenido": ["pan, carne, tomate, queso, lechuga, mayonesa/mostaza"], "tiempo": 10, "precio": 10.0},
        2: {"nombre": "Pancho", "contenido": ["pan, salchica, mayonesa/mostaza"], "tiempo": 5, "precio": 5.0},
        3: {"nombre": "Asado", "contenido": ["vacio/cerdo/pollo/costeleta/chorizo/falda, chinchulin, ensalada"], "tiempo": 60, "precio": 40.0},
}
bebidas = {
        1: {"nombre": "Coca Cola", "contenido": 1.5, "precio": 10.5},
        2: {"nombre": "Jugo de Naranja", "contenido": 1.5, "precio": 10.0},
        3: {"nombre": "Jugo de Manzana", "contenido": 1.5, "precio": 10.0},
        4: {"nombre": "Jugo de Pomelo", "contenido": 1.5, "precio": 10.0},
        5: {"nombre": "Jugo de Pera", "contenido": 1.5, "precio": 10.0},
        6: {"nombre": "Agua", "contenido": 1, "precio": 5.0},
        7: {"nombre": "Cerveza", "contenido": 1, "precio": 10.0},
        8: {"nombre": "Licuado", "contenido": 1, "precio": 15.0 },
        }

tarjetas = {
    1:{"numero": "4509 0303 4252 2345", "fondos": 1000.0},
    2:{"numero": "5334 4356 2321 5363", "fondos": 20000.0},
    3:{"numero": "3303 5524 4434 5223", "fondos": 5000.0},
    4:{"numero": "1234 3456 6789 2231", "fondos": 1500.0},
    5:{"numero": "4325 5646 5453 6567", "fondos": 12000.0},
}

carrito = []

password = "admin0000"

validar_mostrar_opciones = [1, 2, 3, 4, 5]
opciones_elegir_producto = [1, 2, 3, 4]
opciones_validas_carrito = [1, 2, 3]
opciones_validas_admin = [1, 2, 3, 4, 5]
opciones_validas_agregar = [1, 2, 3, 4]
opciones_validas_editar = [1, 2, 3, 4]
opciones_validas_eliminar = [1, 2, 3, 4]
opciones_validar_funcion_editar= [1, 2, 3]


