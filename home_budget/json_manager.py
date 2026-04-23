"""
Archivo para el manejo de fichero json
"""

# Biblioteca para el manejo de json
import json


def guardar_presupuesto(lista_movimientos: list, ruta: str):
    """
    Función para guardar los datos de movimientos en un archivo json

    Args:
        lista_movimiento (list): Lista donde se almacenan los movimientos.
        ruta (str): Ruta donde se almacena el json
    """
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(lista_movimientos, f, indent=4)


def cargar_movimientos(
    ruta: str, msg_fichero_cargado: str, msg_nuevo_fichero: str, msg_corrupto: str
) -> list:
    """
    Función para leer y cargar el archivo json de movimientos.

    Args:
        ruta (str): Ruta donde se almacena el archivo json
        msg_fichero_cargado (str): Mensaje de fichero cargado
        msg_nuevo_fichero (str): Mensaje de fichero nuevo
        msg_corrupto (str): Mensaje de fichero corrupto, se crea uno nuevo

    Returns:
        list: Lista de movimientos.
    """
    # Contro de error si el archivo no existe o corrupto
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            lista_movimientos = json.load(f)
            print(msg_fichero_cargado)
            return lista_movimientos
    except FileNotFoundError:
        lista_movimientos = []
        print(msg_nuevo_fichero)
        return lista_movimientos
    except json.JSONDecodeError:
        lista_movimientos = []
        print(msg_corrupto)
        return lista_movimientos
