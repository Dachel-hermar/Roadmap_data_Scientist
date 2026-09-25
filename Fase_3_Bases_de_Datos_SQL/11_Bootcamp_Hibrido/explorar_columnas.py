import sqlite3
# Paso 1- Conecetarme a la base de datos
conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
# Paso 2 Crear el conector
cursor= conexion.cursor()
cursor.execute("PRAGMA table_info(ventas)")
resultados = cursor.fetchall()
for columna in resultados:
    print(columna)