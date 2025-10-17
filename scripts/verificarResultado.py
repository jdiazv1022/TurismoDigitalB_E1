import pandas as pd
df = pd.read_csv("database/visitantes_clean.csv")
print(df.info())
print(df.head())
print(df.isnull().sum())
