"""
Reto 1: La Fábrica de Comandos (Introducción a 'def')

Contexto Teórico:
Hasta este preciso momento, hemos sido "consumidores" de software. Hemos usado comandos 
que otros ingenieros escribieron para nosotros en el pasado (print(), len(), .append(), zip()).
Hoy pasamos al nivel de Creadores. 

Con la palabra reservada 'def' (Define), le enseñamos a la máquina un comando totalmente 
nuevo inventado por nosotros.
Una Función es exactamente igual a una licuadora (una caja negra): 
1. Recibe ingredientes por la tapa superior (Parámetros/Argumentos).
2. Procesa toda tu lógica algorítmica por dentro (Bucles, Ifs).
3. Escupe un licuado perfecto por abajo usando nuestro viejo amigo, el comando 'return'.
"""

# =========================================================
# EL CLASIFICADOR DEMOGRÁFICO (Filtro Automático)
# =========================================================
# Eres el Arquitecto de Datos de una agencia de Marketing.
# Ventas te manda todos los días listas gigantes de edades de clientes desordenadas.
# Tu Jefe te pide que crees una "máquina" (función) que automatice la separación de estos datos.

edades_crudas_hoy = [15, 22, 45, 12, 17, 30, "ocho", 60, 8.5]

print("--- INICIANDO FÁBRICA DE CLASIFICACIÓN ---")

# TAREA:
# 1. Define una función llamada 'clasificador_clientes' que reciba 1 solo parámetro: 'lista_edades'
# 2. Adentro de la función, inicia tu estado: crea un diccionario con dos llaves: "Mayores" y "Menores" (ambas deben contener listas vacías).
# 3. Crea un bucle que recorra el parámetro 'lista_edades'.
# 4. Si la edad es >= 18, inyéctala (append) en la lista de "Mayores" de tu diccionario. Si no, a "Menores".
# 5. Finalmente (poniendo a prueba la regla de la Indentación del Return), devuelve tu diccionario al mundo exterior.

# (Construye tu máquina aquí abajo)
def clasificador_clientes(lista_edades):
    Mayores=[]
    Menores=[]
    diccionario_edades={
        "Mayores": Mayores,
        "Menores" : Menores
    }
    for edad in lista_edades:
        if not isinstance(edad, int):
            continue
        if edad >=18:
            Mayores.append(edad)
        else:
            Menores.append(edad)
    return diccionario_edades



# =========================================================
# ZONA DE PRUEBAS (Mundo Exterior)
# =========================================================
# Aquí vamos a "llamar" a tu nueva herramienta y a pasarle los datos de hoy para ver si funciona.
# Quítale el símbolo de comentario '#' a las dos líneas de abajo cuando tu función esté lista:

reporte_final = clasificador_clientes(edades_crudas_hoy)
print(reporte_final)
