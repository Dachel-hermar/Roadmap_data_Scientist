"""
💻 Reto 4/10: La Búsqueda Inversa (Sector Ciberseguridad)

El Contexto Teórico: Buscar un "Valor" en Python es instantáneo si conoces su "Clave" (simplemente escribes diccionario["Clave"]). 
Pero a veces, la vida real te pide hacerlo al revés: conoces el "Valor" y necesitas averiguar a qué "Clave" pertenece. 
Esto requiere ingeniería y se llama Búsqueda Inversa (Reverse Lookup).

El Caso: Eres el Data Analyst del equipo de Ciberseguridad. 
Te acaba de saltar una alerta de hackeo crítica desde una dirección IP,
 pero tú necesitas encontrar el Nombre de ese servidor para poder apagarlo.
 Tus Datos:

python


servidores = {
    "BaseDeDatos_Produccion": "192.168.1.5",
    "ServidorWeb_Publico": "10.0.0.1",
    "Servidor_Backups": "192.168.1.10",
    "Sistema_Autenticacion": "10.0.0.5"
}

ip_hackeada = "192.168.1.10"

Tu Tarea Lógica:

Inicia el bucle especializado que extrae a la pareja al mismo tiempo (.items()). Nombra tus variables con sentido (ej. nombre, ip).
Usa un if para evaluar: ¿Es la ip que estás leyendo en esa vuelta exactamente igual (==) a la ip_hackeada?
Si hay coincidencia exacta, imprime tu reporte de emergencia: "¡ALERTA ROJA! Apagando el servidor: [Nombre del Servidor]".
Optimización obligatoria: En el instante preciso en que encuentres al servidor culpable, aplica el botón de autodestrucción del bucle (break). Como ya encontraste a tu objetivo, sería un crimen computacional seguir iterando y gastando memoria preguntando por los servidores restantes.
"""

# Datos 

servidores = {
    "BaseDeDatos_Produccion": "192.168.1.5",
    "ServidorWeb_Publico": "10.0.0.1",
    "Servidor_Backups": "192.168.1.10",
    "Sistema_Autenticacion": "10.0.0.5"
}

# Ip hackeada
ip_hackeada = "192.168.1.10"

# Vamos a crear un bucle for para extraer los datos que necesitamos
for nombre, ip in servidores.items():
    if ip == ip_hackeada:
        print(f'¡ALERTA ROJA! Apagando el servidor: {nombre}')
        break # con esto rompemos el bucle una vez se encuentra el nombre del servidor ip hackeado
    