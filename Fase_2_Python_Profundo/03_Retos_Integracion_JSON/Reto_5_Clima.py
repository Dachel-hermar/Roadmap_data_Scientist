"""
Reto de Integración 5/6: El Meteorólogo (Anidación JSON)

Contexto de Negocio: Cuando un Ingeniero de Datos se conecta a los servidores 
de internet para descargar información (por ejemplo, a una API del clima), 
los datos nunca llegan en una lista bonita y plana. Llegan en estructuras "Anidadas" 
(como muñecas Matrioskas: Una caja dentro de otra caja). 

Tu Jefe te pide que le entregues un reporte rápido de cuántos días llovió en 
Madrid basándose en el paquete de datos que acaba de escupir el satélite meteorológico.
"""

# Tus Datos Crudos (Arquitectura JSON Anidada):
api_clima = {
    "ciudad": "Madrid",
    "pais": "España",
    "registros_semanales": [
        {"dia": "Lunes", "lluvia": True},
        {"dia": "Martes", "lluvia": False},
        {"dia": "Miércoles", "lluvia": True},
        {"dia": "Jueves", "lluvia": False},
        {"dia": "Viernes", "lluvia": True}
    ]
}

# 1. Crea tu acumulador matemático 
dias_lluviosos = 0

# 2. Extracción Nivel 1: Saca la lista de su caja fuerte usando .get()
lista_extraccion = api_clima.get("registros_semanales")

# 3. Extracción Nivel 2: Inicia tu bucle para iterar sobre tu nueva lista_extraccion
for registro in lista_extraccion:
    
    lluvia= registro.get("lluvia")
    if lluvia:
        dias_lluviosos+=1
        



# 6. Imprime el reporte final
print(f"En Madrid llovió un total de {dias_lluviosos} días esta semana.")
