"""
Lógica de apoyo a main
"""


def mostrar_menu():
    """
    Función para mostrar el menú
    """
    print("+-------------------------------------+")
    print("| 🏠 Presupuesto Familiar             |")
    print("+-------------------------------------+")
    print("| 1 - Añadir movimiento               |")
    print("| 2 - Filtar movimientos              |")
    print("| 3 - Total gastos                    |")
    print("| 4 - Total ingresos                  |")
    print("| 5 - Obtener balance                 |")
    print("| 6 - Eliminar movimiento             |")
    print("| 7 - Salir                           |")
    print("+-------------------------------------+\n")


def validar_opcion(msg_input: str, msg_error: str) -> int:
    """
    Funcion para verificar opcion de entrada

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Return:
        (int): opcion validada
    """
    while True:
        try:
            opcion = input(msg_input)
            opcion = int(opcion)
            break
        except ValueError:
            print(msg_error)
    return opcion


def leer_cadenas(msg_imput: str, msg_error: str) -> str:
    """
    Función para verifcar el texto en formato correcto.
    Sin espacios y que no sea una cadena vacía.

    Args:
        msg_imput (str): Mensaje de input.
        msg_error (str): mensaje de error.

    Returns:
        str: texto con formato correcto.
    """
    while True:
        texto = input(msg_imput).lower()
        try:
            if not texto.strip():
                raise ValueError(msg_error)
        except ValueError as e:
            print(f"❌ ERROR: {e}")
        else:
            break
    return texto


def validacion_dato(msg_input: str, msg_error_neg: str, msg_error: str, tipo_dato: type):
    """
    Función para validar datos

    Args:
        msg_input (str): Mensaje de input
        msg_error_neg (str): Mensaje de error, precio negativo.
        msg_error (str): Mensaje de error generico
        tipo_dato (_type_): Tipo de dato esperado.

    Returns:
        float: Dato con formato correcto de moneda
    """
    while True:
        dato = input(msg_input)
        try:
            dato = tipo_dato(dato)
            if dato < 0:
                print(msg_error_neg)
                continue
            break
        except ValueError:
            print(f"❌ ERROR: {msg_error}")
    return dato


def mostrar_movimientos(movimientos_filtrados: list, titulo: str):
    """
    Función para mostrar movimiento por categoria.

    Args:
        categoria (str): Categoria del movimiento.
        movimientos_filtrados (list): Lista de movimientos.
    """
    print("------------------------------------------------------")
    print(f"Movimientos de la categoria: {titulo.title()}")
    print("------------------------------------------------------")
    if not movimientos_filtrados:
        print(" ❌ No hay movimientos_filtrados que mostrar..")
    for movimiento in movimientos_filtrados:
        if movimiento['tipo'] == "Gasto":
            tipo_notacion = "Gasto 🔴"
        else:
            tipo_notacion = "Ingreso 🟢"
        print(f" 👉Movimiento ID: {movimiento['id']}")
        print(f" - Fecha: {movimiento['fecha']}")
        print(f" - Tipo: {tipo_notacion}")
        print(f" - Concepto: {movimiento['concepto']}.")
        print(f" - Categoria: {movimiento['categoria']}.")
        print(f" - Cantidad: {movimiento['cantidad']}")
        print("------------------------------------------------------")
        print("\n")


def mostrar_balance(balance: float):
    """
    Función para mostar balance

    Args:
        balance (float): Resultado del balance
    """
    if balance >= 0:
        print(f"💰 Balance Actual: {balance} € 🟢\n")
    else:
        print(f"💰 Balance Actual: {balance} € 🔴\n")


def validar_tipo_movimiento(msg_input: str, msg_error: str):
    """
    Función para validar tipo de notación
    Valores posibles
    - Gasto
    - Ingreso

    Args:
        msg_input (str): Mensaje del input
        msg_error (str): Mensaje de error
    """
    while True:
        tipo = input(msg_input).title()
        if tipo == "Gasto":
            return tipo
        elif tipo == "Ingreso":
            return tipo
        else:
            print(f"❌ ERROR: {msg_error}")


def validar_fecha(msg_input, msg_error) -> str:
    """
    Función para validar una fecha en formato:
    dd-mm-aaaa

    Args:
        msg_imput (_type_): Mensaje de input
        msg_error (_type_): Mensaje de error

    Returns:
        str: Cadena donde se almacena la fecha con formato indicado.
    """
    while True:
        fecha = input(msg_input).strip()
        # Comprobar formato básico
        if len(fecha) != 10 or fecha[2] != "-" or fecha[5] != "-":
            print(msg_error)
            continue
        dia, mes, anio = fecha.split("-")
        # Comprobar que sean números
        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            print(msg_error)
            continue
        dia = int(dia)
        mes = int(mes)
        anio = int(anio)
        # Comprobar mes válido
        if mes < 1 or mes > 12:
            print(msg_error)
            continue
        # Días por mes
        dias_mes = [31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]
        # Comprobar año bisiesto
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_mes[1] = 29  # Febrero
        # Comprobar día válido
        if dia < 1 or dia > dias_mes[mes - 1]:
            print(msg_error)
            continue
        return fecha
