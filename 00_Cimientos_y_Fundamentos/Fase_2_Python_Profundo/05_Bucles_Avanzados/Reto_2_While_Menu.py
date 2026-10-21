"""
Reto 2: El Bucle Infinito Controlado (while True)

Contexto Teórico:
A veces, los Ingenieros de Software crean un "Bucle Infinito Intencional" escribiendo
la condición `while True:`. Como "True" siempre es Verdadero, el bucle nunca 
se detendrá en su cabecera.
¿Cómo lo detenemos entonces? 
Con nuestro querido botón de eyección desde adentro: el comando `break`.

Este patrón arquitectónico se usa el 100% de las veces para crear "Menús" interactivos, 
cajeros automáticos, videojuegos o sistemas de terminal donde el programa debe 
mantenerse vivo esperando órdenes hasta que el humano le diga "Quiero salir".
"""

# =========================================================
# EL CAJERO AUTOMÁTICO BANCARIO (Menú Interactivo)
# =========================================================
# Eres el desarrollador de sistemas de un banco.
# Necesitas mantener el sistema encendido dándole servicio al cliente.

saldo = 1000

print("--- BIENVENIDO AL BANCO PYTHON ---")

# TAREA: 
# 1. Crea el bucle infinito intencional: `while True:`
# 2. Adentro, usa un input() para guardar la respuesta del cliente: 
#    opcion = input("¿Qué deseas hacer? (1. Ver Saldo, 2. Salir): ")
# 3. Si la opcion es "1", haz un print() mostrando el saldo actual.
# 4. Si la opcion es "2", despídete con un print y usa el comando `break` para destruir el bucle.
# 5. Control de errores (Opcional pero recomendado): Si el usuario escribe una locura (ej. "Hola"), 
#    imprime un mensaje de "Opción no reconocida, intente de nuevo".

while True:
    opcion = input("¿Qué deseas hacer? (1. Ver Saldo, 2. Salir): ")
    print(f"DEBUG -> Valor crudo: '{opcion}' | Tipo de dato: {type(opcion)}")
    if opcion == "1":
        print(f'Su saldo actual es de: {saldo}')
    elif opcion == "2":
        print('Hasta Luego')
        break
    else:
        print("Opción no reconocida, intente de nuevo")


print("--- SISTEMA APAGADO. CAJERO FUERA DE SERVICIO ---")
