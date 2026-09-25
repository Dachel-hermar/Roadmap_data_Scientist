"""
⚔️ Reto 9: El Buscador de Patrones (LIKE) 

Negocio: Seguridad Comercial busca a una empleada sospechosa para interrogarla, 
pero lo único que recuerdan de su expediente es que su nombre empezaba con la letra 'E'. 
Arquitectura: SQL no solo busca palabras exactas, también busca fragmentos usando comodines. 
Ejecuta: SELECT nombre FROM empleados WHERE nombre LIKE 'E%'. 
(El símbolo de porcentaje significa "no me importa qué letras sigan después de la E"). 
Usa el fetchall() y haz que Python denuncie el nombre de la sospechosa en la terminal.
"""
import sqlite3
conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
cursor= conexion.cursor()
cursor.execute("SELECT nombre FROM empleados WHERE nombre LIKE 'E%'")
resultado= cursor.fetchall()
print(f'El nombre de la empleada es {resultado[0][0]}')
