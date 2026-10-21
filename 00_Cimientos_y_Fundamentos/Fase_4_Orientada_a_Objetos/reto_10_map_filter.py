"""
RETO 10: Procesadores Masivos (map y filter)

Contexto de Negocio:
En Data Science casi nunca aplicamos un cálculo a un solo número; lo aplicamos a 
millones de registros a la vez. Python (y Pandas) utiliza funciones escritas en lenguaje C 
para procesar listas enteras a la velocidad de la luz. Las más importantes son `map` y `filter`.

Tu Misión:
Tienes los siguientes precios de un e-commerce:
`precios_crudos = [50, 120, 30, 200, 90]`

1. MAP (La Transformación Masiva):
   - `map(funcion, lista)` inyecta una función a TODOS los elementos de una lista.
   - Crea la variable `precios_con_iva`.
   - Úsala junto a `list()` para mapear una función `lambda` (que multiplique por 1.21) 
     a toda la lista de `precios_crudos`.
     *(Sintaxis: `list(map(lambda x: ..., la_lista))`)*

2. FILTER (La Purga de Datos):
   - `filter(funcion, lista)` pasa la lista por un "colador". Si la función lambda da True, 
     el elemento sobrevive; si da False, es destruido.
   - Crea la variable `precios_altos`.
   - Usa `list()` y `filter()` con una `lambda` para extraer ÚNICAMENTE los precios 
     que sean estrictamente mayores a 100 de la lista original.

3. La Fábrica:
   - Imprime ambas listas nuevas para comprobar la transformación y la purga.
"""

# ==========================================
# 1. MAP (Transformación)
# ==========================================
precios_crudos = [50, 120, 30, 200, 90]
# Escribe tu mapeo masivo aquí...
precios_con_iva= list(map(lambda precio: precio *1.21, precios_crudos))
print(precios_con_iva)

# ==========================================
# 2. FILTER (Purga)
# ==========================================
# Escribe tu colador condicional aquí...
precios_altos= list(filter(lambda precio: precio>100, precios_crudos))
print(precios_altos)



# ==========================================
# 3. LA FÁBRICA (Pruebas)
# ==========================================
# Imprime ambas variables finales...
print()
# Duddas:
# la función map, ¿solo sirve para lista o cualquier iterable?, y ¿lo que hace es mapear todo el iterable como si fuera un bucle? y ¿depues aplicarle la funcion?
# En el caso de que cualquier iterable funcionara, ¿que pasa con los diccionarios?, ya que estos estan compuesto por una clave y un valor
# y ya que estamos entiendo que el método filter funciona como dice su nombre como un filtro,  pero volvemos al incio, ¿Sirve cualquier iterable? y de ser así ¿Que hacemos con el diccionario?
