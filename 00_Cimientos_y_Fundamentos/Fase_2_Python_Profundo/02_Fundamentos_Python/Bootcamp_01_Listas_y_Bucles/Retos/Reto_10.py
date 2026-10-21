"""
💻 Reto 10/10: El Jefe Final (Sector Retail / Logística)
El Contexto: Eres el cerebro del sistema automático de inventario de un almacén. 
Los camiones traen cajas (números positivos) y los clientes compran cajas (números negativos). 
Tus Datos: stock_actual = 50 (Cajas que hay en el almacén al abrir la persiana) 
operaciones = [10, -5, 20, -100, 5] (Las 5 transacciones del día)

Tu Tarea:

Haz un bucle que recorra las transacciones y las vaya sumando a tu stock_actual.
La Regla de Negocio (El Caso Borde Crítico): Físicamente es imposible tener "cajas negativas" (antimateria). 
Si en algún momento, tras procesar una operación, tu stock_actual cae por debajo de cero (ej. un cliente pide 100 cajas pero solo tenías 75), debes:

Imprimir una alarma visual: "ALERTA: Ruptura de stock detectada. Faltan cajas."
Modificar automáticamente tu stock_actual dejándolo en 0 (el almacén queda vacío).
Permitir que el bucle continúe normalmente (no usar break, porque luego pueden llegar más cajas en el siguiente camión).
Al finalizar el día (fuera del bucle), imprime: "El stock final en almacén es de [X] cajas".
"""
# stock en el almacen
stock_actual = 50
# Operaciones del dia compra y venta
operaciones = [10, -5, 20, -100, 5]

for transacciones in operaciones:
    stock_actual += transacciones
    if stock_actual < 0:
        print( "ALERTA: Ruptura de stock detectada. Faltan cajas.")
        stock_actual=0
        continue       
print(f'El stock final en almacén es de {stock_actual} cajas')      