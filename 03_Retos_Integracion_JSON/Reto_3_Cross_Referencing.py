"""
💻 Reto de Integración 3/6 (V2): La Pasarela de Pagos (Cross-Referencing)
El Contexto de Negocio: Eres el Backend Developer del servidor de pagos de un E-Commerce. 
Te acaba de llegar por la red el carrito de compras que un cliente quiere pagar en caja (que tiene forma de Lista pura). 
Pero el cliente solo manda nombres, tú necesitas calcular cuánto dinero real cobrarle a su tarjeta. 
Para eso, tienes que cruzar su carrito contra la base de datos oficial del almacén (que tiene forma de Diccionario). 
Alerta de Negocio: Si un producto del carrito no existe en la base de datos oficial, debes aislarlo inmediatamente porque es un intento de fraude o un error del sistema.
"""
carrito_cliente = ["Laptop", "Mouse", "Auriculares", "Licencia_Falsa_Windows", "Mouse"]

base_datos_precios = {
    "Laptop": 1000,
    "Mouse": 50,
    "Monitor": 200,
    "Auriculares": 80,
    "Teclado": 30
}

# Lógica de negocio
"""
1-La tarea se trata de calcular caunto cobrarle al cliente
Resolución: Para saber cuanto cobrarle, necesito sumar los precios de todos los artículos, para ello usare una variable
llamada costo_total=0 la iniciare en cero, esta variable me fucnionara como acumuladora

2- Si el producto no existe, en la base de datos aislarlo, ya que puede ser fraude o error

"""
# Pasos
# 1. Crear la variable acumuladora costo_total=0
costo_total=0
# 2. Crear la lista vacía para aislar los productos que no existen en la base de datos
productos_no_existentes=[]
# Ahora creamos un bucle for para checkmatear lista de productos y BBDD
# Empezamos por la BBDD
for producto in carrito_cliente:
    if producto in base_datos_precios:
        costo_total += base_datos_precios.get(producto)  
    else:
        productos_no_existentes.append(producto)
    
print(f'En base a la lista de productos pasado por el cliente debes debe de pagar un total: {costo_total}\n Los productos fraudulentos son: {productos_no_existentes}')


# Errores
# 1. En la primera integracion de codigo, tratamos hacer lo siguiente, iteramos la lista del carrito del cliente, para sacar producto a producto
# 2- Despues comprobamos si este se encuentra en la base de datos a traves de el operador de comparación in
# Una vez comparado y ver que si se encunetra en la base de datos tratamos de utilizar a traves de .get(item), para sacar el valor del producto y usarlo como acumulador, aca se dio un error de tipo
#    costo_total+= base_datos_precios.get("producto")
# TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'
# Es decir me lanzo un error de tipo pero de 2 tipos me dice que un nuemro entero y un NoneType se pueden sumar, tengo que ver porque es esto
# Ya veo que el probelma es base_datos_precios.get("producto"), me arroja un None
# Entiendo que esto es ya que al usar el operador in lo único que me da es un balor booleano True o False
# ¿Como solucionarlo?
# Cambie la condición if por un bucle for y me sigue dando lo mismo, no entiendo porque compara un none, si lo que me da de salida el primer bucle es las llaves
# probe esto y me arrojaba lo siguiente: No todo el rato que itero
"""
     if producto in base_datos_precios== True:
        print("verdad")
    else:
        print("No")
"""
# Despues hice esto:
"""
for producto in carrito_cliente:
    # print(producto)
    for producto, precios in base_datos_precios.items():
        costo_total+=precios
    else:
        productos_no_existentes=producto
Output:
En base a la lista de productos pasado por el cliente debes debe de pagar un total: 6800
 Los productos fraudulentos son: Teclado
"""
# Pero claro teclado si estaba en la base de datos algo esta mal, "Eureka", aunque no  lo he comprobado debo de revertir el orden
# Primero iterar sobre la base de datos y despues a traves de un operador lógico como if ver si ese producto este, en caso de estarlo sumar el valor del producto, si no agrgarlo a la lista nueva a traves de .append()
"""
He hecho esto, aunque se que esta mal
for item, precio in base_datos_precios.items(): # buscamos todos los item, y precios de los mismos
    print(item)
    if item in carrito_cliente:
        costo_total+=precio
        
        
else:
    productos_no_existentes.append(item)
    

print(costo_total)
print(productos_no_existentes)
Output:
1130
['Teclado']
"""
# Lo se por su salida obviamente, aunque el problema esta más calro, no esta sumando los valores correctamente, 
# cuando se repite el producto, y lo siguinete es ¿como capto el producto que no esta en la base de datos y si en la lista?
# Solución mi primera iteración estaba bien solo que le estaba pasando como argumento al .get un string "prodcuto", por eso me daba none