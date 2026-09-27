"""
CAPA DE DATOS: database.py

Contexto de Negocio:
Este archivo será el motor de almacenamiento de tu ERP. Aquí NO va a existir ningún 
menú interactivo ni *prints* bonitos. Su única responsabilidad es hablar con el disco 
duro usando SQL. Si otra parte del programa necesita guardar algo, llamará a las 
funciones de este archivo.

Tu Misión (Cero Plantillas):
Construye las siguientes 3 funciones. Recuerda siempre el ciclo vital: 
Conectar -> Cursor -> Ejecutar -> Commit (si es DML) -> Cerrar.

1. Importación:
   - Importa la librería nativa de bases de datos.

2. Función 1: `conectar()`
   - Debe retornar una conexión a una base de datos llamada `inventario.db`.

3. Función 2: `crear_tabla_productos()`
   - Conéctate usando tu propia función `conectar()`.
   - Crea un cursor.
   - Ejecuta un `CREATE TABLE IF NOT EXISTS productos`.
   - Las columnas deben ser: 
     - `id` (Entero, Llave Primaria, Autoincremental)
     - `nombre` (Texto)
     - `precio` (Real/Decimal)
     - `supermercado` (Texto)
     - `fecha` (Texto)
   - Haz commit y cierra la conexión.

4. Función 3: `insertar_producto(nombre, precio, supermercado, fecha)`
   - Debe inyectar un nuevo producto en la tabla `productos`.
   - Recuerda usar `VALUES (?, ?, ?, ?)` para evitar inyecciones SQL, pasándole 
     la tupla con las variables.
   - Haz commit y cierra.

5. Prueba en Cuarentena:
   - Hasta el final del archivo, escribe `if __name__ == '__main__':`
   - Adentro de ese if, manda a llamar a `crear_tabla_productos()`.
   - Inyecta un producto de prueba usando `insertar_producto("Pollo", 5.99, "Mercadona", "2026-09-25")`.
"""

# ==========================================
# ESCRIBE TU CÓDIGO AQUÍ
# ==========================================
import sqlite3

def conectar():
    conexion= sqlite3.connect(r"C:\Roadmap_data_Scientist\Bootcamp_ERP_Personal\inventario.db")
    return conexion

def crear_tabla_productos():
    conexion_db= conectar()
    cursor= conexion_db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL,
    supermercado TEXT,
    fecha DATE

    )
    ''')
    conexion_db.commit() 
    conexion_db.close()

def insertar_producto(nombre, precio, supermercado, fecha):
    conex= conectar()
    cursor= conex.cursor()
    cursor.execute('''
    INSERT INTO productos (nombre, precio, supermercado, fecha) 
    VALUES (?, ?, ?, ?)
''', (nombre, precio, supermercado, fecha))
    conex.commit()
    conex.close()

def consultar_gasto_global():
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute("SELECT ROUND(SUM(precio),2) AS gasto_total_global FROM productos")
    producto= cursor.fetchall()
    conexion.close()
    return producto

def gasto_por_producto():
    conexion= conectar()
    cursor= conexion.cursor()
    cursor.execute("SELECT nombre, ROUND(SUM(precio),2) AS gasto_total FROM productos GROUP BY nombre")
    gasto=cursor.fetchall()
    conexion.close()
    return gasto

def registros_por_productos():
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute("SELECT nombre, COUNT(nombre) AS total_de_productos, supermercado FROM productos GROUP BY nombre ")
    cantidad= cursor.fetchall()
    conexion.close()
    return cantidad

def consultar_producto_especifico(nombre_del_producto):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute("SELECT nombre, ROUND(SUM(precio),2) FROM productos WHERE nombre LIKE ?",(f"%{nombre_del_producto}%",))
    resutado=cursor.fetchall()
    conexion.close()
    return resutado

def total_gastado_por_supermercado():
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute("SELECT supermercado, ROUND(SUM(precio),2) AS total_super FROM productos GROUP BY supermercado")
    resumen=cursor.fetchall()
    conexion.close()
    return resumen


if __name__ == '__main__':
    crear_tabla_productos()
    print (consultar_gasto_global())
    print(gasto_por_producto())
    print(registros_por_productos())
    print(consultar_producto_especifico("Pollo"))
      
    print(f"El Total por supermercado es:{total_gastado_por_supermercado()}")
