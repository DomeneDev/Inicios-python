"""
Fichero especialista para comuniación con el disco duros, para guardar los
resultados de los analisisi en un fichero json 'historial_analisis.json'
"""

# Importación de biblioteca para trabajar con json
import json


def guardar_json(datos: list, nombre_archivo: str):
    """
    Función para guardar los datos en un archivo json.

    Args:
        datos (list): Lista de diccionarios donde almacenaremos los datos.
        nombre_archivo (str): Nombre del archivo donde se guardaran los datos.
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f)


def cargar_json(nombre_archivo: str) -> list:
    """
    Función para leer y cargar el archivo json devolviendo una lista de
    diccionarios con los elementos del archivo json, si el archivo no existe
    devolvera una lista vacia.

    Args:
        nombre_archivo (str): Nombre del archivo json.

    Return:
        list: lista con los elementos del archivo json
    """
    # Contro de error el archivo no existe.
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            datos_archivo = json.load(f)
            return datos_archivo
    except FileNotFoundError:
        datos_archivo = []
        return datos_archivo
