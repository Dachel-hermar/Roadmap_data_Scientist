"""
CAPA DE LÓGICA DE NEGOCIO: models.py

Contexto de Negocio:
Este archivo es el "Cerebro" de tu aplicación. 
Aquí usaremos Programación Orientada a Objetos para crear las reglas de negocio.
Este archivo NO debe saber cómo funciona el SQL por dentro; en su lugar, debe 
"importar" y usar las funciones que creaste en tu esclavo `database.py`.

Tu Misión:
1. Importación:
   - Haz un `import database`.

2. La Clase:
   - Crea la clase `Inventario`.

3. El Constructor (`__init__`):
   - No necesitas pedir parámetros.
   - Adentro, simplemente manda a llamar a `database.crear_tabla_productos()`. 
     Así garantizas que la tabla exista apenas prendas el programa.

4. Método 1: `registrar_compra(self, nombre, precio, supermercado, fecha)`
   - Antes de guardar, implementa una regla de negocio (Encapsulamiento de lógica):
     Si el `precio` es menor o igual a 0, imprime un error "El precio debe ser mayor a 0" y haz un `return` vacío (para matar la función).
   - Si todo está bien, manda a llamar a `database.insertar_producto(nombre, precio, supermercado, fecha)`
   - Imprime "¡Compra registrada con éxito!".

5. Método 2: `ver_gasto_total(self)`
   - Llama a `database.consultar_productos()` y guarda la lista de tuplas en una variable (ej: `compras`).
   - Usa un bucle `for` o una List Comprehension para sumar todos los precios. 
     (Recuerda que el precio es el índice 2 de cada tupla: `fila[2]`).
   - Retorna el número total.

6. Prueba en Cuarentena:
   - Escribe tu `if __name__ == '__main__':`
   - Instancia tu clase: `mi_inventario = Inventario()`
   - Usa el método para registrar un "Atún" de 2.50 en "Dia".
   - Imprime tu método de ver gasto total.
"""

# ==========================================
# ESCRIBE TU LÓGICA AQUÍ
# ==========================================
import database

class GastoBase:
    # 1. El ADN entra directo en el nacimiento
    def __init__(self,tabla, nombre, cantidad, precio,  supermercado, fecha):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.supermercado = supermercado
        self.fecha = fecha
        self.tabla = tabla
        database.crear_tabla_productos(tabla) # (Garantizamos que la BD exista)
       

    # 2. El método de acción ya NO necesita pedir parámetros
    def guardar_en_sql(self):
        if self.precio <= 0:
            print("Error: Precio inválido")
            return
        
        # El objeto envía su PROPIO ADN a la base de datos
        database.insertar_producto(self.tabla, self.nombre, self.cantidad, self.precio, self.supermercado, self.fecha)
        print("¡Compra registrada en el disco duro!")

    @staticmethod
    def valor_total_por_producto(tabla):
        respuesta= database.gasto_por_producto(tabla)
        resultado= "Reporte de Gastos:\n"
        for item in respuesta:
            nombre_producto= item[0]
            gasto_total= item[1]
            resultado += f"En {nombre_producto} has gastado un total de €{gasto_total}\n"
        return resultado
    
    @staticmethod
    def cantidad_por_super(tabla):
        respuesta=database.registros_por_productos(tabla)
        resultado= "Reporte de Registros:\n"
        for item in respuesta:
            nombre_producto= item[0]
            supermercado= item[1]
            cantidad_total= item[2]
            resultado += f"En {supermercado} has comprado un total de {cantidad_total} unidades de {nombre_producto}\n"
        return resultado

    @staticmethod
    def gasto_total(tabla):
        gasto = database.consultar_gasto_global(tabla)
        total_limpio = gasto[0][0]
        return f"Tu gasto histórico global es de: €{total_limpio}"
      
    @staticmethod
    def cuanto_hemos_gastado_en(tabla, nombre_del_producto):
    # La fábrica recibe la palabra y busca en SQL
      respuesta=database.consultar_producto_especifico(tabla,nombre_del_producto)
      if len(respuesta) == 0:
          return f"El producto {nombre_del_producto} no existe."
      else:
          # Sacamos el nombre y el precio de la caja Decimal
          nombre_producto = respuesta[0][0]
          gasto_total = respuesta[0][1]
          
          # Armamos un mensaje elegante y limpio
          return f"En {nombre_producto} has gastado un total de €{gasto_total}"
      
    
    @staticmethod
    def total_por_super(tabla):
        respuesta = database.total_gastado_por_supermercado(tabla)
        resultado = "Reporte de Gastos por Supermercado:\n"
        for item in respuesta:
            supermercado = item[0]
            total_gastado = item[1]
            resultado += f"En {supermercado} has gastado un total de €{total_gastado}\n"
        return resultado


    @staticmethod
    def borrar_registro(tabla, id_registro):
        database.borrar_registros(tabla, id_registro)
        print(f"Registro con ID {id_registro} borrado exitosamente.")

    @staticmethod
    def modificar_precio(tabla,id_registro, nuevo_precio):
        database.modificar_precio(tabla, id_registro, nuevo_precio)
        print(f"Registro con ID {id_registro} modificado exitosamente. Nuevo precio: {nuevo_precio}")

class GastoSupermercado(GastoBase):
    def __init__(self, nombre, cantidad, precio, supermercado, fecha):
        super().__init__("productos", nombre, cantidad, precio, supermercado, fecha)
        

class GastoGato(GastoBase):
    def __init__(self, nombre, cantidad, precio, supermercado, fecha):
        super().__init__("gastos_gato", nombre, cantidad, precio, supermercado, fecha)





if __name__ == '__main__':
    # Prueba de la clase GastoBase
    mi_gato = GastoGato("Pienso", 2, 14.50, "Kiwoko", "2026-10-06")
    mi_gato.guardar_en_sql()
    print(mi_gato.gasto_total("gastos_gato"))


    mi_compra = GastoSupermercado("Leche", 2, 1.50, "Mercadona", "2026-09-25")
    mi_compra.guardar_en_sql()
    print(mi_compra.valor_total_por_producto("productos"))
