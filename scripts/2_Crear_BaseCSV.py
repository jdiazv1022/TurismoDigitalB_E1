import pandas as pd

# Definir las columnas del CSV base
columnas = ["id_visitante", "pais_origen", "edad", "genero", "destino", "region", 
            "fecha_visita", "dias_estadia", "gasto_total", "medio_transporte"]

# Crear un DataFrame vacío con esas columnas
df = pd.DataFrame(columns=columnas)

# Guardar el archivo CSV en la carpeta data
df.to_csv("data/base.csv", index=False)

print("Archivo base.csv creado correctamente en la carpeta data.")
