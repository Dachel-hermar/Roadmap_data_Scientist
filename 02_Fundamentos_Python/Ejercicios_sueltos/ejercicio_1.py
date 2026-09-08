""""
El Contexto: En los sistemas antifraude, a veces el peligro no es cuánto gasta un cliente, 
sino su patrón de gasto. Los ladrones de tarjetas suelen hacer pruebas haciendo transacciones 
cada vez más pequeñas de forma consecutiva para ver el límite de la tarjeta sin hacer saltar los bloqueos por compras grandes.

La Regla de Negocio (El Patrón): Tu código debe lanzar una "Alerta de Fraude" si (y solo si) un usuario realiza 3 transacciones 
CONSECUTIVAS que disminuyen de valor de forma estricta (Ejemplo: gasta 100, luego 80, y luego 50).

Tus Datos: Te entregan esta lista cronológica de las transacciones de hoy de un cliente: 
transacciones = [120, 150, 140, 110, 90, 200, 50]

(Spoiler visual para ti: En esta lista SÍ existe el patrón de fraude. Los números 140, luego 110, y luego 90 cumplen la regla de 3 bajadas consecutivas).

Tu Tarea: Escribe el código Python que recorra la lista, detecte este patrón matemático exacto, y avise del fraude.
"""

transacciones = [120, 150, 140, 110, 90, 200, 50]
# creación de una variable para guardar las transacciones
posibles_fraudes=0
# primero debo de recorrer la lista a traves de un bucle for
for item in range(len(transacciones)-2):
    if transacciones[item] > transacciones[item +1] > transacciones[item + 2]:
        print(f' Alerta de Fraude detectada')
        break
else:
    print("No se detectó fraude")



