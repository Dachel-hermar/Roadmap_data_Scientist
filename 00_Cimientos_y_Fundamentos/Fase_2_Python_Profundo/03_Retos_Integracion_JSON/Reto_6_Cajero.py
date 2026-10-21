"""
Reto de Integración 6/6: El Arquitecto de Datos (Cierre de Caja)

Contexto de Negocio: Eres el Arquitecto de Datos principal de un E-Commerce.
Al final del día, el servidor te envía un único JSON gigante con todas las 
transacciones de la jornada. 

El CEO necesita dos cosas urgentemente antes de cerrar la contabilidad:
1. Saber exactamente cuánto dinero ingresó a la cuenta del banco (Facturación total).
2. Tener una lista con los "IDs" de los clientes cuyas tarjetas fueron rechazadas, 
   para que el equipo de soporte los llame por teléfono mañana.
"""

# Tus Datos Crudos (JSON de Producción):
corte_de_caja = {
    "fecha": "2026-09-09",
    "sucursal": "Tienda Online",
    "transacciones": [
        {"id_cliente": 101, "monto": 150.50, "pago_exitoso": True},
        {"id_cliente": 102, "monto": 50.00,  "pago_exitoso": False}, # Tarjeta rechazada
        {"id_cliente": 103, "monto": 300.00, "pago_exitoso": True},
        {"id_cliente": 104, "monto": 25.00,  "pago_exitoso": False}, # Tarjeta rechazada
        {"id_cliente": 105, "monto": 120.00, "pago_exitoso": True}
    ]
}

# 1. Crea tu acumulador de dinero: 
facturacion_total = 0
# 2. Crea tu lista de alarmas: 
tarjetas_rechazadas = []

# 3. Extrae la lista de "transacciones" del JSON principal usando .get()
diccionario_transacciones= corte_de_caja.get("transacciones")
# print(diccionario_transacciones)
# 4. Inicia tu bucle para auditar las transacciones extraídas
for item in diccionario_transacciones:
    # Si el pago_exitoso es True -> suma el monto a la facturacion_total
    if item["pago_exitoso"]:
        facturacion_total+=item.get("monto")
        # Si no (else) -> inyecta el id_cliente en la lista de tarjetas_rechazadas
    else:
        tarjetas_rechazadas.append(item.get("id_cliente"))


# 5. Imprime los dos reportes para el CEO
print(f'La facturación total para la fecha {corte_de_caja["fecha"]}, en la sucursal {corte_de_caja["sucursal"]}, fue de ${facturacion_total:.4f} dólares ')
print(f'Los id de los clientes cuyas tarjetas han sido rechazadas son los siguientes: {tarjetas_rechazadas}')