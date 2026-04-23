"""
Lógica funcional del proyecto de home budget (Presupuesto familiar)
"""


def registrar_movimiento(
        lista_movimientos: list, fecha: str, tipo: str,
        concepto: str, categoria: str, cantidad: float):
    """
    Función para generar un movimiento, agregara un diccionario con la estructura:
    - id(int): Identificador único incremental
    - fecha(str): Fecha de movimiento
    - tipo(str): Tipo de movimiento(Ingreso, Gasto)
    - concepto(str): Descripción del movimiento
    - categoria(str):Etiqueta de clasificación("Sueldo", "Ocio", "Vivienda"..).
    - cantidad(float): Valor monetario.
    A la lista de movimientos.

    Args:
        lista_movimientos (list): Lista donde se almacenan los movimientos.
        concepto (str): Descripción del movimiento
        categoria (str): Etiqueta de clasificación.
        cantidad (float): Cantidad monetaria.
    """
    # Si no hay movimientos
    if not lista_movimientos:
        # Establecemos el primer ID
        id_mov = 1
    # Si hay movimientos
    else:
        # recorremos toda la lista buscando el id más alta y sumamos uno
        id_mov = max(movimiento['id'] for movimiento in lista_movimientos)+1
    # Generamos el diccionario movimiento
    movimiento = {
        "id": id_mov,
        "fecha": fecha,
        "tipo": tipo,
        "concepto": concepto,
        "categoria": categoria.lower(),
        "cantidad": cantidad
    }
    # añadimos el diccionario a la lista
    lista_movimientos.append(movimiento)


def obtener_ingresos_gastos(lista_movimientos: list) -> dict:
    """
    Función para obtener la suma de los gastos según el tipo

    Args:
        lista_movimientos (list): Lista de movimientos

    Returns:
        dict: Diccionario con la estructura:
        {
            "ingresos":ingresos,
            "gastos":gastos
        }
    """
    gasto = 0
    ingreso = 0
    for movimiento in lista_movimientos:
        if movimiento['tipo'] == "Ingreso":
            ingreso += movimiento['cantidad']
        else:
            gasto += movimiento['cantidad']
    ingresos_gastos = {
        "ingresos": ingreso,
        "gastos": gasto
    }
    return ingresos_gastos


def obtener_balance(ingresos_gastos: dict) -> float:
    """
    Función para obtener el balance desde la lista de movimentos, se calculará
    con la diferencia de valores del diccionario ingresos_gastos, obtenido en la
    función obtner_ingresos_gastos()

    Args:
        ingresos_gastos (dict): Diccionario donde se almacenan la suma de los
        ingresos y los gastos.
        Estructura:
        {
            "ingresos":ingresos,
            "gastos":gastos
        }

    Returns:
        float: Diferencia de las entradas menos las salidas.
    """
    balance = ingresos_gastos['ingresos'] - ingresos_gastos['gastos']
    return round(balance, 2)


def filtar_por_categoria(lista_movimientos: list, categoria: str) -> list:
    """
    Función para listar todos los movimiento de una misma categoría

    Args:
        lista_movimientos (list): Lsita donde se almacenan los movimientos.
        categoria (str): Etiqueta de clasificación.

    Returns:
        list: Lista de todos los movimientos de la misma categoría.
    """
    # Lista para almacenar los movimientos con categoría especificada.
    lista_categoria = []
    # Recorremos la lista de movimientos.
    for movimiento in lista_movimientos:
        # Si la categoía coinciden con la especificada
        if movimiento['categoria'] == categoria.lower():
            # Agregamos a la lista de categoria.
            lista_categoria.append(movimiento)
    # Devolvemos lista de categoria.
    return lista_categoria


def eliminar_movimiento(lista_movimientos: list, id_movimiento: int) -> bool:
    """
    Función para eliminar un movimiento de la lista

    Args:
        lista_movimientos (list): Lista donde se almacenan los movimientos.
        id_movimiento (int): Identificador de movimiento.

    Returns:
        bool: Resultado de la eliminación (True o False).
    """
    # Recorremos la lista de movimientos
    for movimiento in lista_movimientos:
        # Comprobamos que el ID se encuentra en la lista
        if movimiento['id'] == id_movimiento:
            # Eliminamos el movimiento de la lista
            lista_movimientos.remove(movimiento)
            # Devolvemos True como elemento eliminado
            return True
    # Si termina el bucle y no ha encontrado el ID, devolvemos False
    return False
