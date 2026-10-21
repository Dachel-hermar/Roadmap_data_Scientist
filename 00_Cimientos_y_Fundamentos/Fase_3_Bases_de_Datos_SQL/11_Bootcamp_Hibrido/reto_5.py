"""
⚔️ Reto 5: La Prueba del Espejo de Auditoría (SQL SUM() vs Python Acumulador) 
Contexto de Negocio: El área de Contabilidad quiere saber el Gasto Total de Nómina de toda la empresa, 
pero el auditor exige que el cálculo se haga por dos vías distintas para detectar fraudes. 
Arquitectura Híbrida (Haz ambas en el mismo archivo):

La Vía SQL: Haz que la base de datos calcule el total absoluto usando su motor matemático interno (SELECT SUM(...)). 
Extrae ese único dato a Python.
La Vía Python: Extrae la columna cruda de todos los salarios usando SQL simple (SELECT salario...). 
Luego, en Python, usa tu lógica de la Fase 2 (una variable total = 0 y un bucle for) para sumar moneda por moneda. 
¡Ambos métodos deben imprimir exactamente el mismo número en tu terminal!
"""
import sqlite3
# Primera vía
def auditoria_nomina(ruta_bd, reporte_final):
    try:
        conexion= sqlite3.connect(ruta_bd)
        cursor= conexion.cursor()
    except Exception as e:
        print(f'Se ha detactado un error al descargar los datos de la base de datos {e}')
    cursor.execute("SELECT SUM(salario) as total_salario FROM empleados")
    resultado= cursor.fetchall()
    # guardar el resultado en una variable de Python llamada Gasto Total
    total=0
    if resultado:
        total=resultado[0][0]
        print(type(total))
    print(f'El gasto ttal de la empresa en salario es de {total}')

    print("=" * 40)
    print("Segunda Vía de ejecución")
    print("="*40)

    cursor.execute("SELECT salario FROM empleados")
    salario= cursor.fetchall()
    #print(salario)
    gasto_total= 0
    for gasto in salario:
        gasto_total+=gasto[0]
    print(f'El gasto ttal de la empresa en salario es de {gasto_total}')


    if total==gasto_total:
        with open(reporte_final,"w") as informe_contabilidad:
            informe_contabilidad.write(f'Informe para el departamento de Contabilidad\n Despúes de un análisis por dos vías distintas para detectar fraude se detecto que: No hay indicios de fraude\n Por lo que el gasto total en nómina de la empresa es de: {gasto_total}')

    
                                       
        




# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
ruta_crudo= r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\empresa.db"
ruta_final= r"C:\Roadmap_data_Scientist\Fase_3_Bases_de_Datos_SQL\11_Bootcamp_Hibrido\gasto_total"

auditoria_nomina(ruta_crudo, ruta_final)