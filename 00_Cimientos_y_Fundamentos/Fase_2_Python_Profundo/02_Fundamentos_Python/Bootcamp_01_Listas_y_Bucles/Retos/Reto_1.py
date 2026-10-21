"""
💻 Reto 1/10: La Peor Caída Diaria (Basado en LeetCode - Sector Trading)
El Contexto: En finanzas bursátiles, a los inversores no solo les importa cuánto ganan, sino cuál fue el susto más grande que se llevaron. 
Necesitan saber cuál fue la peor "Caída Diaria" (Daily Drawdown) de su cartera. 
Tus Datos: Tienes el precio de una acción durante 6 días consecutivos. 

precios_accion = [100, 120, 80, 90, 85, 130]

Tu Tarea: Escribe el algoritmo que encuentre la **mayor pérdida de dinero** ocurrida exclusivamente de un día para el siguiente.

Día 0 al 1 (100 a 120): Ganó 20 (no nos importa).
Día 1 al 2 (120 a 80): Cayó 40.
Día 3 al 4 (90 a 85): Cayó 5. Resultado final esperado en pantalla: La peor caída fue de 40 euros.

"""

# Datos de precios de la accion en cuestión
precios_accion = [100, 120, 80, 90, 85, 130]

# Variable Campeón
mayor_caida= 0

# Creación de un buvle for para recorrer la lista
for item in range(len(precios_accion)-1):
    """
    Como debo de comparar un precio con otro necesito la posicion(indice) de estso
    len(precios_accion): Calculo el tamaño de la lista
    range(len(precios_acción)): Creo el indice de la mismae itero la misma cantidad de veces que el tamaños de la lista
    Por cada iteración es su indice
    item: indice de la lista en cada iteracion
    """
    
    if precios_accion[item] > precios_accion[item +1]:
        diferencia_aritmetica = precios_accion[item] - precios_accion[item +1]
        if diferencia_aritmetica > mayor_caida:
            mayor_caida = diferencia_aritmetica

print(f'La mayor caída del precio fue de {mayor_caida}')
