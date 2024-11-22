from faker import Faker
from config import SEMILLA_FAKER
from utils import guardar_csv, extraer_subconjunto
import random
from datetime import datetime, timedelta

# Configuración de Faker con una semilla específica para compras
fake = Faker()
fake.seed_instance(SEMILLA_FAKER + 2)  # Semilla única para evitar colisiones

def generar_datos_compra(num_registros, ids_proveedor):
    """
    Genera una lista de diccionarios con los datos para la tabla Compra.
    :param num_registros: Número de registros a generar.
    :param ids_proveedor: Lista de IDs de proveedores para garantizar la relación FK.
    """
    compras = []
    fechas_generadas = []
    
    for i in range(num_registros):
        # ID de Compra
        id_compra = fake.unique.random_number(digits=8, fix_len=True)  # ID único de 8 dígitos
        
        # ID de Proveedor (usamos las claves en orden para mantener consistencia entre contextos)
        id_proveedor = ids_proveedor[i % len(ids_proveedor)]

        # Fecha entre principios de 2023 y finales de 2025
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2025, 12, 31)
        fecha = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        fechas_generadas.append(fecha)

        # Puerto (depende de la fecha)
        puerto = "Callao" if fecha.year < 2025 else "Chancay"

        # Precio de Envío (depende de la fecha)
        if fecha.year < 2025:
            precio_envio = random.randint(300, 500)
        else:
            precio_envio = random.randint(100, 300)

        # Tiempo de Envío (depende de la fecha)
        if fecha.year < 2025:
            tiempo_envio = random.randint(30, 45)
        else:
            tiempo_envio = random.randint(18, 25)

        # Agregar datos a la lista
        compras.append({
            "ID_COMPRA": id_compra,
            "ID_PROVEEDOR": id_proveedor,
            "Puerto": puerto,
            "Precio_envio": precio_envio,
            "Fecha": fecha.strftime("%Y-%m-%d"),  # Formato compatible con PostgreSQL
            "Tiempo_de_Envio": tiempo_envio
        })

        # Mostrar progreso cada 100,000 registros
        if len(compras) % 100000 == 0:
            print(f"{len(compras)} registros generados para Compra...")

    return compras

def crear_csv_compra():
    """Genera los archivos CSV para los contextos de la tabla Compra."""
    # Cargar los IDs de Proveedores desde los contextos existentes
    for num_registros in [1000, 10000, 100000, 1000000]:
        # Leer los IDs de proveedores en orden desde el archivo generado
        archivo_proveedores = "C:\\Users\\Paris Herrera\\Desktop\\bdProyecto\\T_Proveedor\\proveedor_{}.csv".format(num_registros)
        ids_proveedor = []
        with open(archivo_proveedores, "r") as file:
            next(file)  # Saltar encabezado
            for line in file:
                ids_proveedor.append(line.strip().split(",")[0])  # Tomar solo el ID_PROVEEDOR

        # Generar datos para la tabla Compra
        datos_compra = generar_datos_compra(num_registros, ids_proveedor)

        # Guardar los subconjuntos como archivos CSV
        nombre_archivo = f"compra_{num_registros}.csv"
        guardar_csv(datos_compra, nombre_archivo)
        print(f"Archivo {nombre_archivo} generado con {num_registros} registros.")
