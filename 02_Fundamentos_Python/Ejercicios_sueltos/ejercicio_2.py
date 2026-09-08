"""
📦 Simulador 1: El Filtro Logístico (Sector: Transporte)

El Contexto: Eres el analista del centro de distribución de una empresa de paquetería (estilo Amazon). 
Te han entregado una base de datos con los pesos (en kilogramos) de los paquetes de hoy. 

Tus Datos: pesos = [15, 25, 5, 30, 45, 10, 50]

La Regla de Negocio: La furgoneta de reparto de la zona centro tiene una regla sindical estricta de prevención de riesgos laborales: 
Solo suben a la furgoneta los paquetes que pesen estrictamente MENOS de 30 kg. Si un paquete pesa 30 kg o más, 
el sistema debe ignorarlo (no sube).

Tu Tarea: El conductor necesita saber el Peso Total Acumulado (en kilogramos) de los paquetes que SÍ van a subir a su furgoneta hoy.
"""
# Listado de pesos de los paquetes
pesos = [15, 25, 5, 30, 45, 10, 50]
# vamos a crear una variable que funcionara como contador, para así saber que cantidad de paquetes dejamos en el almacen
paquetes_que_se_quedan_en_almacen = 0

# Creamos una variable que acumulara el peso total de los paquetes que se van a subir a la furgoneta
peso_total_kg= 0

# Creamos el bucle para analizar los paquetes es decir su peso
for item in pesos:
    """
    Con esto me aseguro que se recorra toda la lista
    Por muchos paquetes que sean
    """
    if item >= 30:
        paquetes_que_se_quedan_en_almacen +=1
    else:
        peso_total_kg += item
print(f'La furgoneta lleva un peso total de {peso_total_kg} kg hoy')
print(f' La cantidad de paquetes que se quedaron en el alamacén son de {paquetes_que_se_quedan_en_almacen}')      
