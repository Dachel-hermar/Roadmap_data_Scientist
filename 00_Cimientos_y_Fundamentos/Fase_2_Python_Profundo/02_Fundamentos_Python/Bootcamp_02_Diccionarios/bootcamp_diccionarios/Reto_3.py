"""
💻 Reto 3/10: Ofertas Relámpago (Sector E-Commerce)
El Contexto: Eres el Data Analyst del almacén de una tienda de electrónica. 
El departamento de marketing necesita lanzar una campaña de "Ofertas Flash", 
y te piden aislar rápidamente en una nueva base de datos todos los productos que cuesten estrictamente menos de 100 euros. 
Tus Datos Crudos:

python


catalogo = {
    "Laptop": 1200,
    "Mouse": 25,
    "Monitor": 300,
    "Teclado": 45,
    "Auriculares": 80,
    "Silla": 150
}
Tu Tarea Lógica:

Crea un diccionario vacío llamado ofertas_flash = {} que funcionará como tu caja limpia.
Abre un bucle for para leer a las dos partes del catalogo a la vez.
Evalúa con tu if: Si el precio de ese artículo es < 100...
La magia de hoy: ...guarda ese artículo en tu caja limpia. (Recordatorio de oro: Los diccionarios no tienen un .append(). Para inyectarle datos nuevos a un diccionario, se usa la sintaxis de asignación directa: diccionario_limpio[clave] = valor).
Al finalizar el bucle, imprime tu nuevo diccionario ofertas_flash para enviárselo a Marketing. (Debería contener solo el Mouse, el Teclado y los Auriculares).
"""
# Catalogo de precios de productos
catalogo = {
    "Laptop": 1200,
    "Mouse": 25,
    "Monitor": 300,
    "Teclado": 45,
    "Auriculares": 80,
    "Silla": 150
}
# Diccionario vacío para guardar los productos
ofertas_flash = {}
# Bucle for para recorrer los diccionarios y sacar los productos que cuestan menos de 100 euros
for key, values in catalogo.items():
    if values < 100:
        ofertas_flash[key]=values


print(ofertas_flash)
