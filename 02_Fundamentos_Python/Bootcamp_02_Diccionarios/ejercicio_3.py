"""
💻 Reto 2/3 de Diccionarios: El Filtro de Extracción
Ahora que sabes crear y acumular datos en un diccionario, vamos a enseñarte cómo se saca la información. Para recorrer un Diccionario entero, Python tiene un "truco" de sintaxis precioso. Como el diccionario vive en base a parejas (Clave/Valor), tú puedes pedirle al bucle que te escupa a la pareja junta usando el método .items().
El Contexto: Eres el Data Analyst del departamento de Finanzas. Tienes el registro encriptado de salarios. Tu jefe quiere saber los nombres de las personas que ganan un sueldo "Premium" (Alta Dirección) para revisar sus impuestos fiscales. Tus Datos: sueldos_plantilla = {"Juan": 3000, "Ana": 4500, "Pedro": 2500, "Maria": 5000, "Luis": 3200}

for clave, valor in mi_diccionario.items():
    # En cada vuelta, tienes dos variables disponibles al mismo tiempo

Tu Tarea:

Haz un bucle que recorra el diccionario extrayendo a los dos sujetos usando .items(). Nombra a las variables del bucle con sentido de negocio (ej. for empleado, sueldo in...).
Usa un condicional lógico. Si el sueldo de esa persona es estrictamente mayor a 3500, imprime un reporte que diga: "Alerta Fiscal: [Nombre] gana [Sueldo] euros".
Los que ganen 3500 o menos, el sistema los debe ignorar por completo.
"""

# Datos
sueldos_plantilla = {"Juan": 3000, "Ana": 4500, "Pedro": 2500, "Maria": 5000, "Luis": 3200}

# Crear el bucle for para leer los datos, para ello usaremos el método .items()
for empleado, salario in sueldos_plantilla.items():
    if salario > 3500:
        print(f"Alerta Fiscal: {empleado} gana {salario} euros")
    