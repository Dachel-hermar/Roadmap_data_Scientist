"""
Reto 1: El Bucle Condicional (Introducción al 'while')

Contexto Teórico:
El bucle 'for' es fantástico cuando sabes exactamente cuántas vueltas vas a dar 
(ej. iterar sobre una lista de 10 elementos significa dar 10 vueltas matemáticas).
Pero... ¿qué pasa cuando NO sabes cuántas vueltas necesitas? ¿Qué pasa si necesitas 
que un código corra "hasta que se cumpla un objetivo"?
Para eso existe el 'while' (Mientras).

Regla de Oro: El 'while' necesita una condición que eventualmente se vuelva Falsa. 
De lo contrario, creará un "Bucle Infinito" que bloqueará tu computadora.
"""

# =========================================================
# LA ALARMA DE INVENTARIO (El Bot de Reposición)
# =========================================================
# Eres el Analista de un almacén. 
# Arrancas con 20 unidades de un producto en tu base de datos.
# Cada vez que ocurre una transacción, se venden 3 unidades de golpe.
# El sistema necesita detenerse y lanzar una alarma en el instante en que 
# el stock baje de 5 unidades. Tu Jefe quiere saber cuántas transacciones pasaron.

stock_actual = 20
transacciones_realizadas = 0

print("--- INICIANDO MONITOR DE STOCK ---")

# TAREA:
# Escribe un bucle 'while' que funcione MIENTRAS el stock_actual sea mayor o igual a 5.
# Adentro del bucle:
# 1. Réstale 3 al stock_actual
# 2. Súmale 1 a tus transacciones_realizadas
while stock_actual >= 5:
    stock_actual -=3
    transacciones_realizadas +=1



print("\n--- REPORTE DE ALARMA ---")
print(f"Transacciones realizadas antes del corte: {transacciones_realizadas}")
print(f"Stock restante en el almacén: {stock_actual}")
