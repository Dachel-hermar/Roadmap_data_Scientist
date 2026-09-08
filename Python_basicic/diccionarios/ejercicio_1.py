"""
💻 Tu Primer Reto de Diccionarios (Sector RRHH)
El Contexto: Eres el Data Analyst del departamento de Recursos Humanos de una startup. Te han pedido que estructures el perfil digital de un nuevo fichaje.

Tu Tarea:

Crea un diccionario vacío o inicializado llamado empleado.
En el momento de crearlo (usando las llaves {}), asígnale 3 Claves iniciales y sus Valores (ejemplo: "nombre", "departamento", "salario").
Acaban de informarte que la empleada tuvo un desempeño estelar y la han ascendido. Usando la sintaxis de asignación por fuera de las llaves, actualiza su "salario" sumándole un bono numérico, y agrégale una clave totalmente nueva llamada "puesto_nuevo".
Imprime el diccionario completo al final (usando un f-string) para ver cómo luce la base de datos actualizada.
"""
# Creación del diccionario empleado con claves y valores iniciales
empleado={
    "nombre": "Ana",
    "departamento": "Marketing",
    "salario": 30000
}

# Actualización del salario y adición de una nueva clave
empleado["salario"] += 5000  # Se le suma un bono de 5000 al salario
empleado["puesto_nuevo"] = "Gerente de Marketing"  # Se agrega una nueva clave con su puesto actualizado    

print(f'El diccionario final es {empleado}')