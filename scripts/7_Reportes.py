import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos limpios
df = pd.read_csv("database/visitantes_clean.csv")
df['fecha_visita'] = pd.to_datetime(df['fecha_visita'])

# 1. Visitantes por región
plt.figure()
df['region'].value_counts().plot(kind='bar')
plt.title("Visitantes por Región")
plt.xlabel("Región")
plt.ylabel("Número de visitantes")
plt.tight_layout()
plt.savefig("reports/Visitantes_por_Region.png")
print("Gráfico 1 guardado.")

# 2. Top países de origen
plt.figure()
df['pais_origen'].value_counts().head(10).plot(kind='pie', autopct='%1.1f%%')
plt.title("Top 10 Países de Origen")
plt.ylabel('')
plt.tight_layout()
plt.savefig("reports/Visitantes_por_Pais.png")
print("Gráfico 2 guardado.")

# 3. Tendencia mensual de visitas
df['mes'] = df['fecha_visita'].dt.to_period('M')
plt.figure()
df.groupby('mes').size().plot(kind='line')
plt.title("Tendencia mensual de visitas")
plt.xlabel("Mes")
plt.ylabel("Visitas")
plt.tight_layout()
plt.savefig("reports/Tendencia_Mensual.png")
print("Gráfico 3 guardado.")

# 4. Histograma de gasto total
plt.figure()
df['gasto_total'].hist(bins=30)
plt.title("Distribución del gasto total")
plt.xlabel("Gasto total")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("reports/Gasto_Promedio.png")
print("Gráfico 4 guardado.")