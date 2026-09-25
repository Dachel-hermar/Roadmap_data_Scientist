"""
RETO 9: El Lenguaje Acelerado (List Comprehension y Lambda)

Contexto de Negocio:
Un Data Scientist no tiene tiempo para escribir bucles `for` de 5 líneas solo para 
limpiar una columna de nombres. Necesita comprimir esa lógica en 1 sola línea 
para mantener la velocidad de procesamiento.

Tu Misión:
1. List Comprehension (El bucle comprimido):
   - Tienes la lista: `nombres_crudos = [" ANA", "pedro ", "  carlos", "JUAN"]`
   - Crea la variable `nombres_limpios`.
   - Usa una List Comprehension (corchetes `[]`) para iterar sobre `nombres_crudos`.
   - A cada nombre aplícale los métodos `.strip()` (para borrar espacios) y `.title()` (para mayúscula inicial).
   - Sintaxis base: `[accion for item in lista]`
   
2. Funciones Lambda (El método desechable):
   - Crear una función matemática con `def` gasta memoria. 
   - Crea una variable llamada `calcular_iva`.
   - Asígnale una función Lambda que reciba un parámetro `precio` y retorne `precio * 1.21`.
   - Sintaxis base: `lambda parametro: operacion`

3. La Fábrica (Pruebas):
   - Imprime `nombres_limpios` (Deben verse perfectos: ['Ana', 'Pedro', ...]).
   - Imprime el resultado de llamar a `calcular_iva(100)` (Debe dar 121.0).
"""

# ==========================================
# 1. LIST COMPREHENSION (Limpieza de Datos)
# ==========================================
nombres_crudos = [" ANA", "pedro ", "  carlos", "JUAN"]
# Escribe tu List Comprehension aquí abajo...
nombres_limpios=[nombre.strip().title() for nombre in nombres_crudos]

calcular_iva= lambda precio: precio*1.21



# ==========================================
# 2. FUNCIÓN LAMBDA (Matemática rápida)
# ==========================================
# Escribe tu función Lambda aquí abajo...
print(nombres_limpios)
print(calcular_iva(100))



# ==========================================
# 3. LA FÁBRICA (Impresiones)
# ==========================================
# Imprime tus resultados aquí abajo...

