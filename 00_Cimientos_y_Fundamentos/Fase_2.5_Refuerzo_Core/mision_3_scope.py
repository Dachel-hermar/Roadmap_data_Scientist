presupuesto_corporativo = 50000

def registrar_empleado(nombre, salario, departamento="General"):
    global presupuesto_corporativo
    # Intentamos descontar el salario del presupuesto matriz
    presupuesto_corporativo = presupuesto_corporativo - salario
    print(f"✅ {nombre} registrado en {departamento}. Quedan ${presupuesto_corporativo}")

# El Junior intenta registrar a Carlos
registrar_empleado("Carlos", 40000, "Ventas")
registrar_empleado("Sofia", 8000)
