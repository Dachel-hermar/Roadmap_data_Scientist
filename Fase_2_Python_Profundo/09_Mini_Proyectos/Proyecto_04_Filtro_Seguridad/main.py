"""
========================================================================
MINI-PROYECTO 4: EL INGENIERO DE SEGURIDAD (Listas + Diccionarios + JSON)
========================================================================

CONTEXTO DE NEGOCIO:
El departamento de Ciberseguridad te acaba de enviar los registros de acceso
al servidor de la empresa ('servidor_logs.json'). 

A diferencia del proyecto anterior donde el JSON era un gran Diccionario, 
este archivo JSON es una LISTA DE DICCIONARIOS. Esta es la estructura de 
datos más común en el mundo de las APIs y el Big Data.

Hay sospechas de un ataque cibernético de fuerza bruta durante la madrugada.
Tu misión es construir un filtro que analice miles de registros, aísle 
únicamente los intentos de acceso fallidos ("FAILED"), y los guarde en 
un archivo JSON nuevo para entregárselo a la policía cibernética.

LA TEORÍA (Listas de Diccionarios):
Cuando cargas este JSON con `json.load(file)`, lo que obtienes en la RAM 
es una Lista `[]`. Adentro de esa lista, hay varios Diccionarios `{}`.

Para analizarlo, SÍ necesitas un bucle `for`, porque necesitas recorrer 
la lista completa. En cada vuelta del bucle, tendrás en tus manos un 
diccionario individual.

    for registro in lista_de_logs:
        # 'registro' es un diccionario: {"usuario": "...", "status": "..."}
        # Aquí puedes usar tu lógica de Diccionarios: registro["status"]

EL RETO:
Construye una función 'aislar_amenazas(ruta_entrada, ruta_salida)' que:
1. Abra 'servidor_logs.json' en modo "r" y lo cargue en la RAM.
2. Cree una Lista vacía nueva llamada `alertas = []`.
3. Recorra los logs originales con un bucle `for`.
4. Si el 'status' de ese registro es igual a "FAILED", inyecta (.append) 
   ese diccionario entero dentro de tu nueva lista `alertas`.
5. Al terminar el bucle, abre el archivo 'ruta_salida' en modo "w".
6. Guarda tu lista de `alertas` en ese nuevo archivo usando `json.dump()`.

¡Este proyecto combina TODO: File Handling, Listas, Diccionarios y JSON!
Respira, usa el Print Debugging, y avanza paso a paso.
"""

import json

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def aislar_amenanzas(ruta_entrada, ruta_salida):
    """
    Lee un archivo Json con una lista de diccionarios, con intentos de ataques,
    actualiza los datos en una nueva lista y guarda los datos en un archivo nuevo.

    Args:
        ruta_entrada (str): Ruta absoluta o relativa del archivo JSON a leer y actualizar.
        ruta_salida (str) : Ruta absoluta o relativa del archivo Json a escribir 
                    
    Returns:
        lista_alertas (list): Devuelve una lista con las ALertas de hackeo
    """
    # vamos a abrir el servidor
    with open(ruta_entrada,"r") as f:
        mi_diccionario= json.load(f)
        print(mi_diccionario)
    # Vamos a crear la lista donde guardaremos las Alertas
    alertas = []
    cantidad_elementos = 0
    conteo_de_intentos_fallidos = 0
    
    for alerta in mi_diccionario:
        cantidad_elementos += 1
        if alerta['status'] == 'FAILED':
            alertas.append(alerta)
            conteo_de_intentos_fallidos += 1
            
    # Vamos a guardar la lista de diccionarios
    with open(ruta_salida, "w") as f:
        json.dump(alertas, f, indent=4)
        
    return cantidad_elementos, conteo_de_intentos_fallidos

# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
ruta_logs = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_04_Filtro_Seguridad\servidor_logs.json"
ruta_alertas = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_04_Filtro_Seguridad\alertas_seguridad.json"

# Llama a tu función
total, hackeos = aislar_amenanzas(ruta_logs, ruta_alertas)

print("=" * 40)
print("🛡️ REPORTE DE CIBERSEGURIDAD")
print("=" * 40)
print(f"Total de logs analizados: {total}")
print(f"Amenazas neutralizadas:   {hackeos}")
print(f"Base de datos de la policía generada con éxito.")
print("=" * 40)
