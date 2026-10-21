import sqlite3
conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
cursor= conexion.cursor()
cursor.execute("SELECT nombre, departamento, salario FROM empleados WHERE departamento= 'Ventas' AND salario>= 45000")
resultados= cursor.fetchall()
print(resultados)
for fila in resultados:
    print(f"El empleado {fila[0]} cobra {fila[2]}")
conexion.close()