
import pandas as pd
import numpy as np

df = pd.read_csv("data/visitantes.csv", dtype=str)
print("Archivo cargado correctamente con", len(df), "filas")

df = df.replace({"NA": pd.NA, "": pd.NA, "None": pd.NA})
print("Valores 'NA' y vacíos reemplazados por NaN")

antes = len(df)

df = df.drop_duplicates()
print("Duplicados eliminados:", antes - len(df))

df["edad"] = pd.to_numeric(df["edad"], errors="coerce").astype("Int64")
df["dias_estadia"] = pd.to_numeric(df["dias_estadia"], errors="coerce").astype("Int64")
df["gasto_total"] = pd.to_numeric(df["gasto_total"], errors="coerce")
df["fecha_visita"] = pd.to_datetime(df["fecha_visita"], errors="coerce")

print("Tipos de datos convertidos correctamente.")

df["pais_origen"] = df["pais_origen"].fillna("Desconocido")
df["medio_transporte"] = df["medio_transporte"].fillna("No especificado")

# Eliminar filas con errores graves
df = df.dropna(subset=["fecha_visita","gasto_total"])
df = df[df["gasto_total"] >= 0]
print("Filas inválidas eliminadas.")

# Guardar el archivo limpio
df.to_csv("database/visitantes_clean.csv", index=False)
print("Archivo limpio guardado correctamente en database/visitantes_clean.csv")
print("Total de filas finales:", len(df))
