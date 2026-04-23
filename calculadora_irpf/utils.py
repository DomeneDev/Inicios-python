"""
Lógica de apoyo para refactorización de main
"""


def mostrar_menu():
    """
    Función para mostra menú de opciones.
    """
    print("+------------------------------+")
    print("| 💵 Calculadora de IRPF       |")
    print("+------------------------------+")
    print("| 1 - Realizar nuevo calculo   |")
    print("| 2 - Salir del programa       |")
    print("+------------------------------+\n")


def validacion_dato_opcion(msg_input_opcion: str, msg_error_opcion: str) -> int:
    """
    Función para validación de dato opcion.

    Args:
        opcion (str): Entrada de usuario
        msg_opcion (str): Mensaje del input de opción.
        msg_error (str): Mensaje de error opcio no valida

    Returns:
        int: opcion validada.
    """
    while True:
        opcion = input(msg_input_opcion).strip()
        try:
            opcion = int(opcion)
            break
        except ValueError:
            print(msg_error_opcion)
    print("")
    return opcion


def validacion_dato(msg_input_salario: str, msg_error_salario_neg: str, msg_error_dato) -> float:
    """
    Función para validad dato de salario

    Args:
        salario_bruto (float): Salario brurto
        msg_input_salario (str): Mensaje del input de salario.
        msg_error_salario_neg (str): Mensaje de error salario negativo.
        msg_error_dato (str): Mensaje de erro de dato no válido.

    Returns:
        float: Salario bruto validado.
    """
    while True:
        salario_bruto = input(msg_input_salario).strip()
        try:
            salario_bruto = float(salario_bruto)
            if salario_bruto < 0:
                print(msg_error_salario_neg)
                continue
            break
        except ValueError:
            print(msg_error_dato)
    return salario_bruto


def mostrar_resultados(bruto: float, retencion: float, informe: dict):
    """
    Función para mostrar los resultados del informe.

    Args:
        bruto (float): Salario bruto.
        retencion (float): Retención.
        informe (dict): Informe de resultados.
    """
    print("Resultados.")
    print(f" - Sueldo bruto: {bruto:.2f} €")
    print(f" - Impuesto a abonar: {retencion:.2f} €")
    print(f" - Sueldo Neto: {informe['sueldo_neto']:.2f} €")
    print(
        f" - Porcentaje apliado: {informe['porcentaje_retencion']}%")
