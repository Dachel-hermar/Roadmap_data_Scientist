"""
💻 Reto 1/10: El Traductor de Servidores (Sector Web / DevOps)
El Contexto: Eres el Data Analyst del equipo de sistemas de una página web. Los servidores te devuelven códigos numéricos de error, pero el equipo de atención al cliente necesita leer el texto en español para saber qué decirle al usuario. 
Tus Datos: Tienes el diccionario maestro oficial.

python


codigos_http = {
    200: "Todo OK",
    404: "Página no encontrada",
    500: "Error interno del servidor",
    403: "Acceso denegado"
}
Tu Tarea: Escribe el algoritmo que funcione como traductor:

Pídele al usuario por teclado (usando input()) que introduzca un código numérico. (Recuerda la técnica de la cebolla para asegurarte de que la máquina lea un número entero y no un texto).
Crea un bloque if / else. Si el número ingresado existe como clave dentro del diccionario, imprime en pantalla el mensaje de texto correspondiente.
Si el código ingresado NO existe en el diccionario, imprime el mensaje genérico: "Código desconocido. Escale el ticket a IT.".
"""
codigos_http = {
    200: "Todo OK",
    404: "Página no encontrada",
    500: "Error interno del servidor",
    403: "Acceso denegado"
}

# Iniciamos el bucle infinito (sin necesidad de variables previas)
while True:
    # 1. Pedimos el input SIEMPRE como texto puro, sin el 'int'
    codigo_ingresado = input("Ingrese un código numérico: ")
    
    # 2. Control de daños (Filtro de seguridad)
    if not codigo_ingresado.isdigit():
        print("Error: Debes introducir un número entero positivo.")
        continue # Tu herramienta favorita. Ignora lo de abajo y reinicia el bucle pidiendo el input otra vez.
    
    # 3. Si sobrevivió a la prueba anterior, AHORA SÍ es seguro convertirlo a matemática
    codigo_matematico = int(codigo_ingresado)
    
    # 4. Buscamos en la base de datos
    if codigo_matematico in codigos_http:
        print(f"Éxito. El código significa: {codigos_http[codigo_matematico]}")
        break # ¡Misión cumplida! Destruimos el bucle infinito y salimos.
    else:
        print("Código desconocido. Escale el ticket a IT.")
        # Aquí no hace falta poner otro input(). Como no hay 'break', el bucle volverá a girar naturalmente.
        
            
