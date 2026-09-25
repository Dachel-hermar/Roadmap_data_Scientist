"""
Reto 1: Los "Atajos" del Arquitecto (Enumerate y Zip)

Contexto:
Hasta ahora, hemos usado lógica algorítmica dura para resolver problemas. 
Hacerlo por el "camino largo" forjó tu lógica matemática. 
Ahora que entiendes el porqué de las cosas, Python te regala "atajos" nativos 
para escribir código más elegante (Pythonic Code).

1. ENUMERATE: Sirve para recorrer una lista y obtener TANTO EL ÍNDICE (0, 1, 2...) 
COMO EL VALOR al mismo tiempo.
Ejemplo: for indice, valor in enumerate(lista):

2. ZIP: Sirve para recorrer DOS o más listas al mismo tiempo, en paralelo, 
como si cerraras una cremallera.
Ejemplo: for nombre, edad in zip(lista_nombres, lista_edades):
"""

# =========================================================
# TAREA A: Enumerate (El Analista de Rankings)
# =========================================================
# Tienes una lista de competidores en orden de llegada. 
# Imprime un ranking que diga: "Puesto 1: Carlos", "Puesto 2: Ana", etc.
# (Pista: Los índices empiezan en 0, ¡tendrás que sumarle 1 al imprimir el puesto!)

competidores = ["Carlos", "Ana", "Luis", "Marta"]

print("--- RANKING DE COMPETIDORES ---")
# Escribe tu bucle for usando enumerate() aquí...
for puesto, nombre in enumerate(competidores):
    print(f'Puesto {puesto+1}: {nombre}')




# =========================================================
# TAREA B: Zip (El Fusionador de Datos)
# =========================================================
# Tienes dos listas separadas que te mandó Ventas. Son datos correlacionados.
# Tu Jefe necesita fusionarlas en un solo Diccionario limpio y relacional.

productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [1200, 25, 45, 300]

catalogo_final = {}

print("\n--- CATÁLOGO FUSIONADO ---")
# Escribe tu bucle for usando zip() aquí...
# Lógica: Asigna el precio como valor de la llave del producto en el catálogo.
for precio, producto in zip(precios,productos):
    catalogo_final[producto]=precio


print(catalogo_final)
