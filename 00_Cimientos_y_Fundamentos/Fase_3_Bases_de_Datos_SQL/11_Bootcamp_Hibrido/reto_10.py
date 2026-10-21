"""
⚔️ Reto 10: El Jefe Final (El LEFT JOIN Híbrido) 

Negocio: El Gerente Comercial quiere ver a TODA la plantilla de empleados sin excepción. 
1- Si lograron una venta, quiere ver el producto. 
2- Si NO lograron nada, quiere ver el espacio en blanco para exhibirlos. 
(Recuerda que el INNER JOIN los habría desaparecido del reporte por no tener pareja). 

Arquitectura: Haz el cruce de tablas clásico de siempre, 
pero reemplaza la instrucción INNER JOIN por LEFT JOIN. 
Al extraer los datos a Python, los empleados que no han vendido llegarán con un valor de None. 
Adentro de tu bucle for, construye una lógica if / else:

Si el producto es None, imprime con rabia: "❌ [Nombre] tiene 0 ventas".
Si sí hay producto, imprime: "✅ [Nombre] logró vender [Producto]".
"""
import sqlite3

def reporte_ventas(ruta_entrada):
    """
    Esta función es encargada de verificar quien de los empleados a vendido y quien no
    Args:
    ruta_entrada: ruta relativa o absuluta de la base de datos de la empresa  
    Output:
    reporte_departamento_comercial: Reporte con el listado de empleados y sus resultados
    """
    try:
        conexion= sqlite3.connect(ruta_entrada)
        cursor= conexion.cursor()
        # Ver las tablas de nuestra base de datos en este caso asuminos que no tenemos el mapa
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tablas= cursor.fetchall()
        print(tablas)
        # Ahora que ya sabemos con las tablas que contamos vamos a por las relaciones entre tablas y sus columnas
        print("="*40)
        print("Columnas de la tabla de empleados")
        print("=" * 40)
        cursor.execute("PRAGMA table_info(empleados)")
        info_tabla_empleados= cursor.fetchall()
        for columna in info_tabla_empleados:
            print(f"{columna}\n")
        # Ahora vamos a ver la tabla de ventas
        print("="*40)
        print("Columnas de la tabla de ventas")
        print("=" * 40)
        cursor.execute("PRAGMA table_info(ventas)")
        info_tabla_ventas= cursor.fetchall()
        for columna in info_tabla_ventas:
            print(f"{columna}\n")
        # Ahora que ya tenemos todos nuestros datos vamos a pasar a resolver el problema de negocio
        cursor.execute("SELECT empleados.nombre, ventas.producto FROM empleados LEFT JOIN ventas ON empleados.id_empleado= ventas.id_empleado  WHERE empleados.departamento= 'Ventas'")
        resultado= cursor.fetchall()
        # instruccion en pyton  
        total_de_ventas_por_empleado= {} 
        for empleado in resultado:
            if empleado[0] not in total_de_ventas_por_empleado:
                total_de_ventas_por_empleado[empleado[0]]=0         
            if empleado[1]== None:
                print(f"❌ {empleado[0]} tiene 0 ventas")
            else:
                total_de_ventas_por_empleado[empleado[0]]+=1
                print(f"✅ {empleado[0]} logró vender {empleado[1]}")
        print(f'El total de ventas por empleado fue de {total_de_ventas_por_empleado}')
    except Exception as e:
        print(f'Ha ocurrido un error {e}')




# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
ruta_bd= r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db"
# ejecutando la funcion
reporte_ventas(ruta_bd)