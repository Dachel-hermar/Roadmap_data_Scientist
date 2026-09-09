"""
💻 Reto de Integración 2/6: El Analista de Inventario (Mutación JSON)

El Contexto de Negocio: Eres el responsable de los Datos del almacén de una gigantesca tienda de informática. 
Te pasan la base de datos del inventario actual en formato JSON. 
Tu Jefe necesita que diseñes un script que audite y actualice automáticamente el "estado" de los productos 
que se han quedado sin existencias, para que la página web deje de venderlos.
"""
inventario = [
    {"producto": "Laptop", "stock": 10, "estado": "Disponible"},
    {"producto": "Mouse", "stock": 0, "estado": "Disponible"},
    {"producto": "Teclado", "stock": 5, "estado": "Disponible"},
    {"producto": "Monitor", "stock": 0, "estado": "Disponible"}
]

# Crear el bucle para que recorra la la base de datos de productos
for producto in inventario:
    if producto.get("stock")<=0:
        producto["estado"]= "Agotado"

print(inventario)

# Resultados
# Ya este empieza a ser un poco más díficil, pero no en lógica si no en sintaxis
# Problema que me encontre, al llamar a la llave estado, de la variable iteradora producto producto.get("estado")="Agotado", me lanzaba este error
""" File "c:\Roadmap_data_Scientist\03_Retos_Integracion_JSON\Reto_2_inventario.py", line 19
    producto.get("estado")= "Agotado"
    ^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?"""
# Es decir un error de sintaxis por lo que me di cuenta que el método .get(), te sirve para acceder al valor de una clave, y compararlo
# Pero no se te permite a traves de este mismo modificarlo, solamente modifcas, llamando directamente a la clave de ña variable
# Otra cosa fue otro error
# estaba tratando de cambiar el valor directamente de la base de datos que está en formato Json. por lo que me lanzaba otro error
"""  File "c:\Roadmap_data_Scientist\03_Retos_Integracion_JSON\Reto_2_inventario.py", line 19, in <module>
    inventario["estado"]== "Agotado"
    ~~~~~~~~~~^^^^^^^^^^
TypeError: list indices must be integers or slices, not str
"""
# Un error de tipo, este fue más fácil de darse uno cuenta

# me gusto mucho, porque me hizo parar un segundo y pensar
# Pero al final resuleto en nada