import pandas as pd

df = pd.read_csv("data/visitantes.csv")

print("=== Primeras filas del archivo ===")
print(df.head(10))

print("\n=== Información general ===")
print(df.info())

print("\n=== Conteo de valores nulos ===")
print(df.isnull().sum())

print("\n=== Conteo de valores 'NA' (texto) ===")
print((df == "NA").sum())

print("\n=== Filas duplicadas (completas) ===")
print(df.duplicated().sum())

print("\n=== Tipos de datos actuales ===")
print(df.dtypes)

print("\n=== Verificación de formato de fecha ===")
df["fecha_visita_convertida"] = pd.to_datetime(df["fecha_visita"], errors="coerce")
print("Fechas no convertibles:", df["fecha_visita_convertida"].isnull().sum())

print("\n=== Inspección finalizada ===")
