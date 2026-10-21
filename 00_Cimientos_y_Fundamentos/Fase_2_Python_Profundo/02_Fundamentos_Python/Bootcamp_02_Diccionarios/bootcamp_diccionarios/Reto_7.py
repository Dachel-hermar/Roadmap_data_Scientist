"""
💻 Reto 7/10: Detección de Fuerza Bruta (Sector Ciberseguridad)

El Contexto de Negocio: Sigues en el equipo de Ciberseguridad. 
Tienes frente a ti la base de datos en vivo que registra los intentos de inicio de sesión fallidos de los usuarios de la plataforma. 
Las políticas de seguridad de la empresa dictan que cualquier usuario con 3 o más intentos fallidos debe ser neutralizado inmediatamente para proteger los servidores de un ataque de fuerza bruta.

Tus Datos Crudos:

python


intentos_login = {
    "user_101": 1,
    "user_204": 4,
    "admin_root": 0,
    "hacker_99": 7,
    "ceo_boss": 2
}

Tu Tarea Lógica:

En este escenario, está prohibido crear un diccionario nuevo. Vamos a editar la base de datos original directamente (aprovechando que los diccionarios son mutables).
Inicia tu bucle especializado para revisar las cuentas.
Si el número de intentos del usuario evaluado supera o iguala el límite rojo, debes actualizar (sobreescribir) su valor numérico en el diccionario, cambiándolo por el texto "BLOQUEADO".
Al finalizar tu patrullaje, tu Jefe de Seguridad espera ver impreso el diccionario original modificado (con los intrusos neutralizados y los usuarios legítimos manteniendo sus números intactos).
(Un recordatorio conceptual: Ya sabes cómo machacar/actualizar el valor de una clave que ya existe. Lo hiciste magistralmente en tu primer ejercicio de RRHH cuando le cambiaste el puesto a la empleada Ana: diccionario[clave] = nuevo_valor).
"""

# Datos

intentos_login = {
    "user_101": 1,
    "user_204": 4,
    "admin_root": 0,
    "hacker_99": 7,
    "ceo_boss": 2
}

# Objetivo:
"""
Si el ususario ha tenido 3 o más intentos fallidos
Cambiar el valor de su clave identificativa a "BLOQUEADO"
"""
# Pasos
# 1. reorrer todo el diccionario, para extraer sus valores, a traves de un bucle for
# 2. Comparar si el valor de la clave es mayor o igual a 3, a traves de una condicion if
# 3. Si se cumple la condición que estamos evaluando, modificar el valor de la clave por el Texto "Bloquedo"
# 4. Si no mantener como está
# 5. Imprimir el diccionario

# Creación de un bucle for
for usuario, values in intentos_login.items():
    if values >= 3:
        intentos_login[usuario]="BLOQUEADO"
print(intentos_login)