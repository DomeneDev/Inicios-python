"""
Desarrollo de lógica interna para el análisis de cadenas de texto.
Código modular y no dependiente de ninguna interfaz de entrada/salida (input/print)
"""
# Bibliotea re para el reemplazo de caractres sobre un string
import re


def limpiar_texto(texto_bruto: str) -> str:
    """
    Función para "limpiar" el texto introducido:
    - Convertir a minsculas
    - Eliminar signos de puntuacion (. , ;) y reemplazar por espacios en blanco
    Args:
        texto_bruto (str): Texto a "limpiar"

    Returns:
        str: Texto "limpio"
    """
    # Convertir texto a minúsculas
    texto_minus = texto_bruto.lower()
    # Eliminar signos de puntiacion con re.sub()
    texto_tratado = re.sub(r"[.,;]", " ", texto_minus)
    # Devolver el texto tratado, sin signos de puntuación en minúsculas
    return texto_tratado


def contar_frecuencia(texto_limpio: str) -> dict:
    """
    Función para establecer la frecuencia de las palabras en el texto
    Args:
        texto_limpio (str): Texto "limpio" ya tratado por la función limiar_texto

    Returns:
        dict: Diccionario donde se almacena la frecuencia con la estructura {palabra:frecuencia}
    """
    # Genero diccionario vacio para guardar las cantidad de veces que se repiten las palabras
    frecuencia_palabras = {}

    # Separo el texto por palabras y lo almaceno en una lista
    palabras = texto_limpio.split()
    # Bucle para recorrer las palabras de la lista
    for palabra in palabras:
        # Si la palabra no se encuntra en el diccionario
        if palabra not in frecuencia_palabras:
            # Añado palabra y valor 1 como primera coincidencia
            frecuencia_palabras[palabra] = 1
        # Si la palabra SI se encuentra en el diccionario
        else:
            # Aumento el valor en 1
            frecuencia_palabras[palabra] += 1
    # Devuolver diccionario de frecuencia de aparición
    return frecuencia_palabras


def generar_metricas(texto_limpio: str) -> dict:
    """
    Función para generar las métricas para el analisis
    - Contar el total de palabras
    - Encontrar la palabra más larga
    - Calcular la longitud media de las palabras(formato con 2 decimales)

    Args:
        texto_limpio (dict): Diccionario donde se almacenan la frecuencia de aparición de las palabras

    Returns:
        dict: Diccionario donde almacenar los resultados de las métricas con las claves:
        - total_palabras
        - palabra_mas_larga
        - promedio_longitud
    """
    # Convierto la cadena en una lista
    palabras = texto_limpio.split()
    # Total de palabras es la suma de las elementos de la lista
    total_palabras = len(palabras)
    # Utilizo función max para encontrar el elemento con la mayor longitud de la lista
    palabra_mas_larga = max(palabras, key=len)
    # Lógica para calcular la media
    # Variables para almacenar la longitud de la suma de todos los elementos de la lista
    suma_longitudes = 0
    # Recorrer el diccionario para extraer la longitud de las claves y el número de claves.
    for palabra in palabras:
        longitud_de_la_clave = len(palabra)
        suma_longitudes += longitud_de_la_clave
    # Calculo para el promedio de longitud de las claves
    promedio_longitud = round(suma_longitudes/total_palabras, 2)
    # Construir diccionario con las métricas.
    metricas = {
        "total_palabras": total_palabras,
        "palabra_mas_larga": palabra_mas_larga,
        "promedio_longitud": promedio_longitud
    }
    # Devolver el diccionario de las métricas.
    return metricas


def preparar_registro(texto: str, metricas: dict) -> dict:
    """
    Función para preparar los datos para carga en fichero json

    Args:
        texto (str): Texto a analizar
        metricas (dict): Resultado de las métricas

    Returns:
        dict: Diccionario con los datos para su transformación a fichero json
    """
    # Muestra del texto
    muestra_texto = texto[:20]+"..."
    # Diccionario principal
    datos_preparados = {
        'texto original': muestra_texto,
        'resultados': metricas
    }
    return datos_preparados
