import pandas as pd
from pymongo import MongoClient

# Leer el CSV limpio
df = pd.read_csv("database/visitantes_clean.csv")

# Conexión a MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Crear base y colección
db = client["TurismoPeru_2025"]
col = db["Visitantes"]

# Convertir a formato diccionario
records = df.to_dict(orient="records")

# Insertar los datos
col.insert_many(records)
print("Insertados:", len(records), "documentos en MongoDB.")
