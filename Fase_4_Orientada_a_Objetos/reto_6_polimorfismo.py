"""
RETO 6: El Escuadrón (Polimorfismo)

Contexto de Negocio:
El Polimorfismo ("Muchas Formas") permite que distintas clases tengan métodos 
con el EXACTO MISMO NOMBRE, pero que hagan cosas distintas.
Esto es vital para procesar listas de objetos variados sin tener que hacer 
docenas de condicionales (if/else).

Tu Misión:
1. La Madre Ciega: Crea una clase `Empleado`.
   - Su constructor pide `nombre`.
   - Tiene un método `trabajar(self)` que imprime "[nombre] está haciendo trabajo genérico."
2. Los Hijos Polimórficos: Crea dos clases `Programador(Empleado)` y `Gerente(Empleado)`.
   - ¡NO les crees __init__! Si no escribes constructor, heredarán el de la madre automáticamente.
   - ¡SOBRESCRIBE EL MÉTODO!: En ambas clases, crea el método `trabajar(self)`. 
     Esto anulará el método de la madre para ellos.
   - En el `Programador`, que imprima: "💻 [nombre] está picando código en Python."
   - En el `Gerente`, que imprima: "👔 [nombre] está en una reunión de 5 horas."
3. La Fábrica (La Magia del Bucle):
   - Fabrica un Empleado ("Juan"), un Programador ("Ana") y un Gerente ("Carlos").
   - Mételos a todos en una simple Lista: `empresa = [juan, ana, carlos]`.
   - Crea un bucle `for persona in empresa:`
   - Adentro del bucle, simplemente llama a `persona.trabajar()`.
"""

# ==========================================
# 1. LA GENÉTICA (Clase Madre y Clases Hijas)
# ==========================================
# Escribe tus clases aquí abajo...
class Empleado:
    def __init__(self, nombre):
        self.nombre= nombre
    def trabajar(self):
        print(f"{self.nombre} está haciendo trabajo genérico.")

class Programador(Empleado):
    def trabajar(self):
        print(f"💻 {self.nombre} está picando código en Python.")

class Gerente(Empleado):
    def trabajar(self):
        print(f"👔 {self.nombre} está en una reunión de 5 horas.")




# ==========================================
# 2. LA FÁBRICA (La Magia del Bucle Polimórfico)
# ==========================================
# Instancia, mételos en una lista y recórrelos...
empleado=Empleado("Juan")
programador=Programador("Ana")
gerente=Gerente("Carlos")

empresa = [empleado, programador, gerente]
for persona in empresa:
    print(persona)
    persona.trabajar()
