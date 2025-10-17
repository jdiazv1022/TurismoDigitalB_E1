# Proyecto Turismo Digital B — Evaluación Parcial 1

## Objetivo
Desarrollar un proceso ETL con Python y MongoDB para analizar información simulada del turismo en el Perú.  
El proyecto incluye la generación de datos, su limpieza, carga en una base de datos y la creación de reportes visuales.  
También se automatiza todo el flujo mediante un pipeline en Jenkins.

---

## Estructura del Proyecto

```
TurismoDigitalB_E1/
├── ci/
│   ├── Jenkinsfile
│   ├── captura_pipeline.png.png
│   └── captura_pipeline2.png.png
├── data/
│   └── visitantes.csv
├── database/
│   └── visitantes_clean.csv
├── git/
├── reports/
├── scripts/
│   ├── 2_Crear_BaseCSV.py
│   ├── 3_Generar_Data_Turismo.py
│   ├── 4_Inspeccion_Inicial.py
│   ├── 5_Proceso_ETL.py
│   ├── 6_Loading_MongoDB.py
│   ├── 7_Reportes.py
│   └── verificarResultado.py
├── main.py
└── README.md
```

---

## Requisitos

Antes de empezar, asegúrate de tener instalado:

- Python 3.10 o superior  
- MongoDB (local o en la nube)
- Librerías necesarias:
  ```bash
  pip install pandas numpy faker matplotlib pymongo
  ```

---

## Ejecución Paso a Paso

1. **Crear la base vacía**
   ```bash
   python scripts/2_Crear_BaseCSV.py
   ```

2. **Generar datos simulados**
   ```bash
   python scripts/3_Generar_Data_Turismo.py
   ```

3. **Revisar datos crudos**
   ```bash
   python scripts/4_Inspeccion_Inicial.py
   ```

4. **Limpiar y transformar datos**
   ```bash
   python scripts/5_Proceso_ETL.py
   ```

5. **Cargar datos a MongoDB**
   ```bash
   python scripts/6_Loading_MongoDB.py
   ```

6. **Generar reportes y gráficos**
   ```bash
   python scripts/7_Reportes.py
   ```

7. **Ejecutar todo el proceso completo**
   ```bash
   python main.py
   ```

---

## Limpieza de Datos

Durante el proceso ETL se aplicaron las siguientes decisiones:

- Se reemplazaron valores vacíos o “NA” por “Desconocido”.
- Los medios de transporte nulos se cambiaron por “No especificado”.
- Se eliminaron registros duplicados.
- Se corrigieron tipos de datos (edad, gasto, días, fecha).
- Se eliminaron valores negativos o fechas fuera del rango esperado.

---

## Reportes Generados

Los reportes se guardan automáticamente en la carpeta `reports/`.

| Reporte | Archivo generado |
|----------|------------------|
| Visitantes por región | Visitantes_por_Region.png |
| Países de origen | Visitantes_por_Pais.png |
| Tendencia mensual | Tendencia_Mensual.png |
| Distribución del gasto | Gasto_Promedio.png |

---

## Carga en MongoDB

Los datos limpios se guardan en la colección `Visitantes` dentro de la base `TurismoPeru_2025`.

Ejemplo de carga manual (opcional):
```bash
mongoimport --db TurismoPeru_2025 --collection Visitantes --type csv --headerline --file "database/visitantes_clean.csv"
```

---

## Automatización con Jenkins

El archivo **Jenkinsfile** se encuentra en la carpeta `ci/`.  
Define las etapas para ejecutar automáticamente:

1. Generación de datos  
2. Proceso ETL  
3. Carga en MongoDB  
4. Creación de reportes  

En la misma carpeta se incluyen las capturas del pipeline ejecutado:
- `ci/captura_pipeline.png.png`
- `ci/captura_pipeline2.png.png`

---

## Control de Versiones (Git y GitHub)

Inicialización y conexión del repositorio:
```bash
git init
git branch -M main
git remote add origin https://github.com/jdiazv1022/TurismoDigitalB_E1.git
```

Commits principales realizados:
- “Crear estructura base del proyecto”
- “Generar datos simulados con Faker”
- “Aplicar proceso ETL y limpieza de datos”
- “Cargar datos limpios en MongoDB”
- “Generar reportes visuales”
- “Agregar Jenkinsfile y capturas del pipeline”

---

## Checklist Final

Datos limpios generados en `database/visitantes_clean.csv`  
Gráficos guardados en `reports/`  
Datos cargados correctamente en MongoDB  
Jenkins ejecuta todo el flujo completo  
Capturas guardadas en `ci/`  
Repositorio actualizado en GitHub  

---

**Autor:** Jaime Ricardo Díaz Vargas  
**Curso:** Tópicos en Business Intelligence — 2025-II  
**Institución:** Pontificia Universidad Católica del Perú (PUCP)
