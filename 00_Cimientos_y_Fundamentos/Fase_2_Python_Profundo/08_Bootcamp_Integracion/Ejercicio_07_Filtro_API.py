"""
Bootcamp Ejercicio 7/10: La API de Clientes (Navegando JSONs)

REGLAS MILITARES:
1. Cero teoría nueva.
2. Todo encapsulado en una Función (def).
3. Vas a combinar Listas y Diccionarios al mismo tiempo (el estándar JSON).
"""

# REQUERIMIENTO DE NEGOCIO:
# Te acabas de conectar a la base de datos de tu empresa y descargaste los usuarios.
# Los datos vienen en formato JSON: Una Lista inmensa que contiene Diccionarios por dentro.
# El departamento de Marketing quiere lanzar una campaña de correos, pero SOLO
# para los clientes que sean mayores de edad (18+) Y que tengan su cuenta "activa".
#
# Construye una función 'filtrar_clientes' que reciba esta base de datos.
# 1. Crea una lista vacía 'clientes_objetivo'.
# 2. Recorre la base de datos. Para cada diccionario, verifica dos cosas lógicas:
#    - Que la "edad" sea mayor o igual a 18.
#    - Que el estado "activo" sea True.
# 3. Si el cliente cumple AMBAS condiciones a la vez, extrae SOLO su "nombre" y guárdalo en tu lista vacía.
# 4. Retorna (return) tu lista final.

base_de_datos = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Luis", "edad": 17, "activo": True},    # Menor de edad
    {"nombre": "Carlos", "edad": 40, "activo": False}, # Cuenta inactiva
    {"nombre": "Sofia", "edad": 22, "activo": True}
]

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def filtrar_clientes(clientes):
    clientes_objetivo=[]
    for cliente in clientes:
        #print(cliente)
        if cliente["edad"] >=18 and cliente["activo"]==True:
            clientes_objetivo.append(cliente["nombre"])
    return clientes_objetivo



# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí y haz un print.
campaña= filtrar_clientes(base_de_datos)
print(f'Los clientes objetivos para la campaña de marketing son: {campaña}')
# El resultado final debería ser una lista plana: ['Ana', 'Sofia']
