"""
Bootcamp Ejercicio 6/10: Despidos Masivos (El Peligro de Mutar)

REGLAS MILITARES:
1. Cero teoría nueva.
2. Todo encapsulado en una Función (def).
"""

# REQUERIMIENTO DE NEGOCIO:
# Sigues siendo el Analista de Recursos Humanos. 
# La startup se quedó sin fondos. El CEO exige que despidas (borres) del sistema 
# a cualquier empleado que gane ESTRICTAMENTE MÁS de $6000.
# Además, exige saber exactamente cuánto dinero se ahorró la empresa con esta limpieza.
#
# Construye una función 'recorte_personal' que reciba el diccionario.
# 1. Crea una lista vacía para guardar los nombres de los condenados.
# 2. Recorre el diccionario y añade a los condenados a la lista (así evitas el RuntimeError de mutar mientras iteras).
# 3. Crea un acumulador 'ahorro_total = 0'.
# 4. Haz un segundo bucle sobre la lista de condenados. Bórralos del diccionario original usando '.pop()'.
# 5. Atrapa el valor que escupe '.pop()' y súmalo a tu acumulador de ahorros.
# 6. Imprime un reporte final para el CEO con el monto ahorrado y devuelve el diccionario limpio.

nomina_actual = {
    "Ana": 4500,
    "Luis": 6000,
    "Carlos": 3200,
    "Sofia": 7500,
    "Miguel": 4999,
    "Roberto": 8000
}

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def recorte_personal(nomina):
    condenados=[]
    for nombre, salario in nomina.items():
        if salario > 6000:
            condenados.append(nombre)

    print(condenados)
    ahorro_total=0
    for nombre in condenados:
        print(nombre)
        ahorro_total+= nomina.pop(nombre)
    print(f"Despedimos a {condenados}. Nos hemos ahorrado ${ahorro_total}.")
    return nomina 
  
        
   


# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí y haz un print. 
Empleados_eliminados= recorte_personal(nomina_actual)
# Solo deberían sobrevivir Ana, Luis (gana 6000 exactos, se salva), Carlos y Miguel.
print(Empleados_eliminados)

