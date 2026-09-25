"""
💻 Reto 8/10: La Inversión del Diccionario (Sector Data Engineering)
El Contexto Teórico: A veces, las bases de datos heredadas (sistemas viejos) vienen construidas exactamente al revés de lo que necesitamos hoy en día. 
O, como en este caso, la "Clave" identificadora es un texto gigantesco que consume demasiada memoria RAM, y el "Valor" es una sigla súper liviana. 
Para optimizar las búsquedas, los ingenieros de datos realizan una "Inversión Estructural" (las Claves pasan a ser los Valores, y los Valores pasan a ser las nuevas Claves).

Tus Datos Crudos:

python


cargos_antiguos = {
    "Director_General_Ejecutivo_Global": "CEO",
    "Vicepresidente_Finanzas_Corporativas": "CFO",
    "Jefe_Tecnologia_Informacion": "CTO"
}

Tu Tarea Lógica:

Crea tu base de datos limpia cargos_optimizados = {}.
Inicia tu bucle .items() para extraer la información de la base de datos antigua.
El Rompecabezas: Inyecta la información en tu base de datos limpia, pero conectando los cables al revés. Lo que en la vuelta actual era el "Valor" ("CEO"), ahora debe convertirse en tu nueva "Clave" de inyección. Y lo que era la "Clave" original (el texto kilométrico), ahora debe quedar guardado y oculto como el nuevo "Valor".
Imprime el nuevo diccionario para confirmar la migración estructural.
El Jefe de Datos espera ver esto: {'CEO': 'Director_General_Ejecutivo_Global', 'CFO': 'Vicepresidente_Finanzas_Corporativas', 'CTO': 'Jefe_Tecnologia_Informacion'}
"""

# Datos:
cargos_antiguos = {
    "Director_General_Ejecutivo_Global": "CEO",
    "Vicepresidente_Finanzas_Corporativas": "CFO",
    "Jefe_Tecnologia_Informacion": "CTO"
}

# base de datos limpia
cargos_optimizados={}
# inicializando el bucle, para recorrer la base de datos
for key, values in cargos_antiguos.items():
    cargos_optimizados[values]= key
print(cargos_optimizados)

# Resultados
# 1. Rápido, no hubo mucha dificultad técnica
# Salida:
# {'CEO': 'Director_General_Ejecutivo_Global', 'CFO': 'Vicepresidente_Finanzas_Corporativas', 'CTO': 'Jefe_Tecnologia_Informacion'}
# 2. Aunque esté gannado confianza no quiere decir que me confíe pero me gusta la sensación
# 3. Confianza+=1
# Miedos:
# Qué me den los problemas y como no me dicen como resolverlo me quede en blanco
# Solución por el momento y para siempre pseudocódigo 