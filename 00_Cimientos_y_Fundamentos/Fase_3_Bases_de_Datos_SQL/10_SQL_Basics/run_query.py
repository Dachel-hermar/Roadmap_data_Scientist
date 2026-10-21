import sqlite3
import pandas as pd

# Conectar a la base de datos
db_path = r"C:\Roadmap_data_Scientist\10_SQL_Basics\empresa.db"
conexion = sqlite3.connect(db_path)

# Leer la consulta del archivo SQL (con codificación UTF-8 para soportar emojis)
with open(r"C:\Roadmap_data_Scientist\10_SQL_Basics\consulta.sql", "r", encoding="utf-8") as file:
    query = file.read()

print("Ejecutando consulta:\n" + "-"*40)
print(query)
print("-"*40 + "\n")

# Ejecutar y mostrar con Pandas para que se vea bonito en la terminal
try:
    df = pd.read_sql_query(query, conexion)
    if df.empty:
        print("La consulta se ejecutó correctamente pero no devolvió resultados.")
    else:
        print(df.to_markdown(index=False))
except Exception as e:
    print(f"❌ Error de SQL: {e}")

conexion.close()
