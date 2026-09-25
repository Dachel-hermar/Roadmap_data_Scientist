"""
⚔️ Reto 1: La Alerta de Presupuestos (SQL ORDER BY + Python If/Else) 

Negocio: Finanzas está auditando nóminas. 
Quieren una lista de todos los empleados ordenados por sueldo, pero necesitan alertas rojas de sistema para los que ganan demasiado. 

La Arquitectura Híbrida:

Usa SQL para extraer nombre y salario de toda la tabla, obligando a la base de datos a ordenarlos con ORDER BY de mayor a menor.
En Python, adentro de tu bucle for, inyecta un bloque if / else. 
Si el salario es mayor a $50,000, haz que Python imprima: "🚨 ALERTA ROJA: [Nombre] gana [Salario]". 
Si es menor o igual, imprime "✅ Sueldo normal: [Nombre] gana [Salario]".
"""
import sqlite3

# Paso 1- Conecetarme a la base de datos
conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
# Paso 2 Crear el conector
cursor= conexion.cursor()
# Volviendo al ejercicio
cursor.execute("SELECT nombre, salario FROM empleados ORDER BY salario DESC")
resultado_consulta= cursor.fetchall()
print(resultado_consulta)
# Ahora que tenemos una tupla de listas, vamos a extraer solo los empleados que complen con la condicion
for empleado in resultado_consulta:
    if empleado[1] > 50000:
        print(f"🚨 ALERTA ROJA: {empleado[0]} gana {empleado[1]}")
    else:
        print(f"✅ Sueldo normal: {empleado[0]} gana {empleado[1]}")



# Dudas
# 1 Como ver los nombres de las columnas con las cuales trabajamos, sobre todo para identificar las llaves primarias
"""
# Paso 3: Vamos a ver con las tablas que contamos
tablas= cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
resultado_tablas=tablas.fetchall()
print(resultado_tablas)
# Paso 4 - Vamos a ver las distintas columnas con las que contamos en cada una de las tablas
# Tabla empleados
tabla_empleados= cursor.execute("SELECT * FROM empleados limit 2")
resultado_tabla_empleados=tabla_empleados.fetchall()
print(resultado_tabla_empleados)
"""
# Como se podra observar trate de ejcutar varios pasos antes, teniendo en cuenta que no sabías nada de la base de datos ni las tablas con las que trabajaba
# y me encontre que no sabía sacar al nombre de las columnas en sql







