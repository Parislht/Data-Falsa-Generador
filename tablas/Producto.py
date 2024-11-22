import random
import csv
from utils import guardar_csv

def generar_datos_producto(num_registros, archivo_producto_compra):
    """
    Genera una lista de diccionarios con los datos para la tabla Producto.
    :param num_registros: Número de registros a generar.
    :param archivo_producto_compra: Ruta del archivo producto_compra_{num_registros}.csv.
    """
    productos = []

    # Leer datos de producto_compra
    with open(archivo_producto_compra, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # ID_PRODUCTO (se jala del producto_compra)
            id_producto = row["ID_producto"]

            # Precio Venta (30% más del Costo Unitario)
            costo_unitario = float(row["Costo_unitario"])
            precio_venta = round(costo_unitario * 1.3, 2)

            # Impuesto (10% a 20% del Precio Venta, aleatorio)
            impuesto_porcentaje = random.uniform(10, 20) / 100  # Generar un porcentaje entre 10% y 20%
            impuesto = round(precio_venta * impuesto_porcentaje, 2)

            # Agregar datos a la lista
            productos.append({
                "ID_PRODUCTO": id_producto,
                "PrecioVenta": precio_venta,
                "Impuesto": impuesto
            })

            # Salir del bucle si ya se generaron los registros necesarios
            if len(productos) >= num_registros:
                break

    return productos

def crear_csv_producto():
    """Genera los archivos CSV para los contextos de la tabla Producto."""
    # Ruta de la tabla Producto_Compra
    archivo_producto_compra = r"C:\\Users\\Paris Herrera\\Desktop\\bdProyecto\\T_producto_compra\\producto_compra_{num_registros}.csv"

    for num_registros in [1000, 10000, 100000, 1000000]:
        # Generar datos para Producto
        datos_producto = generar_datos_producto(num_registros, archivo_producto_compra.format(num_registros=num_registros))

        # Guardar los subconjuntos como archivos CSV
        nombre_archivo = f"producto_{num_registros}.csv"
        guardar_csv(datos_producto, nombre_archivo)
        print(f"Archivo {nombre_archivo} generado con {num_registros} registros.")
