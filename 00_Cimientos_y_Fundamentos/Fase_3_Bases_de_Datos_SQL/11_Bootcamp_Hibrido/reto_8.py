"""
⚔️ Reto 8: El Ajuste Inflacionario (DML: UPDATE) 
Negocio: Para frenar la fuga de talentos, RRHH dictaminó un aumento fijo de $2000 dólares, 
pero única y exclusivamente para los empleados que pertenecen a 'Marketing'. 
Arquitectura: Vas a usar el comando UPDATE tabla SET columna = columna + X WHERE condicion. 
Inyecta el comando, sella el puente con commit(), y 
luego usa Python para hacer un SELECT rápido e imprimir a Carlos y a Sofía para comprobar que ahora son más ricos.
"""
import sqlite3
try:
    conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
    cursor= conexion.cursor()
    cursor.execute("UPDATE empleados SET salario= salario + 2000 WHERE departamento='Marketing'")
    cursor.execute("SELECT nombre, salario FROM empleados WHERE departamento='Marketing'")
    salario_actualizado=cursor.fetchall()
    print(salario_actualizado)
except Exception as e:
    print(f'Ha ocurrido un error de {e}')
print("===Cerrando conexión y actualizando la base de datos===")
conexion.commit()


