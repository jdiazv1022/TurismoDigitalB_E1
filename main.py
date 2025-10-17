import subprocess

subprocess.run(["python", "scripts/3_Generar_Data_Turismo.py"])
subprocess.run(["python", "scripts/5_Proceso_ETL.py"])
subprocess.run(["python", "scripts/6_Loading_MongoDB.py"])
subprocess.run(["python", "scripts/7_Reportes.py"])

print("Proceso completo ejecutado con éxito.")
