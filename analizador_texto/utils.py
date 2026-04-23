"""
Fichero para almacenar funciones para apoyar al main y refactorizar.
"""


def leer_texto(mensaje_input: str, error_msg: str):
    """
    Función para verificar el formato correcto del texto

    Args:
        texto (str): Texto a revisar
        error_msg (str): Mensaje de error
    """
    while True:
        texto = input(mensaje_input)
        try:
            if not texto.strip():
                raise ValueError(error_msg)
        except ValueError as e:
            print(f"❌ ERROR: {e}")
        else:
            break
    return texto


def mostrar_resultados(metricas: dict, frecuencia: dict):
    """
    Función para formateo de salida de métricas

    Args:
        metricas (dict): Diccionario que almacena las métricas del texto.
    """
    print("+------------------------------------+")
    print("| Resultados del análisis del texto  |")
    print("+------------------------------------+")
    print(f" - Total de palabras del texto: {metricas['total_palabras']}.")
    print(f" - Palabra más larga: {metricas['palabra_mas_larga']}.")
    print(
        f" - Media de longitud de las palabras: {metricas['promedio_longitud']}.")
    print("- Cantidad de palabras:")
    for palabra, cantidad in frecuencia.items():
        if cantidad == 1:
            print(f" \t- {palabra}: {cantidad} vez")
        else:
            print(f" \t- {palabra}: {cantidad} veces.")
