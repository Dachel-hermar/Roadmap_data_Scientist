"""
Bootcamp Ejercicio 1/10: Filtro Financiero y Memoria Muscular

REGLAS MILITARES DEL BOOTCAMP:
1. Cero teoría nueva. Solo requerimientos crudos de negocio.
2. Todo debe estar encapsulado en Funciones (def).
3. Debes usar Programación Defensiva (if not isinstance) o try/except si sospechas peligro.
"""

# REQUERIMIENTO DE NEGOCIO:
# Eres el Analista de un banco local.
# Tienes una lista de transacciones diarias (los positivos son depósitos, los negativos son retiros).
# Construye una función llamada 'clasificar_transacciones' que reciba esa lista.
# La función debe devolver un diccionario con dos llaves: 
# "Depositos" (lista de números positivos) y "Retiros" (lista de números negativos).
# Tu Guardia de Seguridad debe rechazar silenciosamente (continue) cualquier dato corrupto (textos).

transacciones_crédito = [1500, -300, 200, "Error_API", -50, 400.50, "Cero"]

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def clasificar_transacciones(transacciones):
    """
    Esta función se creo para clasificar las transacciones realizadas en el día
    Args:
    transacciones (recibe una lista de las transacciones de crédito)
    Output
    Depositos (listado de numeros positivos)
    Retiros (listado de numeros negativos)
    """
    deposito=[] # listado de números positivos
    retiro= [] # Listado de números negativos
    # Diccionario vacío que va a recibir los distintos tipos de créditos
    credito ={
        "Depositos" : deposito,
        "Retiros" : retiro
    }
    for valor in transacciones:
        """
        Bucle for para recorrer la lista de valores de creditos pasados como argumento de la funcion
        """
        # bloque try\except para captar cualquier error y el programa no se detenga
        try: 
            if valor >=0:
                deposito.append(valor)
            else:
                retiro.append(valor)
        except Exception as e: # Capta cualquier error y lo guarda en la variable e
            print(f'Error detectado {e}, saltando al próximo valor...')

    return credito 
# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí pasándole la lista 'transacciones_crédito'
reporte_final =clasificar_transacciones(transacciones_crédito)
# y haz un print del resultado para verificar tu lógica.
print(reporte_final)
