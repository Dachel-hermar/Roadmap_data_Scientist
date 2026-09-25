"""
RETO 11: Procesamiento Infinito (Generadores y la palabra 'yield')

Contexto de Negocio:
Hasta ahora, todas tus funciones terminaban con un `return`. El problema del `return` 
es que escupe TODA la información de golpe. Si le pides procesar 10 millones de filas 
de una base de datos y haces `return lista_final`, tu memoria RAM explotará.

Solución: Los Generadores.
Un generador usa la palabra `yield` en lugar de `return`. Lo que hace es escupir UN 
solo resultado, "pausar" la función, y esperar a que tú le pidas el siguiente usando 
la función nativa `next()`. ¡Así puedes procesar el infinito sin quemar la RAM!

Tu Misión:
1. El Generador: Crea una función `generador_ids()` (sin parámetros).
   - Crea un contador: `id = 1`.
   - Crea un bucle infinito: `while True:`
   - Adentro del bucle, en vez de un `return`, escribe `yield id`.
   - Justo abajo del yield, suma el contador: `id += 1`.
2. La Fábrica:
   - Guarda el motor en una variable: `fabrica = generador_ids()`
   - Imprime lo que sale si llamas a `next(fabrica)`.
   - Vuelve a imprimir `next(fabrica)`.
   - Vuelve a imprimir `next(fabrica)`.
"""

# ==========================================
# 1. EL MOTOR GENERADOR (Pausando el tiempo)
# ==========================================
# Escribe tu función aquí abajo...

def generador_ids():
    id=1
    while True:
        yield id
        id +=1
    


# ==========================================
# 2. LA FÁBRICA (Extracción controlada)
# ==========================================
# Extrae los IDs uno a uno...
fabrica = generador_ids()
print(next(fabrica))

