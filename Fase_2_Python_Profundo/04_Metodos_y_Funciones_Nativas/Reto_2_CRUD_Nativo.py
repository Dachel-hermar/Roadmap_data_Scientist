"""
Reto 2: El Cirujano de Datos (Operaciones CRUD Nativas)

Contexto de Negocio:
En la Ingeniería de Software, todas las bases de datos del mundo se rigen por 4 pilares:
CRUD (Create, Read, Update, Delete - Crear, Leer, Actualizar, Borrar).
En Python, no siempre tienes que crear estructuras vacías para armar una nueva. 
A veces tu misión es operar de forma clínica sobre bases de datos que ya existen.

MÉTODOS NATIVOS DE DESTRUCCIÓN E INYECCIÓN A DOMINAR HOY:
1. .insert(indice, valor): Inyecta un dato en una Lista en la posición exacta que quieras.
2. .remove(valor): Busca a ciegas un elemento por su VALOR en una Lista y lo destruye.
3. .pop(indice): Extrae (y borra) un elemento de una Lista guiándose por su POSICIÓN. Si se deja vacío .pop(), arranca el último elemento de la cola.
4. del diccionario[llave]: El francotirador. Destruye permanentemente una llave de un Diccionario.
"""

# =========================================================
# LA SALA DE URGENCIAS (El Sistema del Hospital)
# =========================================================
# Eres el Arquitecto de Datos de un hospital.
# Tienes la cola de la sala de espera (Lista) y el registro de camas (Diccionario).

sala_espera = ["Carlos", "Ana", "Luis", "Marta"]
registro_camas = {"Cama_1": "Pedro", "Cama_2": "Vacia", "Cama_3": "Juan"}

print("--- ESTADO INICIAL ---")
print(f"Sala: {sala_espera}")
print(f"Camas: {registro_camas}")
# TAREA 1 (Inyección): Llegó una paciente en estado de emergencia llamada "Sofía". 
# Debe saltarse toda la cola e ir directamente al primer lugar de la fila.
# Usa el método .insert() en la sala_espera.
sala_espera.insert(0,"Sofía")


# TAREA 2 (Búsqueda y Destrucción): "Luis" se curó mágicamente y se fue a su casa.
# Búscalo por su texto y elimínalo de la lista.
# Usa el método .remove() en la sala_espera.
sala_espera.remove("Luis")


# TAREA 3 (Extracción de Posición): El médico abre la puerta y llama al primer paciente 
# de la fila para atenderlo. Quita al que esté en la primera posición.
# Usa el método .pop() en la sala_espera.
sala_espera.pop(0)


# TAREA 4 (Eliminación de Hash): El hospital va a entrar en remodelación y decidieron 
# destruir físicamente la "Cama_2".
# Bórrala permanentemente de la base de datos del hospital usando el comando 'del'.
del registro_camas["Cama_2"]

print("\n--- ESTADO FINAL AUDITADO ---")
print(f"Sala: {sala_espera}")
print(f"Camas: {registro_camas}")
