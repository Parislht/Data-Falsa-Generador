from faker import Faker
from config import SEMILLA_FAKER
from utils import guardar_csv, extraer_subconjunto

# Configuración de Faker con una semilla específica para proveedores
fake = Faker()
fake.seed_instance(SEMILLA_FAKER + 1)  # Cambiamos la semilla para que sea diferente de clientes

# Lista actualizada de países
PAISES = [
    "Australia", "Brunei Darussalam", "Canadá", "Chile", "China", 
    "Hong Kong", "Indonesia", "Japón", "Corea del Sur", "Malasia", 
    "México", "Nueva Zelanda", "Papúa Nueva Guinea", "Perú", "Filipinas", 
    "Rusia", "Singapur", "Tailandia", "Estados Unidos", "Vietnam"
]

def generar_datos_proveedor(num_registros):
    """Genera una lista de diccionarios con los datos para la tabla Proveedor."""
    proveedores = []

    for _ in range(num_registros):
        id_proveedor = fake.unique.random_number(digits=8, fix_len=True)  # ID único de 8 dígitos
        pais = fake.random.choice(PAISES)  # Seleccionar un país aleatoriamente
        proveedores.append({"id_proveedor": id_proveedor, "pais": pais})
        
        # Mostrar progreso cada 100,000 registros
        if len(proveedores) % 100000 == 0:
            print(f"{len(proveedores)} registros generados para Proveedor...")
    
    return proveedores

def crear_csv_proveedor():
    """Genera los archivos CSV para los contextos de la tabla Proveedor."""
    # Generar datos para el millón de registros
    datos_proveedor = generar_datos_proveedor(1000000)

    # Guardar subconjuntos para cada contexto
    for num_registros in [1000, 10000, 100000, 1000000]:
        subconjunto = extraer_subconjunto(datos_proveedor, num_registros)
        nombre_archivo = f"proveedor_{num_registros}.csv"
        guardar_csv(subconjunto, nombre_archivo)
        print(f"Archivo {nombre_archivo} generado con {num_registros} registros.")
