"""
💻 Reto 3/3: El Formato Universal (El Jefe Final)
Llegamos a la prueba de fuego del día de hoy. Vamos a hacer un "Reto Híbrido". En el mundo real del Análisis de Datos, cuando le pides información a una base de datos externa, a la nube, o a una página web (APIs), casi nunca te mandan un diccionario suelto. Te mandan una Lista gigante que contiene Diccionarios adentro. Esta estructura (Lista de Diccionarios) se conoce como Formato JSON, y es el estándar de transmisión de datos en todo el planeta Tierra.

El Contexto: Trabajas para una aplicación financiera con restricción legal de edad. La API te acaba de escupir en formato JSON los datos de los 3 usuarios que se registraron hoy. Necesitas aislar los nombres de los que SÍ son legales. Tus Datos:

python


registro_usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Juan", "edad": 17},
    {"nombre": "Luis", "edad": 30}
]
(Fíjate bien en la arquitectura: Es una Lista matemática de 3 elementos. Pero cada elemento no es un texto, ¡es un diccionario de datos completo!)

Tu Tarea Lógica:

Crea una lista vacía llamada usuarios_legales = [] para tu reporte limpio.
Crea el bucle clásico que recorra la lista registro_usuarios. (Ten en mente que en cada vuelta, tu variable iteradora tomará la forma de un diccionario entero).
Usa la lógica condicional para evaluar si la "edad" de ese diccionario específico es >= 18. (Recordatorio: Para leer el valor de un diccionario, se llama a su clave entre corchetes [ ]).
Si cumple la condición legal, guárdalo en tu lista limpia. Pero ojo a la regla de negocio: No quiero que guardes el diccionario entero, inyecta con tu .append() únicamente el "nombre" de esa persona.
Al finalizar el bucle, imprime tu lista de usuarios legales, que debería ser solo ['Ana', 'Luis'].
"""

# Datos
registro_usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Juan", "edad": 17},
    {"nombre": "Luis", "edad": 30}
]

# Contruccion de la lista vacía para almacenar solamente los usuarios que cumolen con la condicón que sean mayores de edad
usuarios_legales = []

# Creo un bucle for para recorrer la lista
for item in registro_usuarios:
    print(item)
    if item["edad"] >= 18:
        usuarios_legales.append(item["nombre"])
    
print(f"Los usuarios mayores de edad son: {usuarios_legales}")
       
    