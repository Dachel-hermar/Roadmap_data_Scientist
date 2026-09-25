"""
⚔️ Reto 3: El Desafío del Becario (SQL SELECT + Python Diccionarios) 
Negocio: Se cayó el sistema de base de datos. 
¡Está estrictamente prohibido usar las cláusulas GROUP BY o COUNT() en SQL para este reto! 
Tienes que salvar el reporte de RRHH agrupadando a la gente "a la antigua", usando la RAM de Python. 

La Arquitectura Híbrida:
Usa SQL solo para extraer en bruto el departamento y el nombre de todos los empleados (SELECT ...).
En Python, crea un Diccionario vacío (ej. censo_rrhh = {}).
Adentro del bucle for, saca del baúl de los recuerdos tu lógica de la Fase 2: 
Construye el código para verificar si el departamento ya existe en el diccionario; 
si no existe, créalo con valor 1. Si ya existe, súmale 1. 
(¡Demuéstrame que aún dominas los diccionarios!). Al final, imprime el diccionario resultante.
"""
import sqlite3
path_bd= r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db"
conexion = sqlite3.connect(path_bd)
cursor= conexion.cursor()

consulta = cursor.execute("SELECT nombre, departamento FROM empleados")
resultado= consulta.fetchall()

censo_rrhh = {}
for empleado in resultado:
    if empleado[1] in censo_rrhh:
        censo_rrhh[empleado[1]] +=1
    else:
        censo_rrhh[empleado[1]]=1
print(f'El resultado del censo fue el siguiente {censo_rrhh}')


