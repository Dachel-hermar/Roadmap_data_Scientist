# Reto de Integración 1/6: Filtro de Candidatos (RRHH)
"""
El Contexto de Negocio: Eres el Data Analyst que asiste al departamento de RRHH. 
Acaba de cerrar la oferta de empleo para "Data Scientist Junior" y recibieron decenas de currículums en formato JSON. 
Tu Jefe te pide que filtres la base de datos y le entregues una nueva base de datos limpia (otra lista de diccionarios) 
que contenga única y exclusivamente a los candidatos viables para llamarlos a entrevista.
Regla de Negocio (Filtro Viable): El candidato debe saber Python (True) Y su salario esperado debe ser menor o igual a 30,000 euros anuales.
"""
candidatos = [
    {"nombre": "Juan", "python": True, "salario_esperado": 35000},
    {"nombre": "Ana", "python": True, "salario_esperado": 28000},
    {"nombre": "Luis", "python": False, "salario_esperado": 25000},
    {"nombre": "Marta", "python": True, "salario_esperado": 30000},
    {"nombre": "Pedro", "python": True, "salario_esperado": 40000}
]

# 1. Crea la nueva lista vacía para guardar a los candidatos ganadores
candidatos_viables = []

# 2. Inicia tu bucle para recorrer la lista de candidatos
for candidato in candidatos:
    # print(lista) # Siempre compruebo la salida
    # Creando la condición para cumplir la regla del negocio
    if candidatos.get("python")== True and candidatos.get("salario_esperado")<=30000:
        candidatos_viables.append(candidatos)



# 3. Imprime la lista final
print(candidatos_viables)

# Resultados:
# Ahora mismo me encuentro eufrico, aunque para muchos, no parezca gran cosa, para mi lo es
# He resuelto este ejercicio, en un tiempo que no llego a los 5 minutos y la verdad eso para mi es premio
# Hoy me siento imparable, ya estoy dominando la base, aunque se que a´n faltan muchas funciones por dominar dentro de 
# la programación básica, estoy contento
# Confianza *=2