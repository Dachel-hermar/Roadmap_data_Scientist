
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()



def conectar():
    DATABASE_URL = os.getenv("DATABASE_URL")
    conexion = psycopg2.connect(DATABASE_URL)
    return conexion

def crear_tabla_financiera(tabla):
    conexion_db= conectar()
    cursor= conexion_db.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {tabla}(
    id SERIAL PRIMARY KEY,
    concepto TEXT NOT NULL,
    monto REAL NOT NULL,
    fecha DATE NOT NULL,
    categoria TEXT NOT NULL
    )
    ''')
    
    conexion_db.commit() 
    conexion_db.close()

def crear_tabla_metas_financieras():
    conexion_db= conectar()
    cursor= conexion_db.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS Metas_Financieras(
    id SERIAL PRIMARY KEY,
    nombre_categoria TEXT UNIQUE NOT NULL,
    limite_maximo REAL NOT NULL

    )
    ''')
    
    conexion_db.commit() 
    conexion_db.close()

def insertar_valores_metas_financieras(nombre_categoria, limite_maximo):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f'''
    INSERT INTO Metas_Financieras(nombre_categoria, limite_maximo)
    VALUES (%s,%s)
''', (nombre_categoria, limite_maximo ))
    conexion.commit()
    conexion.close()






    
def insertar_valores(tabla,concepto, monto, fecha, categoria):
    conex= conectar()
    cursor= conex.cursor()
    cursor.execute(f'''
    INSERT INTO {tabla} (concepto, monto, fecha, categoria) 
    VALUES (%s, %s, %s, %s)
''', (concepto, monto, fecha, categoria))
    conex.commit()
    conex.close()


# Suma total de ingresos o gastos
def valores_totales(tabla):
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute(f"SELECT ROUND(SUM(monto):: numeric,2) AS ingresos_totales FROM {tabla}")
    resultado= cursor.fetchall()
    conexion.close()
    return resultado

# Consultar gasto o ingreso por categoria
def consultar_categorias(tabla):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"SELECT categoria, ROUND(SUM(monto):: numeric,2) FROM {tabla} GROUP BY categoria")
    resultado=cursor.fetchall()
    conexion.close()
    return resultado

# Consulta por concepto
def concepto_unitario(tabla, nombre_concepto):
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"SELECT concepto, ROUND(SUM(monto):: numeric,2) FROM {tabla} WHERE concepto ILIKE %s GROUP BY concepto",(f"%{nombre_concepto}%",) )
    resultado=cursor.fetchall()
    conexion.close()
    return resultado


def consultar_gastos_vs_metas():
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute(f"""SELECT Gastos.categoria, ROUND(SUM(Gastos.monto)::numeric, 2) AS gastado, Metas_Financieras.limite_maximo
    FROM Gastos
    INNER JOIN Metas_Financieras 
    ON Gastos.categoria = Metas_Financieras.nombre_categoria
    GROUP BY Gastos.categoria, Metas_Financieras.limite_maximo;""")
    resultado=cursor.fetchall()
    conexion.close()
    return resultado





if __name__ == "__main__":
    crear_tabla_metas_financieras()
    insertar_valores_metas_financieras("Varios", 30)
    insertar_valores_metas_financieras("Fijos", 500)
    
    





