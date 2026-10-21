
"""
⚔️ Reto 2: El Auditor Comercial (SQL INNER JOIN + Python Contadores) 
Negocio: El CEO quiere una lista del éxito comercial, pero también necesita un recuento matemático absoluto 
de cuántos tratos fueron cruzados y confirmados. 
La Arquitectura Híbrida:
Usa SQL para tirar el INNER JOIN entre empleados y ventas. Extrae el nombre y el producto.
En Python, crea una variable contador_ventas = 0 (antes del bucle). 
Adentro del bucle, imprime quién vendió qué y súmale 1 al contador. Al terminar el bucle, Python debe declarar: 
"📊 Auditoría finalizada: Se cruzaron [contador] ventas exitosas en total.".
"""
import sqlite3
conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
cursor= conexion.cursor()
# Vamos a ver las PK de las tablas
consulta= cursor.execute("SELECT empleados.nombre, ventas.producto FROM empleados INNER JOIN ventas ON empleados.id_empleado= ventas.id_empleado")
resultado= consulta.fetchall()
print(resultado)
contador= 0
for empleado in resultado:
    print(f'El empleado {empleado[0]} vendio un {empleado[1]}')
    contador +=1
print(f"📊 Auditoría finalizada: Se cruzaron {contador} ventas exitosas en total.")