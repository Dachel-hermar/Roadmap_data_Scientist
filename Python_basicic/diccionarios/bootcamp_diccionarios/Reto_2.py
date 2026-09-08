"""
💻 Reto 2/10: El Empleado del Mes (Sector Ventas / Retail)
El Contexto: Eres el analista de ventas de una concesionaria de coches. Tienes el registro total de ventas (en euros) de tus 4 empleados. Tus Datos:

python


ventas_mes = {
    "Juan": 15000,
    "Ana": 35000,
    "Pedro": 25000,
    "Marta": 42000
}
Tu Tarea: ¡Vuelve la Lógica del Campeón de la Fase 2! Necesitamos encontrar matemáticamente quién vendió más.

Crea dos variables "Campeón" antes del bucle: mayor_venta = 0 y mejor_empleado = "" (un texto vacío).
Usa un bucle con .items() para extraer a la pareja al mismo tiempo.
Compara en el if: Si la venta actual supera a la mayor_venta histórica, destrona a ambos campeones (actualiza el número de la venta y actualiza el nombre del empleado).
Al finalizar el bucle, imprime el anuncio: "El empleado del mes es [Nombre] con unas ventas de [Ventas] euros".
"""

# Datos de empleados
ventas_mes = {
    "Juan": 15000,
    "Ana": 35000,
    "Pedro": 25000,
    "Marta": 42000
}

# Variable para almacenar al Campeón
mayor_venta=0
mejor_empleado=""

# Inicializando un bucle para recorrer el diccionario
for key,value in ventas_mes.items():
    if value > mayor_venta:
        mayor_venta=value
        mejor_empleado= key
print(f'El empleado del mes es {mejor_empleado} con unas ventas de {mayor_venta} euros')