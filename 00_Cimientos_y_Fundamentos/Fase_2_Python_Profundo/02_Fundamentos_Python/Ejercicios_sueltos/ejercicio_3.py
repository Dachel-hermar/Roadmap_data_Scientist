"""
🌡️ Simulador 2: El Termostato Inteligente (Sector: IoT / Domótica)
Sigamos sumando horas de vuelo. Vamos a entrenar el Bucle Espacial y la Modificación de Listas.

El Contexto: Trabajas para una empresa de Hogares Inteligentes (IoT). Tienes una lista que registra la temperatura en grados Celsius que manda un sensor cada hora. Tus Datos: temperaturas = [20, 22, -99, 21, 23, -99, 24]

El Problema de Negocio: El sensor a veces pierde conexión WiFi, y cuando eso pasa, el sistema envía un código de error de -99 grados. Esto arruina completamente las gráficas de calor y asusta a los clientes.

Tu Tarea: Escribe el código Python puro que limpie los datos modificando la lista original. Debes recorrer la lista de temperaturas y, si encuentras el error -99, debes cambiarlo por un 0.
"""

# Datos de temperatura
temperaturas = [20, 22, -99, 21, 23, -99, 24]
# Creamos una variable contador para saber cuantas veces se repite el error -99
contador_de_errores = 0

# vamos a crear un bucle for que recorra toda la lista
for item in range(len(temperaturas)):
    """ 
    En este caso he utilizado range(len(temperaturas))
    Esto es debido a que no se en que posición puede estar la temperatura de error -99
    Por eso utilizo el índice en la lista, es decir le doy un índice a cada uno de lo valores
    composición
    len(temperatura): Calcula la longitud de la lista
    range(len(temperatura)): Crea un índice en base a la longitud de la lista
    
    output:
    índice de la lista
    """
    if temperaturas[item] == -99:
        temperaturas[item] = 0
        contador_de_errores +=1
        """
        Si temperatura en su índice es igual a -99 cambiarlo por 0
        si no es igual a -99 no hacer nada
        """
else:
    print(f'La lista de temperaturas ya está limpia: {temperaturas}')
    print(f'Se detectaron {contador_de_errores} erorres')
    
