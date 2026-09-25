"""
⚔️ Reto 7: El Operativo de Limpieza (DML: DELETE) 
Negocio: ¿Recuerdas aquel triste "Cable HDMI" que está registrado en la tabla de ventas pero que no tiene ningún empleado asignado? 
Esa es "data basura". El equipo de QA pide eliminar ese registro. 

Arquitectura: Vas a usar el comando DELETE FROM tabla WHERE condicion. 
En el mundo SQL, para detectar vacíos se usa la condición especial id_empleado IS NULL. 
Alerta de Ingeniero: Como vas a alterar permanentemente la base de datos, 
después del cursor.execute(...) tienes que sellar el pacto con un conexion.commit(). 
Si no haces el commit, el cable no se borrará. 
(Y mucho cuidado: Si se te olvida poner el WHERE, ¡borrarás toda la tabla de ventas!).
"""
import sqlite3
conexion = sqlite3.connect(r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db")
cursor= conexion.cursor()
cursor.execute("PRAGMA table_info('ventas')")
columnas= cursor.fetchall()
#print(columnas)

cursor.execute("SELECT * FROM ventas LIMIT 5")
tabla_ventas= cursor.fetchall()
#print(tabla_ventas)

try:
    cursor.execute("DELETE FROM ventas WHERE id_empleado is NULL")
except Exception as e:
    print(f"Ha ocurrido un error {e} ¡CORRIGELO!")
      
print("===CERRANDO CONEXIÓN CON LA BASE DE DATOS Y GUARDANDO LOS CAMBIOS===")
conexion.commit()



