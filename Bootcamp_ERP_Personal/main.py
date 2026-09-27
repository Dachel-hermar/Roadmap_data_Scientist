"""
CAPA DE INTERFAZ (CONTROLADOR): main.py

Contexto de Negocio:
¡Llegamos al final del Proyecto 1! Tienes un sótano robusto (`database.py`) y un 
cerebro pensante (`models.py`). Pero los usuarios normales no saben ejecutar funciones, 
necesitan una interfaz gráfica. 
Este archivo es tu Cajero Automático. Aquí es donde pondremos el bucle infinito y los 
inputs para que el usuario pueda usar tu ERP.

Tu Misión:
1. Importación:
   - Importa tu capa lógica: `from models import Compra`

2. El Bucle Infinito:
   - Crea un `while True:` que mantenga vivo el programa.

3. El Menú Visual:
   - Imprime un menú con las siguientes opciones:
     1. Registrar una nueva compra
     2. Ver gasto total global
     3. Ver gasto por producto (agrupado)
     4. Buscar cuánto gasté en un producto específico
     5. Salir

4. El Cerebro del Menú (if/elif):
   - Pide al usuario que elija una opción mediante un `input()`.
   - Si elige 1: Pide por input el nombre, precio, supermercado y fecha.
     - Protege el precio con un `try/except ValueError` para que el programa no explote si el usuario escribe "veinte" en lugar de `20`.
     - Instancia tu objeto: `nueva_compra = Compra(nombre, precio, supermercado, fecha)`
     - Mándala a guardar: `nueva_compra.guardar_en_sql()`
   - Si elige 2: Ejecuta y printea el método estático correspondiente de tu clase Compra.
   - Si elige 3: Ejecuta y printea el método estático correspondiente.
   - Si elige 4: Pide al usuario que escriba la palabra clave a buscar, y pásasela al método estático correspondiente.
   - Si elige 5: Despídete, y ejecuta un `break` para apagar el sistema.
"""

# ==========================================
# ESCRIBE TU CONTROLADOR AQUÍ
# ==========================================
from models import Compra
while True:
    print(f'{"=="*20}CARGANDO OPCIONES{"=="*20}') 
    print(f"ELIGE UNA DE LAS SIGUIENTES OPCIONES\n 1. Registrar una nueva compra\n 2. Ver gasto total global\n 3. Ver gasto por producto (agrupado)\n 4. Buscar cuánto gasté en un producto específico\n 5. Consultar la cantidad de productos por Supermercado\n 6. Cantidad gastado por super\n 7.Salir ")
    try:
        opcion=int(input("ELIGA UNA OPCIÓN:   "))
        if opcion ==1:
            nombre=input("Agregue el nombre del producto:  ").title()
            precio=float(input("Agregue el valor del producto:  "))
            supermercado=input("Agregue el nombre del Super:  ").title()
            fecha= input("Agregue la fecha:  ")
            nueva_compra = Compra(nombre, precio, supermercado, fecha)
            nueva_compra.guardar_en_sql()

        if opcion==2:
            print(Compra.gasto_total())

        if opcion==3:
            print(Compra.valor_total_por_producto())

        if opcion==4:
            product_name=input("Ingresa el nombre del producto que quieas consultar:  ")
            print(Compra.cuanto_hemos_gastado_en(product_name))
       
                  
        if opcion==5:
            print(Compra.cantidad_por_super())

        if opcion==6:
            print(Compra.total_por_super())

        if opcion==7:
            print("HASTA PRONTO")
            break
                  
    except Exception as e:
        print("Se ha detectado un error {e}, por favor compruebe, el dato introducido")
        break


    
