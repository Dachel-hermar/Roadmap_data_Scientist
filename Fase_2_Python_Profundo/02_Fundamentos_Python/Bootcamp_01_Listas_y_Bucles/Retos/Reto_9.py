"""
💻 Reto 9/10: Tasa de Fuga / Churn Rate (Sector SaaS)
El Contexto: Eres el Data Analyst de Netflix. Te pasan la cantidad de suscriptores activos de los últimos 5 meses. 
Tu directiva te pide el "Churn Rate" (El porcentaje total de clientes que se han fugado) comparando el primer mes contra el último mes. 
Tus Datos: suscripciones = [1000, 950, 900, 800, 750]

Tu Tarea: Escribe el código que calcule el porcentaje de pérdida total.

Calcula la pérdida matemática: (Suscriptores Iniciales - Suscriptores Finales).
Calcula el porcentaje real: (Pérdida / Suscriptores Iniciales) * 100.
Imprime: "La tasa de fuga total fue del [X] %".
"""

# Datos de clientes 
suscripciones = [1000, 950, 900, 800, 750]


perdida_matematica = suscripciones[0] - suscripciones[-1]
porcentaje_real = (perdida_matematica/ suscripciones[0])*100
print(f"La tasa de fuga total fue del {porcentaje_real} %")