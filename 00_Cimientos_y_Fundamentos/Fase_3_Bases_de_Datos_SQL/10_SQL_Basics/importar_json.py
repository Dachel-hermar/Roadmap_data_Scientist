import json
import sqlite3

# 1. Conexión a la base de datos (Te la regalo yo)
conexion = sqlite3.connect(r"C:\Roadmap_data_Scientist\10_SQL_Basics\empresa.db")
cursor = conexion.cursor()

# 2. TU RETO DE PYTHON: Abrir el JSON, leerlo y extraer los datos
ruta_json = r"C:\Roadmap_data_Scientist\10_SQL_Basics\nuevos_empleados.json"

# ---> ESCRIBE TU CÓDIGO PYTHON AQUÍ <---
# Pista: Abre el archivo JSON.
# Usa un bucle FOR para iterar sobre los empleados.
# Extrae el id, nombre, departamento, salario y fecha. ¡Cuidado con los diccionarios anidados!
with open(ruta_json, "r") as archivo_json:
    datos_empleados = json.load(archivo_json)
    #print(datos_empleados)
for empleado in datos_empleados:
    id = empleado['id_empleado']
    nombre = empleado['perfil']['nombre_completo']
    departamento= empleado['perfil']['area_asignada']
    salario= empleado['finanzas']['salario_base']
    fecha = empleado['fecha_ingreso']
    


    


# 3. TU RETO SQL: Por cada empleado en el bucle, debes ejecutar un INSERT INTO
# Pista de sintaxis: cursor.execute(f"INSERT INTO empleados VALUES ({id}, '{nombre}', '{departamento}', {salario}, '{fecha}')")
    try:
        cursor.execute(f"INSERT INTO empleados VALUES ({id}, '{nombre}', '{departamento}', {salario}, '{fecha}')")
    except sqlite3.IntegrityError:
        print(f"⚠️ Alerta: El ID {id} de {nombre} ya existe en la bóveda. Saltando...")


# 4. Guardar los cambios (Te lo regalo yo)
conexion.commit()
conexion.close()
print("✅ Proceso ETL Completado: Empleados inyectados en la bóveda SQL.")
