# Reto de Integración 4/6: El Analista de Gastos (Group By)

transacciones = [
    {"categoria": "Comida", "monto": 50},
    {"categoria": "Transporte", "monto": 20},
    {"categoria": "Comida", "monto": 30},
    {"categoria": "Ocio", "monto": 100},
    {"categoria": "Transporte", "monto": 10}
]

# 1. Crea el diccionario vacío para el reporte final
gastos_agrupados = {}
# 2. Inicia tu bucle for para recorrer las transacciones
for dato in transacciones:
    
    categoria= dato.get("categoria")
    monto= dato.get("monto")
    if categoria in gastos_agrupados:
        gastos_agrupados[categoria]+=monto
    else:
        gastos_agrupados[categoria]=monto
        


    
      
           
       



# 3. Imprime el reporte financiero agrupado
print(gastos_agrupados)
