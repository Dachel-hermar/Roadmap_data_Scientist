"""
⚔️ Reto 4: El Formateador del Banco (SQL + Python Strings) 
Contexto de Negocio: El sistema viejo del banco necesita procesar nuestra nómina, 
pero es tan arcaico que solo acepta nombres en letras MAYÚSCULAS 
y salarios formateados con el símbolo de divisa (Ej: $58000). 
Arquitectura Híbrida: Usa SQL para extraer a todos los empleados (nombre y salario). 
Usa tu bucle en Python y rescata los métodos nativos de texto de la Fase 2 (como .upper()) 
para imprimir un reporte que diga exactamente: "Nómina bancaria: FERNANDO TORRES - $58000".
"""
import sqlite3
conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
cursor= conexion.cursor()
# vamos a consultar nuestras tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tablas= cursor.fetchall()
print(tablas)
# Ya sabemos que trabajamos con dos tablas ahora vamos a ver sus campos
print("="*40)
print("Columnas de la tabla de ventas")
print("=" * 40)
cursor.execute("PRAGMA table_info(ventas)")
tabla_ventas= cursor.fetchall()
for columna in tabla_ventas:
    print(f"{columna}\n")
# Y ahora la tabla empleados
print("="*40)
print("Columnas de la tabla de empleados")
print("=" * 40)
cursor.execute("PRAGMA table_info(empleados)")
tabla_empleados= cursor.fetchall()
for column in tabla_empleados:
    print(f"{column}\n")
# Ahora que ya hemos visto los datos volvemos a la solución, ya sabemos que debemos de trabajar con la tabla empleados
cursor.execute("SELECT nombre, salario FROM empleados")
resultado= cursor.fetchall()
print(resultado)
# Ahora nuestro bucle for, para extraer los datos

for empleado in resultado:
    print(f"Nómina bancaria: {empleado[0].upper()} - ${empleado[1]}")

# REPORTE
# Se han rescatado con éxito, a los trabajadores y sus respectivos salarios, como lo necesita el sitema
# Se puede proceder a pagar la nómina
