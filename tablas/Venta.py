import random
from datetime import datetime, timedelta
import csv
from utils import guardar_csv

def generar_datos_venta(num_registros, archivo_clientes):
    """
    Genera una lista de diccionarios con los datos para la tabla Venta.
    :param num_registros: Número de registros a generar.
    :param archivo_clientes: Ruta del archivo clientes_{num_registros}.csv.
    """
    ventas = []

    # Leer datos de la tabla Clientes
    with open(archivo_clientes, "r") as file:
        reader = csv.DictReader(file)
        dnis = [row["DNI"] for row in reader]  # Extraer los DNI en orden

    # Generar datos de Venta
    for i in range(num_registros):
        # ID_VENTA (número único de 9 dígitos)
        id_venta = random.randint(100000000, 999999999)

        # DNI (extraído en orden)
        dni = dnis[i % len(dnis)]

        # Fecha (entre junio de 2023 y diciembre de 2025)
        start_date = datetime(2023, 6, 1)
        end_date = datetime(2025, 12, 31)
        random_days = random.randint(0, (end_date - start_date).days)
        fecha = start_date + timedelta(days=random_days)
        fecha_formateada = fecha.strftime("%Y-%m-%d")  # Formato compatible con SQL

        # Agregar registro a la lista
        ventas.append({
            "ID_VENTA": id_venta,
            "DNI": dni,
            "Fecha": fecha_formateada
        })

        # Mostrar progreso cada 100,000 registros
        if len(ventas) % 100000 == 0:
            print(f"{len(ventas)} registros generados para Venta...")

    return ventas

def crear_csv_venta():
    """Genera los archivos CSV para los contextos de la tabla Venta."""
    # Ruta de la tabla Clientes
    archivo_clientes_base = r"C:\\Users\\Paris Herrera\\Desktop\\bdProyecto\\T_clientes\\clientes_{num_registros}.csv"

    for num_registros in [1000, 10000, 100000, 1000000]:
        # Ruta del archivo para el contexto actual
        archivo_clientes = archivo_clientes_base.format(num_registros=num_registros)

        # Generar datos para Venta
        datos_venta = generar_datos_venta(num_registros, archivo_clientes)

        # Guardar los subconjuntos como archivos CSV
        nombre_archivo = f"venta_{num_registros}.csv"
        guardar_csv(datos_venta, nombre_archivo)
        print(f"Archivo {nombre_archivo} generado con {num_registros} registros.")
