"""
RETO 7: La Magia Oculta (Métodos Dunder)

Contexto de Negocio:
En el Reto 6, notaste que al imprimir un objeto (`print(gerente)`), Python te arrojaba 
basura de memoria: `<__main__.Gerente object at 0x00...>`
Los "Dunder Methods" (Doble Underscore) son métodos nativos que empiezan y terminan con `__`.
Sirven para decirle a Python cómo debe comportarse tu objeto ante comandos básicos 
como `print()` o `len()`.

Tu Misión:
1. La Entidad: Crea la clase `CarritoCompras`.
2. El Estado (`__init__`): Pide el `cliente` e inicializa una lista vacía `self.articulos = []`.
3. Comportamiento Estándar: Crea un método `agregar(self, item)` que le haga un `.append()` 
   a la lista de artículos.
4. MAGIA 1 (`__str__`): Este método define la "cara" de tu objeto.
   - Crea: `def __str__(self):`
   - DEBE retornar un string. Haz que retorne: "🛒 Carrito de [cliente]".
5. MAGIA 2 (`__len__`): Este método define la "longitud" de tu objeto.
   - Crea: `def __len__(self):`
   - DEBE retornar un entero. Haz que retorne la longitud nativa de la lista: `len(self.articulos)`.
6. La Fábrica:
   - Crea un carrito para ti.
   - Agrégale 3 strings al azar (Ej: "Manzana", "Laptop", "Libro").
   - Imprime el objeto directamente: `print(carrito)` (¡Ya no saldrá basura de memoria!).
   - Imprime su longitud directamente: `print(len(carrito))` (¡Python sabrá contar tus artículos!).
"""

# ==========================================
# 1. EL MOLDE MÁGICO (Clase y Dunders)
# ==========================================
# Escribe tu clase aquí abajo...
class CarritoCompras:
    def __init__(self, cliente):
        self.cliente=cliente
        self.articulos=[]
    def agregar(self, item):
        self.articulos.append(item)
    def __str__(self):
        return f"🛒 Carrito de {self.cliente}"

    def __len__(self):
        return len(self.articulos)
    




# ==========================================
# 2. LA FÁBRICA (Pruebas de Magia)
# ==========================================
# Instancia, agrega items e imprime...
carrito_compra=CarritoCompras("Dachel")

carrito_compra.agregar("Querer")
carrito_compra.agregar("Crecer")
carrito_compra.agregar("Rápido")
carrito_compra.agregar("pero")
carrito_compra.agregar("no")
carrito_compra.agregar("Ciego")
print(carrito_compra)
print(len(carrito_compra))
