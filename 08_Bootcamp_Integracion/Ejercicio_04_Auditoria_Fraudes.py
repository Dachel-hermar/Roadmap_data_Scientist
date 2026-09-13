"""
Bootcamp Ejercicio 4/10: Auditoría de Fraudes (Listas y Umbrales)

REGLAS MILITARES:
1. Cero teoría nueva.
2. Todo encapsulado en una Función (def).
3. Apaga la mentalidad de bucles infinitos por un momento. Aquí los datos ya existen y son finitos.
"""

# REQUERIMIENTO DE NEGOCIO:
# Eres Analista de Datos en el departamento de Seguridad de un banco internacional.
# Te entregan una lista masiva de transacciones (en dólares) que ocurrieron durante la madrugada.
# La ley internacional exige que cualquier transacción que sea MAYOR ESTRICTAMENTE a $10,000 USD 
# sea aislada e investigada por posible lavado de dinero.
#
# Construye una función 'detectar_fraudes' que reciba una lista de transacciones.
# 1. Crea una lista vacía llamada 'transacciones_sospechosas'.
# 2. Usa un bucle para recorrer la lista de transacciones una por una.
# 3. Si una transacción supera los 10,000, inyéctala (append) a la lista de sospechosas.
# 4. Al final, la función debe devolver (return) la lista con las transacciones peligrosas.

transacciones_nocturnas = [450, 12500, 30, 9999, 10001, 8500, 50000]

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def detectar_fraudes(transacciones):
    transacciones_sospechosas=[]
    for valor in transacciones:
        if valor > 10000:
            transacciones_sospechosas.append(valor)
    return transacciones_sospechosas


# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí pasándole las 'transacciones_nocturnas'
sospechas= detectar_fraudes(transacciones_nocturnas)
# Imprime el resultado para verificar que solo atrapó las 3 transacciones ilegales.
print(sospechas)
