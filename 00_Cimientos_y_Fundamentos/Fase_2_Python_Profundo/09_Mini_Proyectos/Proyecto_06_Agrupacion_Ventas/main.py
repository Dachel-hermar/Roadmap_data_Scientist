"""
========================================================================
MINI-PROYECTO 6: EL MOTOR DE AGRUPACIÓN (Simulador de GROUP BY)
========================================================================

CONTEXTO DE NEGOCIO:
El departamento de Finanzas te ha enviado un archivo 'ventas.csv'. 
Tiene miles de transacciones de distintos departamentos.
No quieren saber cuánto se vendió en total. 
Quieren saber:
"¿Cuánto dinero generó EXACTAMENTE cada Categoría?"

"¿Qué categoría de productos está manteniendo viva a la empresa 
y dónde deberíamos inyectar el presupuesto de marketing el próximo mes?"

En SQL o Pandas, esto se hace con un comando mágico llamado 'GROUP BY'.
Pero como eres un Arquitecto de Datos, hoy vas a programar el algoritmo 
matemático que hace funcionar a ese comando mágico por debajo.

LA TEORÍA (Acumuladores Dinámicos):
En el Proyecto 05, usaste un Diccionario para contar palabras (sumabas +1).
Hoy usarás un Diccionario para SUMAR DINERO.
La llave será la 'categoria' y el valor será el 'precio' acumulado.

    if categoria in ingresos_por_categoria:
        ingresos_por_categoria[categoria] += precio_de_esta_venta
    else:
        ingresos_por_categoria[categoria] = precio_de_esta_venta

EL RETO:
Construye una función 'agrupar_ventas(ruta_csv, ruta_json)' que:
1. Cree tu diccionario acumulador vacío (¡RECUERDA DÓNDE PONERLO!).
2. Abra el archivo 'ventas.csv' y lea sus líneas.
3. Evade la cabecera (la primera línea que dice id_venta,categoria...).
4. En un bucle, procesa cada línea:
   - Quita los saltos de línea y divídela por comas.
   - Extrae la categoría y el precio.
   - CUIDADO: El precio viene como Texto (String). Debes convertirlo 
     a un número (float o int) para poder sumarlo matemáticamente.
5. Usa la lógica del Acumulador de Diccionarios para sumar los precios 
   por categoría.
6. Guarda tu Diccionario final en un archivo 'reporte_financiero.json'.

¡Combina la lectura de CSV (Proyecto 2) con los Acumuladores (Proyecto 5)!
"""

import json

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def agrupar_ventas(ruta_csv, ruta_json):
    # Crear un diccionario vacío para acumular los ingresos por categoría de productos
    ingresos_por_ventas= {}
    
    with open(ruta_csv, "r") as archivo_csv:
        # leer todas las líneas del csv
        lineas= archivo_csv.readlines()
        # Evitar la cabecera
        # Antes vamosa vizualizar nuestros datos
        #print(lineas)
        # Dado que la cabecera de nuestro archivo csv es la primera linea esa al hacer un bucle para recorrer cada linea la vamos a saltar con un condicional if
        
        for linea in lineas:
            if linea.startswith('id_venta'):
                continue
            #print(linea)
            # vamos a quitar los slatos de lineas y dividir el texto, sustituyendo las comas por espacios
            datos= linea.strip().split(",")
            #print(datos)
            # Ahora vamos a extraer la categoría y el precio de esta
            # Dada que es una lista de elementos las recorremos
            categoria=datos[1]
            precio= int(datos[-1])

            if categoria in ingresos_por_ventas:
                ingresos_por_ventas[categoria]+= precio
                
                
            else:
                ingresos_por_ventas[categoria]=precio

        

        
                
            

    # Ahora vamos a guardar nuestro diccionario en un archivo .json
    with open(ruta_json, "w") as reporte:
        json.dump(ingresos_por_ventas, reporte, indent=4)
        
    # ==========================================
    # ALGORITMO DEL CAMPEÓN (Encontrar el Máximo)
    # ==========================================
    categoria_estrella = ""
    dinero_maximo = 0
    
    # .items() nos permite recorrer las llaves y los valores al mismo tiempo
    for categoria, dinero in ingresos_por_ventas.items():
        if dinero > dinero_maximo:
            dinero_maximo = dinero
            categoria_estrella = categoria
            
    return ingresos_por_ventas, categoria_estrella, dinero_maximo


# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
ruta_csv = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_06_Agrupacion_Ventas\ventas.csv"
ruta_json = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_06_Agrupacion_Ventas\reporte_financiero.json"

# Llama a tu función
informe, cat_top, ingresos_top = agrupar_ventas(ruta_csv, ruta_json)

print("=" * 40)
print("📊 REPORTE FINANCIERO (GROUP BY)")
print("=" * 40)
print(f"Ingresos Totales por Categoría:")
for cat, dinero in informe.items():
    print(f" - {cat}: ${dinero} USD")
print("-" * 40)
print(f"🏆 CATEGORÍA ESTRELLA: {cat_top} (${ingresos_top} USD)")
print(f"💡 Decisión de Negocio: Inyectar presupuesto de marketing en {cat_top}.")
print("=" * 40)
