from faker import Faker
from config import SEMILLA_FAKER
from utils import guardar_csv
import random

# Configuración de Faker con una semilla específica para Producto_Compra
fake = Faker()
fake.seed_instance(SEMILLA_FAKER + 3)  # Semilla única para garantizar unicidad

def generar_datos_producto_compra(num_registros, ids_compra, ids_proveedor):
    """
    Genera una lista de diccionarios con los datos para la tabla Producto_Compra.
    :param num_registros: Número de registros a generar.
    :param ids_compra: Lista de IDs de Compra en orden.
    :param ids_proveedor: Lista de IDs de Proveedor en orden.
    """
    productos_compra = []
    ids_producto = set()  # Para garantizar que los IDs de producto sean únicos

    for i in range(num_registros):
        # Generar ID único de producto
        while True:
            id_producto = fake.unique.random_number(digits=8, fix_len=True)
            if id_producto not in ids_producto:
                ids_producto.add(id_producto)
                break

        # ID de Compra (extraído en orden)
        id_compra = ids_compra[i % len(ids_compra)]

        # ID de Proveedor (extraído en orden)
        id_proveedor = ids_proveedor[i % len(ids_proveedor)]

        # Generar Costo Unitario
        costo_unitario = round(random.uniform(10, 3000), 2)

        # Generar Cantidad
        cantidad = random.randint(50, 100)

        # Agregar registro a la lista
        productos_compra.append({
            "Costo_unitario": costo_unitario,
            "ID_producto": id_producto,
            "ID_compra": id_compra,
            "ID_proveedor": id_proveedor,
            "Cantidad": cantidad
        })

        # Mostrar progreso cada 100,000 registros
        if len(productos_compra) % 100000 == 0:
            print(f"{len(productos_compra)} registros generados para Producto_Compra...")

    return productos_compra

def crear_csv_producto_compra():
    """Genera los archivos CSV para los contextos de la tabla Producto_Compra."""

    for num_registros in [1000, 10000, 100000, 1000000]:
        # Ruta de la tabla Compra
        archivo_compra = f"C:\\Users\\Paris Herrera\\Desktop\\bdProyecto\\T_Compra\\compra_{num_registros}.csv"

        # Leer IDs de Compra e IDs de Proveedor en orden desde la tabla Compra
        ids_compra = []
        ids_proveedor = []
        with open(archivo_compra, "r") as file:
            next(file)  # Saltar encabezado
            for line in file:
                columns = line.strip().split(",")
                ids_compra.append(columns[0])  # ID_COMPRA
                ids_proveedor.append(columns[1])  # ID_PROVEEDOR (de la tabla Compra)

        # Generar datos para Producto_Compra
        datos_producto_compra = generar_datos_producto_compra(num_registros, ids_compra, ids_proveedor)

        # Guardar los subconjuntos como archivos CSV
        nombre_archivo = f"producto_compra_{num_registros}.csv"
        guardar_csv(datos_producto_compra, nombre_archivo)
        print(f"Archivo {nombre_archivo} generado con {num_registros} registros.")
