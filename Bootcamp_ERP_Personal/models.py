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

class Compra:
    # 1. El ADN entra directo en el nacimiento
    def __init__(self, nombre, precio, supermercado, fecha):
        self.nombre = nombre
        self.precio = precio
        self.supermercado = supermercado
        self.fecha = fecha
        database.crear_tabla_productos() # (Garantizamos que la BD exista)

    # 2. El método de acción ya NO necesita pedir parámetros
    def guardar_en_sql(self):
        if self.precio <= 0:
            print("Error: Precio inválido")
            return
        
        # El objeto envía su PROPIO ADN a la base de datos
        database.insertar_producto(self.nombre, self.precio, self.supermercado, self.fecha)
        print("¡Compra registrada en el disco duro!")

    @staticmethod
    def valor_total_por_producto():
        return database.gasto_por_producto()
    
    @staticmethod
    def cantidad_por_super():
        return database.registros_por_productos()

    @staticmethod
    def gasto_total():
        gasto=database.consultar_gasto_global()
        return gasto
      
    @staticmethod
    def cuanto_hemos_gastado_en(nombre_del_producto):
    # La fábrica recibe la palabra y busca en SQL
      respuesta=database.consultar_producto_especifico(nombre_del_producto)
      if respuesta[0][0] is None:
          return f"El producto {nombre_del_producto} no existe."
      else:
          return respuesta
      
    
    @staticmethod
    def total_por_super():
        return database.total_gastado_por_supermercado()


       
            
        
if __name__ == '__main__':
    # Nace el objeto (Ya sabe que es un Atún)
   compra_1 = Compra("Atún", 2.80, "Dia", '2026-09-27')
   # El objeto se guarda a sí mismo en SQL
   compra_1.guardar_en_sql()
   # Le preguntas a la pared de la fábrica el total global
   print(Compra.gasto_total())
   print(Compra.cuanto_hemos_gastado_en("Arroz"))
   print(Compra.total_por_super())
   
