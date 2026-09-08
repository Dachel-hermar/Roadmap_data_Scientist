"""
🛍️ Simulador 3 de 3: El Gestor de Almacén (Sector: Retail)
Vamos al último simulador intensivo del día. Vamos a mezclar Condicionales, Bucles Simples y un concepto nuevo vital: Crear Listas Vacías y rellenarlas.

El Contexto: Eres el analista del almacén de una tienda de ropa. Tienes el registro del escáner que leyó los productos que acaban de llegar en el camión. 

Tus Datos: productos_entrantes = ["Camisa", "Pantalon", "Defectuoso", "Zapatos", "Defectuoso", "Gorra"]

La Regla de Negocio: El jefe de almacén necesita separar físicamente la mercancía en dos cajas distintas. 
Los productos buenos deben ir al inventario oficial, y los defectuosos deben ir al contenedor de devoluciones.

Tu Tarea: Escribe el código Python que mueva los datos de un lugar a otro:
"""

# Lista de productos
productos_entrantes = ["Camisa", "Pantalon", "Defectuoso", "Zapatos", "Defectuoso", "Gorra"]
# Crear una variable que guarde los productos buenos, esta variable sera una lista
inventario=[]
# productos malos
basura=[]
# vamos a crear una variable contadora de cuantos productos defectuosos llegaron
contador_basura=0

for item in productos_entrantes:
    """
    Creo el bucle for para recorrer la lista
    """
    if item == "Defectuoso":
        basura.append(item)
        contador_basura +=1
    else:
        inventario.append(item)
print(f'La lista de invenario oficial es la siguiente: {inventario}')
print(f'La lista de inventarios defectuoso es la siguiente: {basura}\n y la cantidad son de {contador_basura}')