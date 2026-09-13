"""
Bootcamp Ejercicio 2/10: El Buscador Interactivo (Memoria Muscular)

REGLAS MILITARES:
1. Cero teoría nueva.
2. Todo encapsulado en una Función (def).
3. Piensa como Científico: ¿Cómo manejo casos donde el usuario escribe mal el dato?
"""

# REQUERIMIENTO DE NEGOCIO:
# Eres el Data Scientist de un almacén retail.
# Tienes una base de datos (Diccionario) con productos y su stock actual.
# Los operadores del almacén necesitan una herramienta en la consola para consultar 
# rápidamente si hay stock de un producto sin tener que reiniciar el programa cada vez.
#
# Construye una función 'buscador_stock' que reciba el diccionario de inventario.
# La función debe iniciar un bucle infinito interactivo (Cajero Automático) que:
# 1. Le pregunte al usuario: "¿Qué producto buscas? (Escribe SALIR para terminar): "
# 2. Si el usuario escribe "SALIR", el bucle se rompe y el programa se despide.
# 3. Si escribe un producto, búscalo en el diccionario. Si existe, imprime su stock.
# 4. Si NO existe (Control de Errores), imprime "Producto no encontrado".

inventario_actual = {
    "Laptop": 15,
    "Mouse": 42,
    "Teclado": 0,
    "Monitor": 8
}

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def buscador_stock(inventario):
    while True:
        
        producto= input("¿Qué producto buscas? (Escribe SALIR para terminar): ")
        if producto == "SALIR":
            print('Hasta pronto')
            break
            
        if producto in inventario:
            print(f'El stock actual de {producto} es {inventario[producto]}')
        else:
            print("Producto no encontrado")




# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí pasándole el inventario_actual
busqueda= buscador_stock(inventario_actual)

# Problemas encontrados
# Anteriormente habia escrito el bucle for despues de la primera función printç
# Lo que sucedia, era que el else se ejecutaba de todas manera, incluso cuando se ponía un producto que estaba en la base de datos
# Despúes de analizarlo no entendía el porque se ejecutaba igualmente, el problema era la función while que había definido arriba del todo
# Supongo que era esoun tema de jerarquíaaunque no lo entiendo del todo
# Ya que incluso así el sistema debería de haber respetado el la condición else
# Bueno nada lo cambie arriba despues del while, me refiero a mi bucle y funciono
# Duda que aún no logro entender
# El tema era el bucle en diccionario estaba obligando a la maquina a dar vueltas inecesarias, cuando solamente llamando a la llave ya tenia el resultado
