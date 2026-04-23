from inventario_logic import agregar_producto, vender_producto, obtener_resumen
from utils import mostrar_menu, leer_cadenas, validar_opcion, validacion_dato, mostrar_venta, mostrar_resumen
from csv_manager import guardar_csv, cargar_csv, borrar_archivo_fisico

# Nombre fichero
NOMBRE_FICHERO = "inventario.csv"

# RUTA DE FICHERO
RUTA = f"gestor_de_inventario/data/{NOMBRE_FICHERO}"

# ---- CONSTANTES MSG  -----
INPUT_OPCION = "➡ Introduzca una opción: "
INPUT_NOMBRE = "Nombre del producto: "
INPUT_CANT = "Cantidad del producto: "
INPUT_PREC = "Precio del producto (2 decimales): "
INPUT_CARGA = "Existe un inventario ¿Desea (C)argarlo o (R)esetearlo? "
INPUT_RESET = "Esta opción eliminará todo el contenido del inventario, ¿Desea continuar (Y/N)? "
INPUT_BORRADO = f"Esta opción eliminará el archivo {NOMBRE_FICHERO} y su contenido, ¿Desea continuar (Y/N)? "

# ---- CONSTANTES ERR ----
ERROR_OPCION = "🛑 El valor introducido debe ser un número entero..."
ERROR_NOMBRE = "🛑 No has introducido un nombre..."
ERROR_PREC_NEG = "🛑 El precio no puede ser negativo..."
ERROR_CANT_NEG = "🛑 La cantidad no puede ser negativa..."
ERROR_DATO_INV = "ERROR: ❌ no es un valor válido, intentelo de nuevo."
ERROR_OPC_NO_VAL = "🛑 Opción no válida"
ERROR_RUTA = "El fichero .csv no existe en la ruta cofigurada."

# ---- COSNTANTES MENSAJE INFORMATIVOS ----
MSG_CARGA = "👍 Archivo cargado con éxito"
MSG_CANCELACION = "Operación cancelada por el usuario...."
MSG_SALIDA = "Los datos se han guardado autómiciamente... Adios..."
MSG_RESETEO = "🧹 Archivo reseado con éxito.."
MSG_ELMINIADO = "☠ Base de datos eliminada..."

# Función principal de programa


def ejecutar_inventario():
    """
    Función princpial para ejecutar el programa y su funcionalidad
    """
    # Diccionario vacío para almacenar el inventario del almácen
    # Carga de fichero inventario
    inventario = cargar_csv(RUTA)
    # Si el fichero existe
    if inventario:
        en_carga = True
        while en_carga:
            # Solicitamos si el usuario quiere cargar la base de datos o reset
            opcion_cargar = input(INPUT_CARGA).upper()
            match  opcion_cargar:
                case "C":
                    print(MSG_CARGA)
                    en_carga = False
                case "R":
                    while True:
                        opcion_reset = input(INPUT_RESET).upper()
                        match opcion_reset:
                            case "Y":
                                inventario = {}
                                guardar_csv(inventario, RUTA, ERROR_RUTA)
                                print(MSG_RESETEO)
                                en_carga = False
                                break
                            case "N":
                                print(MSG_CANCELACION)
                                break
                            case _:
                                print(ERROR_OPC_NO_VAL)
                case _:
                    print(ERROR_OPC_NO_VAL)
    while True:
        # Mostramos menú
        mostrar_menu()
        # Solicitamos opción y validamos
        opcion = validar_opcion(INPUT_OPCION, ERROR_OPCION)
        match opcion:
            case 1:
                # Leer nombre validado
                nombre = leer_cadenas(INPUT_NOMBRE, ERROR_NOMBRE)
                # validar cantidad
                cantidad = validacion_dato(
                    INPUT_CANT, ERROR_CANT_NEG, ERROR_DATO_INV, int)
                # Validar precio
                precio = validacion_dato(
                    INPUT_PREC, ERROR_PREC_NEG, ERROR_DATO_INV, float)
                # Agregar producto
                agregar_producto(nombre, precio, cantidad, inventario)
                guardar_csv(inventario, RUTA, ERROR_RUTA)
                # Mensaje de confirmación.
                print("✅ Producto añadido o modificado\n")
            case 2:
                # Solicitamos datos del producto a vender
                # Validación de nombre de producto
                nombre = leer_cadenas(INPUT_NOMBRE, ERROR_NOMBRE)
                # Validación de Cantidad de venta
                cantidad = validacion_dato(
                    INPUT_CANT, ERROR_CANT_NEG, ERROR_DATO_INV, int)
                # Comprobamos si se puede realizar la venta:
                exito = vender_producto(nombre, cantidad, inventario)
                # modificar registro
                guardar_csv(inventario, RUTA, ERROR_RUTA)
                # Mostra informacion de venta
                mostrar_venta(exito, nombre, cantidad, inventario)
            case 3:
                # Llamamamos a lógica de metricas de inventario
                resumen = obtener_resumen(inventario)
                # Mostrar resumen
                mostrar_resumen(resumen)
            case 4:
                opcion_borrado = input(INPUT_BORRADO).upper()
                match opcion_borrado:
                    case "Y":
                        borrar_archivo_fisico(RUTA)
                        print(MSG_ELMINIADO)
                        inventario = {}
                        print()
                        return inventario
                    case "N":
                        print(MSG_CANCELACION)
                        break
                    case _:
                        print(ERROR_OPC_NO_VAL)
            case 5:
                guardar_csv(inventario, RUTA, ERROR_RUTA)
                print(MSG_SALIDA)
            case _:
                pass


if __name__ == "__main__":
    ejecutar_inventario()
