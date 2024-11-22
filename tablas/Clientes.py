from faker import Faker
from config import SEMILLA_FAKER
from utils import guardar_csv, extraer_subconjunto

# Configuración de Faker
fake = Faker()
fake.seed_instance(SEMILLA_FAKER)

# Lista de los 24 departamentos del Perú
DEPARTAMENTOS = [
    "Amazonas", "Ancash", "Apurimac", "Arequipa", "Ayacucho",
    "Cajamarca", "Callao", "Cusco", "Huancavelica", "Huanuco",
    "Ica", "Junin", "La Libertad", "Lambayeque", "Lima",
    "Loreto", "Madre de Dios", "Moquegua", "Pasco", "Piura",
    "Puno", "San Martín", "Tacna", "Tumbes", "Ucayali"
]

def generar_datos_clientes(num_registros):
    """Genera una lista de diccionarios con los datos para la tabla Clientes."""
    clientes = set()  # Usamos un set para garantizar que no se repitan los DNI
    resultados = []

    while len(clientes) < num_registros:
        dni = fake.unique.random_number(digits=8, fix_len=True)  # Generar DNI único
        departamento = fake.random.choice(DEPARTAMENTOS)  # Seleccionar un departamento
        if dni not in clientes:
            clientes.add(dni)
            resultados.append({"DNI": dni, "Departamento": departamento})
        
        # Mostrar progreso cada 100,000 registros
        if len(clientes) % 100000 == 0:
            print(f"{len(clientes)} registros generados para Clientes...")
    
    return resultados

def crear_csv_clientes():
    """Genera los archivos CSV para los contextos de la tabla Clientes."""
    # Generar datos para el millón de registros
    datos_clientes = generar_datos_clientes(1000000)

    # Guardar subconjuntos para cada contexto
    for num_registros in [1000, 10000, 100000, 1000000]:
        subconjunto = extraer_subconjunto(datos_clientes, num_registros)
        nombre_archivo = f"clientes_{num_registros}.csv"
        guardar_csv(subconjunto, nombre_archivo)
        print(f"Archivo {nombre_archivo} generado con {num_registros} registros.")
