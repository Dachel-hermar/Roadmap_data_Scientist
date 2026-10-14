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
import psycopg2
from dotenv import load_dotenv
import os
# Esto abre la caja fuerte del archivo .env al encender el sistema
load_dotenv()


def conectar():
    DATABASE_URL = os.getenv("DATABASE_URL")
    conexion = psycopg2.connect(DATABASE_URL)
    return conexion

def crear_tabla_productos(tabla):
    conexion_db= conectar()
    cursor= conexion_db.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {tabla}(
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    cantidad INTEGER,
    precio REAL,
    supermercado TEXT,
    fecha DATE

    )
    ''')
    
    conexion_db.commit() 
    conexion_db.close()

def crear_nueva_columnas(tabla, columna, tipo, predeterminado=None):
    conexion_db= conectar()
    cursor= conexion_db.cursor()
    # Vamos a verificar que la columna no exista antes de intentar crearla
    nueva_columna=cursor.execute(f'''
    ALTER TABLE {tabla}
    ADD COLUMN {columna} {tipo} DEFAULT {predeterminado}

    ''')
    conexion_db.commit() 
    conexion_db.close()

def insertar_producto(tabla,nombre, cantidad, precio, supermercado, fecha):
    conex= conectar()
    cursor= conex.cursor()
    cursor.execute(f'''
    INSERT INTO {tabla} (nombre, cantidad, precio, supermercado, fecha) 
    VALUES (%s, %s, %s, %s, %s)
''', (nombre, cantidad, precio,  supermercado, fecha))
    conex.commit()
    conex.close()

def borrar_registros(tabla, id_registro):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"DELETE FROM {tabla} WHERE id = %s", (id_registro,))
    conexion.commit()
    conexion.close()

def modificar_precio(tabla,id_registro,nuevo_precio):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"UPDATE {tabla} SET precio = %s WHERE id = %s", (nuevo_precio, id_registro))
    conexion.commit()
    conexion.close()

def consultar_gasto_global(tabla):
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute(f"SELECT ROUND(SUM(cantidad * precio):: numeric,2) AS gasto_total_global FROM {tabla}")
    producto= cursor.fetchall()
    conexion.close()
    return producto

def gasto_por_producto(tabla):
    conexion= conectar()
    cursor= conexion.cursor()
    cursor.execute(f"SELECT nombre, ROUND(SUM(cantidad * precio):: numeric,2) AS gasto_total FROM {tabla} GROUP BY nombre")
    gasto=cursor.fetchall()
    conexion.close()
    return gasto

def registros_por_productos(tabla):
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute(f"SELECT nombre,supermercado, SUM(cantidad) AS total_de_productos FROM {tabla} GROUP BY nombre, supermercado")
    cantidad= cursor.fetchall()
    conexion.close()
    return cantidad

def consultar_producto_especifico(tabla, nombre_del_producto):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"SELECT nombre, ROUND(SUM(cantidad * precio)::numeric,2) FROM {tabla} WHERE nombre ILIKE %s GROUP BY nombre",(f"%{nombre_del_producto}%",))
    resutado=cursor.fetchall()
    conexion.close()
    return resutado

def total_gastado_por_supermercado(tabla):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"SELECT nombre, supermercado, ROUND(SUM(cantidad * precio)::numeric,2) AS total_super FROM {tabla} GROUP BY supermercado, nombre")
    resumen=cursor.fetchall()
    conexion.close()
    return resumen


if __name__ == '__main__':
    crear_nueva_columnas("gasto")