"""
Bootcamp Ejercicio 5/10: El Analista de RRHH (Filtrando Diccionarios)

REGLAS MILITARES:
1. Cero teoría nueva.
2. Todo encapsulado en una Función (def).
3. Vas a iterar sobre un diccionario extrayendo llaves y valores al mismo tiempo.
"""

# REQUERIMIENTO DE NEGOCIO:
# Eres el analista de Recursos Humanos de una startup de tecnología.
# Te entregan la nómina completa en forma de Diccionario (Empleado: Salario).
# El CEO quiere hacer un ajuste salarial inflacionario para proteger a los que menos ganan.
#
# Construye una función 'ajuste_salarial' que reciba el diccionario original.
# 1. No crees diccionarios nuevos. Vas a mutar (modificar) el diccionario original.
# 2. Recorre el diccionario extrayendo la llave (nombre) y el valor (salario) con .items().
# 3. Si el salario de un empleado es estrictamente menor a $5,000, auméntale el salario en un 10%.
#    (Ejemplo: salario = salario + (salario * 0.10)). Actualiza ese valor directamente en el diccionario original.
# 4. Devuelve (return) el mismo diccionario pero con los salarios actualizados.

nomina_actual = {
    "Ana": 4500,
    "Luis": 6000,
    "Carlos": 3200,
    "Sofia": 7500,
    "Miguel": 4999
}

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def ajuste_salarial(nomina):
    for nombre, salario in nomina.items():
        if salario < 5000:
            salario= salario + (salario * 0.1)
            nomina[nombre]= salario
    return nomina




# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí pasándole la 'nomina_actual'
salario_actualizado= ajuste_salarial(nomina_actual)
# Imprime el resultado. Deberías ver un diccionario solo con Ana, Carlos y Miguel.
print(salario_actualizado)
