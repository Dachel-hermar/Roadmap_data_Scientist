"""
Bootcamp Ejercicio 3/10: La Caja Registradora (Síntesis Total)

REGLAS MILITARES:
1. Cero teoría nueva.
2. Todo encapsulado en una Función (def).
"""

# REQUERIMIENTO DE NEGOCIO:
# Eres el Arquitecto de Software de un supermercado.
# Necesitas construir el sistema base de una caja registradora.
#
# Construye una función 'caja_registradora' que no reciba parámetros.
# 1. Inicia una variable 'total' en 0 (Tu viejo amigo el Acumulador).
# 2. Abre un bucle interactivo (while True).
# 3. Pide al usuario un input: "Ingresa el precio del artículo (o escribe COBRAR para finalizar): "
# 4. Si el usuario escribe "COBRAR", rompe el bucle y devuelve (return) el 'total' final.
# 5. Si no es "COBRAR", asume que es un precio. Conviértelo a decimal (float) y súmalo al 'total'.
# 6. ¡PELIGRO EN PRODUCCIÓN!: Si el cajero teclea letras por error (ej. "veinte"), el sistema explotará
#    al intentar usar float(). Debes envolver la conversión en un 'try/except' para atrapar 
#    el error, imprimir "Dato inválido, intenta de nuevo", y usar 'continue' para que la máquina no muera.

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def caja_registradora():
    total=0
    while True:
        try:
            precio= input("Ingresa el precio del artículo (o escribe COBRAR para finalizar): ")
            if precio=="COBRAR":
                return total
                
            precio= float(precio)
            total += precio
        except Exception:
            print("Dato inválido, intenta de nuevo")
            continue
        
        





# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
total_compra = caja_registradora()
print(f"\n--- FACTURA FINAL ---")
print(f"El cliente debe pagar: ${total_compra}")

# Problemas Encontrados
# Estaba tratando de probar una condición logica que no tenía sentido alguno
# Después del break intente un if!="COBRAR" todo lo demás convertir a float y sumar
# ¿Qué pasaba el try\except me tomaba cualquier cosa fuera de COBRR como error
