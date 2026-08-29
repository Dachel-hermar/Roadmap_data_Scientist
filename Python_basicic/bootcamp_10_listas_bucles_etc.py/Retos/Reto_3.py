"""
💻 Reto 3/10: Limpieza de Datos (Data Quality)
El Contexto: Eres el Data Scientist de un E-commerce. 
Te pasan los datos de ventas diarias, pero el sistema falló y registró valores negativos y ceros (errores de sistema). 
Tus Datos: precios_crudos = [100, -20, 50, 0, 120, -5]

Tu Tarea: Escribe el código que purgue los datos corruptos. Debes crear una lista vacía precios_limpios = []. 
Recorre la lista de datos crudos, y solo si el precio es estrictamente mayor a 0, inyéctalo en tu lista limpia. 
Imprime la lista limpia al final.
"""

# Primero mis datos actuales
precios_crudos = [100, -20, 50, 0, 120, -5]

# Variable para contar la cantidad de precios corruptos que hay
precios_corruptos=0
# cantidad de precios limpios
cantidad_precios_limpios= 0

# Lista vacía para almacenar los datos correctos
precios_limpios=[]

# creacion del bucle for para recorrer la lista

for item in precios_crudos:
    # Condicion if
    if item <=0:
        precios_corruptos +=1
        continue
    else:
        cantidad_precios_limpios +=1
        precios_limpios.append(item)
        
# porciento que representan de los precios buenos o limpios
porcentaje= (precios_corruptos/len(precios_crudos))*100
print(f'La lista de precios limpios es : {precios_limpios}') 
print(f'cantidad de Precios Corruptos: {precios_corruptos}')   
print(f'Porcentaje de precios corruptos sobre limpios: {porcentaje}%')
