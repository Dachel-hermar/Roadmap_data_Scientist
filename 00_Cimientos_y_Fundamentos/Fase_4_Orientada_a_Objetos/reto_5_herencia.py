"""
RETO 5: La Genética Corporativa (Herencia y super)

Contexto de Negocio:
Una empresa tech se cansó de escribir el mismo código para todos sus tipos de empleados.
Necesitan una Clase Madre que contenga la lógica básica, y Clases Hijas que hereden 
esa lógica pero tengan sus propias habilidades especiales.

Tu Misión:
1. La Clase Madre: Define la clase `Empleado`.
   - Constructor (`__init__`): Pide `nombre` y `salario`. Guárdalos en `self`.
   - Comportamiento: Crea un método `fichar(self)` que imprima "[nombre] ha fichado su entrada."
2. La Clase Hija: Define la clase `Programador(Empleado)`. (El paréntesis indica quién es su madre).
   - Constructor: Pide `nombre`, `salario` y `lenguaje`.
   - ¡LA MAGIA!: Adentro de este constructor, llama al constructor de la madre usando 
     `super().__init__(nombre, salario)`. 
   - Luego, guarda el atributo exclusivo del hijo: `self.lenguaje = lenguaje`.
   - Comportamiento Exclusivo: Crea un método `programar(self)` que imprima 
     "[nombre] está escribiendo en [lenguaje]".
3. Las Pruebas (Fábrica):
   - Fabrica un Programador llamado "Carlos", con salario 4000 y lenguaje "Python".
   - Demuestra la genética: Llama a `carlos.fichar()` (Heredado de la madre).
   - Demuestra la especialización: Llama a `carlos.programar()` (Exclusivo del hijo).
"""

# ==========================================
# 1. EL MOLDE MADRE (Superclase)
# ==========================================
# Escribe la clase Empleado aquí...
# Definiendo la clase madre
class Empleado:
    """
    Clase Madre dentro de esta vivirá la lógoca básica repetitiva
    """
    def __init__(self, nombre, salario):
        """"
        Constructor de comportamiento inicial de la clase, esta instancia la clase con los argumentos dados
        Args:
        nombre: nombre del trabajador
        salario: salario del trabajador
        """
        self.nombre=nombre
        self.salario=salario

    def fichar(self):
        """
        Método de la clase para el fichaje de cada trabajador
        """
        print(f'El trabajador {self.nombre} a fichado su entrada')

class Programador(Empleado): # El uso de parentisis dentro de la contruccion de una clase indica que hereda como parametro una clase madre
    def __init__(self, nombre, salario, lenguaje):
        """
        Con esto definimos el Constructor de la clase hija, la cual tiene como argumentos los datos de los empleados
        Args:
        nombre: nombre del trabajador
        salario: salario del trabajador
        lenguaje: lenguaje en que programa el empleado
        """
        super().__init__(nombre, salario)
        self.lenguaje=lenguaje
    def programar(self):
        print(f"{self.nombre} está escribiendo en {self.lenguaje}")
        
    



# ==========================================
# 2. EL MOLDE HIJO (Subclase)
# ==========================================
# Escribe la clase Programador aquí...
trabajador=Programador("Carlos",40000,"Python")
trabajador.fichar()
trabajador.programar()
persona= Empleado("Dachel", 40000)
persona.fichar()



# ==========================================
# 3. LA FÁBRICA (Pruebas de Genética)
# ==========================================
# Fabrica a Carlos y hazlo fichar y programar...

