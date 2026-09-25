# Función Clásica (Ocupa 2 líneas, tiene nombre reservado en la RAM)
def multiplicar(a, b):
    return a * b

# Función Lambda Equivalente (Ocupa 1 línea, retorna el resultado automáticamente)
# Sintaxis: lambda parámetros : operación
multiplicador_rapido = lambda a, b: a * b

# La usas y la llamas exactamente igual:
print(multiplicador_rapido(10, 5))