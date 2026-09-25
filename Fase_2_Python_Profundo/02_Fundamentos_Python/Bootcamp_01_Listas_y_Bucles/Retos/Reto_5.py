"""
💻 Reto 5/10: La Media Móvil Simple (Sector Series Temporales / Bolsa)

El Contexto: En los mercados financieros, los datos diarios son muy erráticos. 
Para ver la tendencia real del mercado, los analistas usan la "Media Móvil de 2 días" (que es simplemente promediar el precio de hoy con el precio de mañana). 
Tus Datos: ventas = [10, 20, 30, 40, 50]

Tu Tarea: Escribe el código que genere una lista nueva con los promedios.
"""

# Valores actuales
ventas = [10, 20, 30, 40, 50]
# Lista nueva de de promedios
promedios_datos= []

for item in range(len(ventas)-1):
    promedio= (ventas[item]+ventas[item +1])/2
    promedios_datos.append(promedio)
print(f'Media Móvil de 2 días: {promedios_datos}')