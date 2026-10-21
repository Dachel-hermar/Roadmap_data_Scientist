"""
RETO 8: El Molde Inteligente (Decoradores: @staticmethod y @classmethod)

Contexto de Negocio:
Hasta ahora, todos tus métodos llevaban `self`, porque necesitaban alterar la memoria 
de una instancia específica (Ej: la cuenta de Carlos). 
Pero, ¿qué pasa si quieres que un método pertenezca a la Clase en sí, sin necesidad 
de instanciar a nadie? Para eso usamos los Decoradores (el símbolo @).

Tu Misión:
1. Crea la clase `CalculadoraFinanciera`. 
   - ¡NO escribas __init__! (No necesitamos guardar estado individual hoy).
2. Un Atributo de Clase (Fuera de los métodos):
   - Justo debajo de la declaración de la clase, escribe: `tasa_interes = 0.05`
3. El Static Method (El utilitario):
   - Usa el decorador `@staticmethod` una línea antes de definir tu método.
   - Crea `def sumar(a, b):` (¡OJO! No lleva `self`, porque no toca el estado interno).
   - Retorna la suma de a y b.
4. El Class Method (El controlador del molde):
   - Usa el decorador `@classmethod`.
   - Crea `def ver_tasa(cls):` (¡OJO! Lleva `cls` de Class, no `self`).
   - Retorna `cls.tasa_interes`.
5. La Fábrica (¡SIN INSTANCIAR!):
   - Afuera de la clase, NO crees ninguna variable. Llama a los métodos 
     directamente usando el nombre del Molde.
   - Imprime: `CalculadoraFinanciera.sumar(10, 50)`
   - Imprime: `CalculadoraFinanciera.ver_tasa()`
"""

# ==========================================
# 1. EL MOLDE INTELIGENTE (Decoradores)
# ==========================================
# Escribe tu clase aquí abajo...

class CalculadoraFinanciera:

   tasa_interes = 0.05
   @staticmethod
   def sumar(a,b):
      return a+b
   @classmethod
   def ver_tasa(cls):
      return cls.tasa_interes

# ==========================================
# 2. LA FÁBRICA (Pruebas sin Instanciación)
# ==========================================
# Llama a los métodos directamente usando la Clase...
print(CalculadoraFinanciera.sumar(10, 50))
print(CalculadoraFinanciera.ver_tasa())
