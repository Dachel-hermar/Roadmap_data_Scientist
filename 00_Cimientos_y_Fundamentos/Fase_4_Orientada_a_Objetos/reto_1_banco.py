"""
RETO 1 del 3x3: El Sistema Bancario (Fundamentos OOP)

Contexto de Negocio:
El Banco Central necesita que construyas el núcleo de su nuevo sistema financiero, aislando 
el dinero de los clientes mediante Programación Orientada a Objetos.

Tu Misión (Arquitectura sin cajas negras):
1. La Entidad: Crea la clase `CuentaBancaria`.
2. El Estado (__init__): El constructor debe exigir el nombre del `titular` y el `saldo_inicial`.
   - Guárdalos en la memoria del objeto usando `self`.
3. El Comportamiento: Crea un método llamado `depositar(self, monto)`. 
   - Debe sumarle el `monto` al saldo actual del objeto.
   - Debe imprimir: "✅ Depósito de $[monto] exitoso. Nuevo saldo de [titular]: $[saldo_actual]"
4. La Instanciación (Afuera de la clase, en el bloque principal):
   - Fabrica una cuenta para "Ana" con $500.
   - Usa el método depositar de Ana para ingresarle $250.

¡No uses variables globales! Todo debe vivir dentro de la Clase.
"""

# ==========================================
# 1. EL MOLDE (La Clase y sus Métodos)
# ==========================================
# Escribe tu clase aquí abajo...
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular= titular
        self.saldo= saldo_inicial

    def depositar(self,monto):
        self.saldo += monto
        print(f"✅ Depósito de ${monto} exitoso. Nuevo saldo de {self.titular}: ${self.saldo}")
    

    




# ==========================================
# 2. LA FÁBRICA (Instanciación y Pruebas)
# ==========================================
# Escribe tus pruebas aquí abajo...
cuenta_ana=CuentaBancaria("Ana", 500)
cuenta_ana.depositar(35)

# Conclusiones:
# Si la clase nace con x cantidades de argumentos, cuando se instancia la misma, debe de instanciarse con la misma cantidad de argumentos
# Los comportamiento de las funciones dentro de estas clases también pueden nacer con una cantidad de argumentos, ahora cuando llamamos a
# este método debe de también llamarse con los argumentos con los que nacio

