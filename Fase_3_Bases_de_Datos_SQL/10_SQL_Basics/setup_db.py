import sqlite3
import os

# Ruta de la base de datos
db_path = r"C:\Roadmap_data_Scientist\10_SQL_Basics\empresa.db"

# Asegurarse de que el directorio existe
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Conectar a la base de datos (se creará automáticamente si no existe)
conexion = sqlite3.connect(db_path)
cursor = conexion.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    departamento TEXT NOT NULL,
    salario INTEGER NOT NULL,
    fecha_ingreso TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY,
    id_empleado INTEGER,
    monto INTEGER NOT NULL,
    producto TEXT NOT NULL,
    FOREIGN KEY(id_empleado) REFERENCES empleados(id_empleado)
)
''')

# Insertar datos de prueba
empleados_data = [
    (1, 'Ana Garcia', 'Ventas', 45000, '2023-01-15'),
    (2, 'Carlos Lopez', 'Marketing', 38000, '2023-03-10'),
    (3, 'Elena Martinez', 'Ventas', 52000, '2022-11-05'),
    (4, 'David Ruiz', 'IT', 60000, '2021-08-20'),
    (5, 'Sofia Torres', 'Marketing', 41000, '2024-02-01')
]

ventas_data = [
    (101, 1, 1500, 'Laptop Pro'),
    (102, 1, 800, 'Monitor 4K'),
    (103, 3, 2200, 'Servidor Cloud'),
    (104, 3, 150, 'Teclado Mecanico'),
    (105, None, 50, 'Cable HDMI') # Venta sin empleado asignado
]

# Limpiar tablas por si el script se corre dos veces
cursor.execute('DELETE FROM empleados')
cursor.execute('DELETE FROM ventas')

cursor.executemany('INSERT INTO empleados VALUES (?,?,?,?,?)', empleados_data)
cursor.executemany('INSERT INTO ventas VALUES (?,?,?,?)', ventas_data)

conexion.commit()
conexion.close()

print("✅ Base de datos 'empresa.db' creada y poblada con éxito.")
