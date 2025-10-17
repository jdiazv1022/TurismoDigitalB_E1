# Librerías principales
from faker import Faker        
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

fake = Faker()

n = 3000   # cantidad de registros "reales" que queremos generar

# Listas con valores posibles (puedes editar para añadir países o destinos)
paises = ["Perú","Chile","Argentina","USA","Colombia","Brasil","España","México"]
# cada destino viene con su región (tuplas: (destino, region))
destinos = [
    ("Machu Picchu", "Cusco"),
    ("Lago Titicaca", "Puno"),
    ("Paracas", "Ica"),
    ("Arequipa", "Arequipa"),
    ("Huaraz", "Áncash"),
    ("Cusco Ciudad", "Cusco"),
    ("Trujillo", "La Libertad")
]

# Posibles medios de transporte; incluimos None intencional para nulos
transportes = ["Avión","Bus","Auto","Tren","Desconocido", None]

rows = []
for i in range(1, n+1):
    # id_visitante: V0001, V0002, ...
    idv = f"V{str(i).zfill(4)}"

    # seleccionamos un país al azar
    pais = random.choice(paises)

    # edad entre 15 y 79 (np.random.randint incluye el mínimo y excluye el máximo)
    edad = np.random.randint(15, 80)

    # genero: M o F al azar
    genero = random.choice(["M","F"])

    # elegimos un destino y su región
    destino, region = random.choice(destinos)

    # fecha: generamos una fecha aleatoria entre 2024-01-01 y 2025-09-30
    start = datetime(2024, 1, 1)
    fecha = start + timedelta(days=random.randint(0, 640))

    dias = int(np.random.choice([1,2,3,4,5,7,10], p=[0.15,0.2,0.25,0.1,0.15,0.1,0.05]))

    gasto = round(max(0, np.random.normal(800 if pais == "Perú" else 1400, 400)), 0)

    # transporte: al azar, puede ser None
    transporte = random.choice(transportes)

    if random.random() < 0.02:
        pais = None

    if random.random() < 0.03:
        transporte = "NA"

    rows.append([
        idv,
        pais,
        edad,
        genero,
        destino,
        region,
        fecha.strftime("%Y-%m-%d"),
        dias,
        gasto,
        transporte
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "id_visitante","pais_origen","edad","genero","destino","region",
        "fecha_visita","dias_estadia","gasto_total","medio_transporte"
    ]
)

# Tomamos 30 filas aleatorias y las duplicamos para probar deduplicación
df = pd.concat([df, df.sample(30, random_state=1)], ignore_index=True)

# Guardamos en la carpeta data
df.to_csv("data/visitantes.csv", index=False)

print("Generado visitantes.csv con", len(df), "filas")
