"""
💻 Reto 6/10: El Test A/B (Sector Marketing)

El Contexto: Tu empresa envió 2 versiones de un mismo correo para ver cuál gustaba más. 
Tienes el número de clicks que recibió cada campaña durante los últimos 4 días. 
Tus Datos: clicks_a = [10, 25, 15, 30] clicks_b = [15, 20, 25, 40]

Tu Tarea:

Crea un acumulador para el total de la Campaña A y otro para el total de B.
Usando un bucle (o dos bucles distintos, como te sea más fácil), acumula todos los clicks de A y de B.
Al terminar de contar todo, crea un bloque lógico (if / elif / else) que enfrente al Campeón A contra el Campeón B.
Si ganó A, imprime: "Ganó la Campaña A por una diferencia de [X] clicks". Si ganó B, imprime el mensaje para B. 

"""
# Datos de las campañas
clicks_a = [10, 25, 15, 30]
clicks_b = [15, 20, 25, 40]

# Vamos a crear un acumulador para ambas campañas
acumulador_camp_a = 0
acumulador_camp_b = 0

# Creacion de bucles para la acumulacion de ambas variables
for item_a in clicks_a:
    acumulador_camp_a += item_a
for item_b in clicks_b:
    acumulador_camp_b += item_b

if acumulador_camp_a > acumulador_camp_b:
    print(f'Ganó la Campaña A por una diferencia de {acumulador_camp_a-acumulador_camp_b} clicks')
else:
    print(f'Gano la campaña B por una diferencia de {acumulador_camp_b-acumulador_camp_a} clicks')

