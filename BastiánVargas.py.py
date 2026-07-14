#ET

#PetMarket

productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
} 

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}


def Agregar_producto(
        productos, stock,
        codigo, nombre, 
        categoria, marca, 
        peso_kg, es_importado, es_para_cachorro, 
        precio, unidades
):
    if buscar_codigo(stock, codigo):
        return False
    else:
        productos[codigo] = [nombre, categoria, marca, float(peso_kg), es_importado == "S", es_para_cachorro == "S"]
        stock[codigo] = [int(precio), int(unidades)]
        return True



def Validar_unidades(unidades):
    try:
        return int(unidades) > 0
    except ValueError:
        return False

def Validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def Validar_cachorro(es_para_cachorro):
    opciones = ["S", "N"]
    return es_para_cachorro in opciones

def Validar_importado(es_importado):
    opciones = ["S", "N"]
    return es_importado in opciones

def Validar_peso(peso_kg):
    try:
        return float(peso_kg) > 0
    except ValueError:
        return False

def Validar_texto(dato):
    return dato.strip() != ""



def eliminar_producto(productos, stock, codigo):
    if buscar_codigo(stock, codigo):
        productos.pop(codigo)
        stock.pop(codigo)
        return True
    else:
        return False


def Actualizar_precio(stock, codigo, nuevo_precio):
    if buscar_codigo(stock, codigo):
        stock[codigo][0] = nuevo_precio
        return True

    return False


def buscar_codigo(stock, codigo):
    for cod in stock.keys():
        if cod == codigo:
            return True
    return False


def busqueda_precio(stock, productos, p_min, p_max):
    resultados = []

    for codigo, dato in stock.items():
        precio = dato[0]
        unidades = dato[1]

        if precio >= p_min and precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            resultados.append(f"{nombre} -- {codigo}")
    for producto in resultados:
        print("===========")
        print(producto)
        print("===========")



def unidades_categoria(stock, productos, categoria):
    total = 0
    for codigo, dato in productos.items():
        if dato[1].upper() == categoria.upper():
            total += stock[codigo][1]
    print(f"La cantidad de unidades de/del {categoria} es de {total}")



def Leer_opc():
    while True:
        opc = int(input(":"))
        if 1 <= opc <= 7:
            return opc
        print("Debe seleccionar una opción válida")

def Mostrar_menu():
    Bucle_menu = True
    while Bucle_menu:
        try:
            print("""========== MENÚ PRINCIPAL ==========
1. Unidades por categoría
2. Búsqueda de productos por rango de precio
3. Actualizar precio de producto
4. Agregar producto
5. Eliminar producto
6. Salir
=====================================
""")
            print("Ingrese una opción: ")
            opcion = Leer_opc()
            match opcion:
                case 1:
                    print("Ingrese el nombre de una categoría: ")
                    categoria = input(":").upper()
                    unidades_categoria(stock, productos, categoria)
                case 2:
                    ingreso_invalido = True
                    while ingreso_invalido:
                        try:
                            print("Ingrese el precio minimo")
                            p_min = int(input(":"))
                            print("Ingrese el precio máximo")
                            p_max = int(input(":"))
                            ingreso_invalido = False

                        except ValueError:
                            print("Debe ingresar valores enteros")
                    busqueda_precio(stock, productos, p_min, p_max)
                case 3:
                    Actualizar = True
                    while Actualizar:
                        print("Ingrese el código del producto: ")
                        codigo = input(":").upper()
                        print("Ingrese el nuevo precio")
                        nuevo_precio = int(input(":"))
                        if Actualizar_precio(stock, codigo, nuevo_precio):
                            print("Precio actualizado con éxito")
                        else:
                            print("El código no existe")
                        resultado_invalido = True
                        while resultado_invalido:
                            print("¿Desea actualizar otro precio (s/n)?")
                            respuesta = input(":").lower()
                            if respuesta == "s":
                                resultado_invalido = False
                            elif respuesta == "n":
                                resultado_invalido = False
                                Actualizar = False
                            else:
                                print("Respuesta invalida, intente de nuevo")
                case 4:
                    print()
                    codigo = input("Ingrese el codigo del producto: ").upper()
                    nombre = input("Ingrese el nombre del producto: ").upper()
                    categoria = input("Ingrese el categoria del producto: ").upper()
                    marca = input("Ingrese la marca del producto: ").upper()
                    peso_kg = input("Ingrese el peso en kg del producto: ").upper()
                    es_importado = input("¿El producto es importado? (s/n): ").upper()
                    es_para_cachorro = input("¿El producto es para cachorros?(s/n): ").upper()
                    precio = input("Ingrese el precio del producto: ").upper()
                    unidades = input("Ingrese las unidades del producto: ").upper()

                    if not Validar_texto(codigo):
                        print("El codigo no puede estar vacío ni ser solo espacios en blancos")
                    if buscar_codigo(stock, codigo):
                        print("El codigo ya existe")
                    elif not Validar_texto(nombre):
                        print("El nombre no puede estar vacío ni ser solo espacios en blancos")
                    elif not Validar_texto(categoria):
                        print("La categoría no puede estar vacía ni ser solo espacios en blancos")
                    elif not Validar_texto(marca):
                        print("La categoría no puede estar vacía ni ser solo espacios en blancos")
                    elif not Validar_peso(peso_kg):
                        print("el peso de ser un numero decimal mayor a cero")
                    elif not Validar_importado(es_importado):
                        print("Solo puede ingresar 's' o 'n'")
                    elif not Validar_cachorro(es_para_cachorro):
                        print("Solo puede ingresar 's' o 'n'")
                    elif not Validar_precio(precio):
                        print("El precio debe ser un numero entero mayor a cero")
                    elif not Validar_unidades(unidades):
                        print("Las unidades deben ser un numero entero mayor a cero")
                    else:
                        if Agregar_producto(
                            productos, stock,
                            codigo, nombre, 
                            categoria, marca, 
                            peso_kg, es_importado, es_para_cachorro, 
                            precio, unidades,
                        ):
                            print("Producto agregado con éxito")
                        else:
                            print("El código ya existe")

                case 5:
                    print("Ingrese el código del producto que desea eliminar: ")
                    codigo = input(":").upper()
                    if eliminar_producto(productos, stock, codigo):
                        print("Producto eliminado con éxito")
                    else:
                        print("El código no existe")
                case 6:
                    print("Programa finalizado")
                    Bucle_menu = False
                case _:
                    print("Debe seleccionar una opción válida")
                    


        except ValueError:
            print("Debe seleccionar una opción válida")


Mostrar_menu()
