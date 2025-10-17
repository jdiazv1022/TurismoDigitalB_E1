# Proyecto Turismo Digital B — Evaluación Parcial 1

## Objetivo
Aplicar un proceso ETL con Python y MongoDB para analizar datos simulados del turismo peruano.

## Estructura
- `data/` → datos crudos (visitantes.csv)
- `database/` → datos limpios (visitantes_clean.csv)
- `reports/` → gráficos generados
- `scripts/` → scripts Python (ETL, carga y reportes)

## Ejecución paso a paso
1. `python scripts/2_Generar_BaseCSV.py`
2. `python scripts/3_Generar_Data_Turismo.py`
3. `python scripts/4_Inspeccion_Inicial.py`
4. `python scripts/5_Proceso_ETL.py`
5. `python scripts/6_Loading_MongoDB.py`
6. `python scripts/7_Reportes.py`

## Decisiones de limpieza
- Valores nulos de país → "Desconocido"
- Medio de transporte nulo → "No especificado"
- Eliminación de duplicados exactos
- Fechas fuera de rango eliminadas
- Gasto negativo eliminado
