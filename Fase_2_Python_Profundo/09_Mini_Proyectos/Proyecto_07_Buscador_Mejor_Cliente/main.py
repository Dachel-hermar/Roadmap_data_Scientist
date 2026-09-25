"""
========================================================================
MINI-PROYECTO 7: EL BUSCADOR DEL MEJOR CLIENTE (Algoritmo del Campeón)
========================================================================

CONTEXTO DE NEGOCIO:
Como analista de datos de un banco, te han pasado el archivo 'clientes_b2b.json'.
Es una lista de diccionarios con clientes corporativos.
Para cada cliente tienes: 'nombre', 'ingresos', y 'deuda_pendiente'.

El Director Comercial necesita saber:
"¿Quién es verdaderamente nuestro mejor cliente?"
No se trata del que tiene más ingresos brutos. El mejor cliente es el que 
tiene el mayor VALOR NETO (Ingresos menos Deuda).
También necesitan saber si hay algún cliente en "bancarrota" (que su deuda 
sea mayor que sus ingresos).

LA TEORÍA (La Regla del Acompañante):
Cuando haces el Algoritmo del Campeón, la variable numérica (dinero) siempre 
necesita una variable "acompañante" (nombre). 
Cuando el dinero es destronado, el nombre también DEBE cambiar DENTRO DEL MISMO IF.

    mejor_nombre = ""
    mejor_valor = 0
    
    # Adentro del bucle...
    if valor_actual > mejor_valor:
        mejor_valor = valor_actual     # Actualizo el récord
        mejor_nombre = nombre_actual   # ¡Me robo el nombre al mismo tiempo!

EL RETO:
Construye una función 'analizar_cartera(ruta_json)' que:
1. Defina las variables del Campeón (Mejor Cliente y su Valor Neto).
2. Abra el JSON y lo cargue (recuerda que será una Lista de Diccionarios).
3. Recorra la lista con un bucle 'for cliente in lista_clientes:'.
4. Por cada cliente, extraiga su nombre, ingresos y deuda.
5. Calcule el Valor Neto (ingresos - deuda_pendiente).
6. Aplique el Algoritmo del Campeón para encontrar al que tenga el Neto MÁS ALTO.
7. Al terminar el bucle, imprima un reporte que diga:
   "El mejor cliente es [Nombre] con un valor neto real de $[Valor]"

OPCIONAL (Bonus de Seniority):
¿Puedes agregar un Algoritmo de "El Peor Cliente" para encontrar al que tenga 
el valor neto MÁS BAJO (o negativo)? 
(Pista: El peor_valor no puede empezar en 0, porque hay valores negativos. 
Inícialo en un número gigante, como 9999999, para que cualquier valor lo destrone).
"""

import json

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================




# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# ruta = r"C:\...\Proyecto_07_Buscador_Mejor_Cliente\clientes_b2b.json"

# Llama a tu función
