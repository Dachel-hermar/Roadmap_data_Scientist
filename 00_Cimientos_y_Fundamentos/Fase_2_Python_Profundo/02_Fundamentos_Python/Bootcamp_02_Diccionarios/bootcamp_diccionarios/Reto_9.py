"""
💻 Reto 9/10: El Test A/B (Sector Analítica Web / Marketing)

El Contexto de Negocio: En el mundo corporativo digital, los analistas de datos nunca intentan adivinar qué diseño de página web le gustará más al cliente. 
Lo que hacen es lanzar dos versiones al mismo tiempo (La Campaña A y la Campaña B) y miden matemáticamente cuál logra que la gente haga más clicks (A esta métrica se le llama CTR - Click Through Rate).

Tus Datos Crudos:

python


campana_A = {"CTR": 0.05, "Rebotes": 40, "Ventas": 100}
campana_B = {"CTR": 0.08, "Rebotes": 35, "Ventas": 150}
Tu Tarea Lógica:

A diferencia de todos los retos anteriores, aquí no debes crear ningún bucle para revisar todo el almacén, porque tu Jefe te pidió comparar única y exclusivamente la métrica del CTR. Los demás datos no importan ahora mismo.
Tienes que extraer el dato específico. ¿Recuerdas cómo sacar la información de un diccionario "yendo directo a la yugular" de la Clave? (Lo hicimos en el reto final de JSON de ayer).
Diseña la lógica matemática condicional (if / elif / else) que extraiga la caja del CTR de la Campaña A y la compare directamente contra la caja del CTR de la Campaña B.
El sistema debe imprimir el dictamen: "La ganadora es la Campaña [A o B] con un CTR de [valor]". (Como buen analista de Edge Cases, añade la lógica por si ambas empatan en métricas).
"""
# Datos
campana_A = {"CTR": 0.99, "Rebotes": 40, "Ventas": 100}
campana_B = {"CTR": 0.08, "Rebotes": 35, "Ventas": 150}

# Como el objetivo es comparar los CTR en este caso vamos a optener solamente esos valores, para ello lo pido directamente 
# Como es un diccionario con el método .get() obtengo el valor de la clave
if campana_A.get("CTR")>= campana_B.get("CTR"):
    print(f"La ganadora es la Campaña A con un CTR de {campana_A.get("CTR")}")
else:
    print(f"La ganadora es la Campaña B con un CTR de {campana_B.get("CTR")}")

# Resultados
# 1. Bien, fácil podría decirse
# confianz sigue aumentando