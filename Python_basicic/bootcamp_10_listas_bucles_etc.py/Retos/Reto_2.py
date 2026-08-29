"""
💻 Reto 2/10: La Racha Invicta (Basado en HackerRank - Sports Analytics)
El Contexto: Estás analizando el rendimiento histórico de un equipo de eSports.
El entrenador quiere saber de cuánto fue su mejor racha de victorias ininterrumpidas. 
Tus Datos: Una lista cronológica con los resultados de sus partidas (W = Win/Victoria, L = Loss/Derrota). 
resultados = ["W", "L", "W", "W", "W", "L", "W", "W"]

Tu Tarea: Calcula e imprime la Racha Máxima de Victorias Consecutivas. Resultado final esperado en pantalla: 
La mejor racha fue de 3 victorias.
"""

# Datos de victorias y derrotas
resultados = ["W", "L", "W", "W", "W", "L", "W", "W"]

# variable para guardar la cantidad de racha actual
racha_actual= 0
# Racha máxima ininterrumpidas
racha_maxima = 0

# Creo el bucle for 
for victoria in resultados:
    if victoria == "L":
     racha_actual = 0
    
    else:
        racha_actual +=1
        if racha_actual > racha_maxima:
            racha_maxima = racha_actual


print(f'La mejor racha fue de {racha_maxima} victorias')