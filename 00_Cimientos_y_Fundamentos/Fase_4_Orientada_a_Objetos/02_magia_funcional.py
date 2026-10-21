precios_crudos = [100, 200, 300, 400]
precios_con_iva_senior = [precio * 1.21 for precio in precios_crudos]
print(precios_con_iva_senior)
# El filtro (if) siempre se incrusta al final, después de la declaración del for:
precios_caros = [precio for precio in precios_crudos if precio > 250]
print(f"Los precios filtrados son: {precios_caros}")