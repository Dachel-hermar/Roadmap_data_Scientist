"""
⚔️ Reto 6: Detectando la Fuga de Capital (SQL GROUP BY + HAVING) 
Contexto de Negocio: El CEO quiere auditar solo a los departamentos que estén gastando más de $80,000 dólares en salarios acumulados. 
Los departamentos baratos no le interesan. 
Arquitectura: Deja que el motor SQL haga todo el trabajo pesado. 
Diseña una consulta poderosa usando GROUP BY para separar a los grupos y filtrándolos con la temida cláusula estadística HAVING. 
Python simplemente debe agarrar a los departamentos culpables y publicarlos en la terminal
"""
import sqlite3
path_bd= r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db"
conexion= sqlite3.connect(path_bd)
cursor= conexion.cursor()
cursor.execute("SELECT departamento, SUM(salario) AS salario_total FROM empleados GROUP BY departamento HAVING SUM(salario)> 80000  ")
resultado= cursor.fetchall()
departamentos=[]
salarios=[]
for gasto in resultado:
    departamentos.append(gasto[0])
    salarios.append(gasto[1])
    
print(f'Los departamentos que gastan en salario más de 80000 dólares son los siguientes:')
print(f'{"=" * 20} DEPARTAMENTOS  {"=" * 20}')
print(departamentos)
print(f'{"=" * 20} Gastos {"=" * 20}')
print(salarios)