"""
Reto 1: El Chaleco Antibalas (Manejo Estructurado de Errores con try/except)

Contexto Teórico:
Hace un momento usaste Programación Defensiva (un 'if') para evitar que un Texto 
rompiera un código que esperaba un Número. Eso es brillante cuando PUEDES predecir el error exacto.

Pero en la vida real del Científico de Datos, te conectarás a servidores que se caen de golpe, 
o intentarás dividir una variable entre cero sin saberlo, o buscarás en un JSON un dato que alguien borró.
Esos errores son impredecibles y, cuando ocurren, Python aborta el script instantáneamente.

Para evitar que tu sistema explote por sorpresas, usamos el bloque 'try / except'.
Le dices a la máquina: 
"INTENTA (try) ejecutar este bloque de código peligroso. 
Si algo sale mal y EXPLOTA (except), no detengas el programa... simplemente ejecuta 
este plan de rescate y sigue con tu vida".
"""

# =========================================================
# LA CALCULADORA DE RENDIMIENTO FINANCIERO
# =========================================================
# Eres el Científico de Datos de un fondo de inversión.
# Tienes una lista de ganancias, y otra lista con los meses que operó cada empresa.
# Tu Jefe te pide la "Ganancia Promedio por Mes" de cada una.

ganancias = [10000, 5000, 0, 8000, 12000]
meses_operados = [5, 2, 0, 4, "seis"] 

print("--- CALCULANDO RENDIMIENTOS ---")

# TAREA:
# 1. Crea un bucle usando la función zip() para recorrer ambas listas en paralelo.
# 2. Adentro del bucle, calcula: promedio = ganancia / meses, e imprímelo.
# 3. ¡PELIGRO!: Hay dos trampas mortales en las listas de arriba:
#    - La empresa 3 operó 0 meses (Matemáticamente, la División entre Cero destruye el universo).
#    - La empresa 5 dice "seis" (Dividir un int entre un str lanza un TypeError).
# 4. Envuelve tu cálculo (y tu print) adentro de un bloque `try:`.
# 5. Usa `except Exception as error:` para atrapar la explosión, e imprime: 
#    f"Error detectado: {error}. Saltando empresa..."

# Logica de pseudocodigo
# 1. Voy a crear la estructura de lo que debe de hacer el programa primero 
# Objetivo: Ganancias Promedios del Mes, tengo dos listas ganancias y meses operando
# ¿Como calcular el promedio? promedio = ganacias/meses es decir total del dinero ganado entre los meses operando, eso me da el promedio mensual
# Como tengo dos lista usaremos el método zip() para analizar ambas en paralelo
# Debo de crear una variable que sea el promedio
# Vamos a comprobar el promedio de ganancias con print(),  Me da un error ZeroDivisionError (division por cero)
# ¿Como lo arreglo? podría usar el camino viejo y usar condicionales if, probemoslo y despúes creamos el ejercicio con try/except
    
for ganancia, mes in zip(ganancias,meses_operados):
    if not isinstance(ganancia,int) or ganancia==0:
        continue
    if not isinstance(mes,int) or mes==0:
        continue
    promedio_mensual= ganancia/mes # esto me daría el promedio de ganacias mensualmente

    
    print(promedio_mensual) 

print("\n--- ANÁLISIS TERMINADO. EL SISTEMA SIGUE VIVO ---")

# Nose como hacer tablas bonitas ni nada, pero esta es la segunda version
# para ella usaremos try/except y una funcion

def promedio_ganancias_mensual(ganacias_empresas, meses):
    for beneficios,mes_op in zip( ganacias_empresas, meses):
        try:
            promedio= beneficios/mes_op
            print(promedio)
        except Exception as e:
            print(f"Error detectado: {e}. Saltando empresa...")
            

promedio_ganancias_mensual(ganancias, meses_operados)


print("\n---Análisis de la segunda forma de hacer el calculo")




