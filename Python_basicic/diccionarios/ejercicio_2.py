"""
💻 Reto de Nivel Medio: El Diccionario Acumulador (El Group By)
Ha llegado el momento de traducir a código puro el superpoder que dominaste en la Fase 2 (Lógica en papel): usar un Diccionario para agrupar y contar bases de datos masivas.

El Contexto: Eres el analista de inventario de un supermercado. Te acaban de pasar la cinta cruda de la caja registradora con todo lo que se vendió en la última hora, y necesitas hacer el reporte agrupado. Tus Datos: caja_registradora = ["Manzana", "Pera", "Manzana", "Platano", "Manzana", "Pera", "Uva"]

Tu Tarea:

Crea un diccionario vacío llamado conteo_ventas = {}.
Haz el bucle simple para recorrer la lista de la caja_registradora.
Dentro del bucle, vas a necesitar un bloque if/else usando la palabra reservada in (que en Python sirve para preguntar si algo ya existe dentro de una caja).
La Lógica de Negocio (Piénsalo bien):
Si la fruta ya existe como clave registrada en el diccionario, simplemente le sumas 1 a su cantidad.
Si la fruta aún NO existe en el diccionario (porque es la primera vez que pasa por la caja registradora), entonces debes crear la clave nueva en el diccionario y asignarle un 1 inicial.
Al finalizar el bucle, imprime tu diccionario para ver el conteo agrupado por categorías.
"""

# Datos
caja_registradora = ["Manzana", "Pera", "Manzana", "Platano", "Manzana", "Pera", "Uva"]

# Creo el diccionario
conteo_ventas = {}

# Creo el bucle for para iterar encima de la lista
for item in caja_registradora:
    print(item)
    if item not in conteo_ventas:
        conteo_ventas[item] =1
    else:
        conteo_ventas[item]+=1
print(f"El conteo de ventas es: {conteo_ventas}")