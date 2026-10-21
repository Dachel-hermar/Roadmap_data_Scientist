"""
Bootcamp Ejercicio 10/10: La Trilogía del Caos - Parte 3 (El Analista de Riesgos)

REGLAS MILITARES:
1. El último desafío del Bootcamp. 
2. Integra todo el conocimiento estructural. Cero pistas de arquitectura.
"""

# REQUERIMIENTO DE NEGOCIO (EL JEFE FINAL):
# Eres el Jefe de Análisis de Riesgos de un banco de inversión.
# Te entregan una base de datos compleja (Estructuras Anidadas): Un Diccionario donde las Llaves 
# son los nombres de los clientes, y los Valores son LISTAS que contienen todas sus 
# transacciones del mes (números positivos son depósitos, números negativos son compras/retiros).
#
# Construye una función 'detectar_bancarrotas' que reciba esa base de datos.
# 1. Crea un nuevo diccionario vacío llamado 'clientes_en_rojo'.
# 2. Recorre el diccionario original (llaves y valores).
# 3. Para cada cliente, debes calcular cuál es su saldo matemático total (la suma de toda su lista).
#    (Piensa como Arquitecto: ¿Cómo sumas los números de una lista? Puedes usar un acumulador 
#    adentro de otro bucle 'for', o buscar si Python tiene alguna función matemática nativa...).
# 4. Si el saldo final de un cliente es MENOR A CERO (está endeudado), debes agregarlo
#    a tu diccionario 'clientes_en_rojo' (Llave = Nombre, Valor = Deuda).
# 5. Devuelve (return) el diccionario de deudores para enviarlo al departamento de embargos.

transacciones_banco = {
    "Ana": [1000, -200, 500, -3000],   # Total matemático: -1700 (¡Bancarrota!)
    "Luis": [500, 100, 400],           # Total matemático: 1000 (A salvo)
    "Carlos": [-50, -20, -100],        # Total matemático: -170 (¡Bancarrota!)
    "Sofia": [5000, -2000, 500]        # Total matemático: 3500 (A salvo)
}

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
# Objetivo: Saber los clientes que estan en bancarrota
# para ello necesitaremos un declarar un diccionario vacio, donde guardar a estos y saber cuales son
def detectar_bancarrota(transacciones):
    clientes_en_rojo={} # Almacenamos a los clientes en banca rota, para su posterior análisis
    for cliente, saldo in transacciones.items():
        #print(cliente)
        #print(saldo)
        # Como no encontre ninguna funcion que me ayudara a contar los elementos de una lista lo hare a la vieja usanza
        """
        total = 0
        for numero in saldo:
            total+=numero
            """
        total = sum(saldo)
        if total <0:
            clientes_en_rojo[cliente]=total
            
        
    return clientes_en_rojo



# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función pasándole el diccionario transacciones_banco.
bancarrota=detectar_bancarrota(transacciones_banco)
# Imprime el resultado. Debería devolverte exactamente: {'Ana': -1700, 'Carlos': -170}
print(bancarrota)
