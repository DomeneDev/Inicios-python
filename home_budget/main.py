"""
Fichero principal del programa
"""
from budget_logic import registrar_movimiento, obtener_ingresos_gastos, obtener_balance, filtar_por_categoria, eliminar_movimiento
from utils import mostrar_menu, validar_opcion, leer_cadenas, validacion_dato, mostrar_movimientos, mostrar_balance, validar_tipo_movimiento, validar_fecha
from json_manager import guardar_presupuesto, cargar_movimientos

# ---- Nombre del fichero json ----
NOMBRE_FICHERO = "home_budget.json"

# ---- Ruta para guardar fichero ----
RUTA = f"home_budget/data/{NOMBRE_FICHERO}"

# ---- CONSTANTES PARA INPUTS ----
INPUT_OPC = "Seleccione una opción: "
INPUT_CON = "Intoruduzca concepto: "
INPUT_CAT = "Introduzca categoria: "
INPUT_CANT = "Introduzca cantidad: "
INPUT_ID = "Introduzca el ID del movimiento a eliminar: "
INPUT_TIPO_MOV = "Introduce el tipo de movimiento (Gasto/Ingreso): "
INPUT_FECHA = "Introduce la fecha del movimiento(dd-mm-aaaa): "

# ---- CONSTANTES PARA ERROR ----
ERROR_OPC = "Error: 🛑 Debe introducir el valor númerico de la opción.."
ERROR_CON = "🛑 No has introducido un concepto válido..."
ERROR_CAT = "🛑 No has introducido una categoria válida..."
ERROR_CANT_NEG = "Error: 🛑 La cantidad no puede ser negativa..."
ERROR_DATO = "Error: 🛑 Introduzca un dato válido..."
ERROR_DATO_NEG = "🛑 El ID no puede ser negativo..."
ERROR_TIPO_MOV = "🛑 El movimiento no es correcto..."
ERROR_FECHA = "🛑 La fecha introducida no esta en el formato correcto o no es correcta..."

# ---- MENSAJES INFORMATIVOS ----
MSG_FICHERO_CARGADO = ""
MSG_FICHERO_NUEVO = ""
MSG_FICHERO_CORRUPTO = ""


def ejecutar_budget():
    """
    Función principal del programa
    """
    # Lista para almacenar movimientos.
    movimientos = cargar_movimientos(
        RUTA, MSG_FICHERO_CARGADO, MSG_FICHERO_NUEVO, MSG_FICHERO_CORRUPTO)
    # Bucle principal
    while True:
        # Mostramos menú
        mostrar_menu()
        # Almacenamos opción del usuario
        opcion = validar_opcion(INPUT_OPC, ERROR_OPC)
        # Evaluamos y realizamos operación
        match opcion:
            case 1:
                fecha = validar_fecha(INPUT_FECHA, ERROR_FECHA)
                tipo = validar_tipo_movimiento(INPUT_TIPO_MOV, ERROR_TIPO_MOV)
                concepto = leer_cadenas(INPUT_CON, ERROR_CON)
                categoria = leer_cadenas(INPUT_CAT, ERROR_CAT)
                cantidad = validacion_dato(
                    INPUT_CANT, ERROR_CANT_NEG, ERROR_DATO, float)
                registrar_movimiento(movimientos, fecha,
                                     tipo, concepto, categoria, cantidad)
                guardar_presupuesto(movimientos, RUTA)
                print(f"✍ Movimiento {concepto} anotado.\n")
            case 2:
                categoria = leer_cadenas(INPUT_CAT, ERROR_CAT)
                lista_filtrada = filtar_por_categoria(movimientos, categoria)
                mostrar_movimientos(lista_filtrada, categoria)
            case 3:
                ingresos_gastos = obtener_ingresos_gastos(movimientos)
                gastos = ingresos_gastos['gastos']
                print(f"Gastos totales: {gastos}")
            case 4:
                ingresos_gastos = obtener_ingresos_gastos(movimientos)
                ingresos = ingresos_gastos['ingresos']
                print(f"Ingresos totales: {ingresos}")
            case 5:
                ingresos_gastos = obtener_ingresos_gastos(movimientos)
                balance_movimientos = obtener_balance(ingresos_gastos)
                mostrar_balance(balance_movimientos)
            case 6:
                id_movimiento = validacion_dato(
                    INPUT_ID, ERROR_DATO_NEG, ERROR_DATO, int)
                if eliminar_movimiento(movimientos, id_movimiento):
                    print(" ❌ Movimiento eliminado...")
                else:
                    print(" 📛 Movimiento no encontrado....")
            case 7:
                guardar_presupuesto(movimientos, RUTA)
                print("🖐 Saliendo del programa....")
                break
            case _:
                print("📛 Opción no válida")


if __name__ == "__main__":
    ejecutar_budget()
