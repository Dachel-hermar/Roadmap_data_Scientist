"""
RETO 2 del 3x3: El Cajero Seguro (Validación de Estado)

Contexto de Negocio:
Implementar una regla de validación para evitar sobregiros (saldos negativos).

Tu Misión:
1. Agrega el método `retirar(self, monto)` a la clase.
2. Adentro, usa un if/else para proteger el `self.saldo`:
   - Si el saldo alcanza o sobra, descuenta y aprueba (✅).
   - Si el saldo no alcanza, bloquea y rechaza (❌).
3. Prueba el sistema fabricando la cuenta de Carlos ($1000).
   - Retiro 1: $1500 (Debe fallar).
   - Retiro 2: $200 (Debe pasar).
"""

# ==========================================
# 1. EL MOLDE (La Entidad y sus Guardianes)
# ==========================================
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        print(f"✅ Depósito de ${monto} exitoso. Nuevo saldo de {self.titular}: ${self.saldo}")

    # TODO: Construye tu método retirar() aquí abajo...
    def retirar(self,monto):
        if monto <= self.saldo:
            self.saldo-=monto
            print(f"✅ Retiro de ${monto} exitoso. Nuevo Saldo: ${self.saldo}")
        else:
            print(f"❌ Operación Rechazada: Fondos insuficientes para retirar ${monto}")

    



# ==========================================
# 2. LA FÁBRICA (Pruebas de Quality Assurance)
# ==========================================
# TODO: Crea a Carlos y pon a prueba su cuenta aquí abajo...
cliente= CuentaBancaria("Carlos", 330)
cliente.retirar(490)
cliente.depositar(40)
cliente.retirar(340)

