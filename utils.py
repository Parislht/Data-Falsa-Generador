# utils.py
import pandas as pd

def guardar_csv(datos, nombre_archivo):
    df = pd.DataFrame(datos)
    df.to_csv(nombre_archivo, index=False)

def extraer_subconjunto(datos, num_registros):
    """Extrae los primeros num_registros de una lista de datos."""
    return datos[:num_registros]


def guardar_subconjuntos_csv(subconjunto, nombre_archivo):
    df = pd.DataFrame(subconjunto)
    df.to_csv(nombre_archivo, index=False)
    print(f"Archivo {nombre_archivo} generado con {len(subconjunto)} registros.")
