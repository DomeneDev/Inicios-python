"""
Lógica para el calculo de IRPF de un salario
"""

# Constante para almacenar los tramos (limite, porcentaje a aplicar)
TRAMOS = [
    (12450, 0.19),
    (20200, 0.24),
    (35200, 0.30),
    (60000, 0.37),
    (float('inf'), 0.45)
]


def calcular_retencion(sueldo_bruto: float) -> float:
    """
    Función para calcular la retención de un sueldo bruto
    Args:
        sueldo_bruto (float): Sueldo bruto

    Returns:
        float: Retención
    """
    # Variables para almacenar el impuesto acumulado y el limite anterior
    impuesto_acumulado = 0
    limite_anterior = 0
    # Bucle para recorres la lista TRAMOS
    for limite_actual, porcentaje in TRAMOS:
        # ¿El salario supera el tramo actual?
        if sueldo_bruto > limite_actual:
            # Tramo completo
            dinero_en_tramo = limite_actual - limite_anterior
        else:
            # Tramo parcial o final
            dinero_en_tramo = sueldo_bruto - limite_anterior
        # Solo calculamos si hay dinero en positivo en el tramo
        if dinero_en_tramo > 0:
            impuesto_tramo = dinero_en_tramo * porcentaje
            impuesto_acumulado += impuesto_tramo
        # Preparamos limite para el siguiente paso
        limite_anterior = limite_actual
        # Condición de salida
        if sueldo_bruto <= limite_actual:
            break
    # Devolvemos retención dineararia
    return round(impuesto_acumulado, 2)


def generar_informe(sueldo_bruto: float, retencion: float) -> dict:
    """
    Función para genear un diccionario con el informe de sueldo
    Args:
        sueldo_bruto (float): Sueldo bruto
        retencion (float): Retención calculada en calcular_retencion()

    Returns:
        dict: Diccionario con la métricas: neto, porcentaje de retencion  (2f)
    """
    if sueldo_bruto == 0:
        return 0
    # Cálculo de sueldo neto
    sueldo_neto = round(sueldo_bruto - retencion, 2)
    # Cálculo de porcentaje de retención
    porcentaje_retencion = round((retencion / sueldo_bruto) * 100, 2)
    # Generamos diccionario para almacenar resultados
    resultados = {
        "sueldo_neto": sueldo_neto,
        "porcentaje_retencion": porcentaje_retencion
    }
    # Devolvemos resultados
    return resultados
