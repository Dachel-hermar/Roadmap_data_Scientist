"""
💻 Reto 6/10: El Criptógrafo (Sector Machine Learning / NLP)

El Contexto de Negocio: En el campo de la Inteligencia Artificial (específicamente en NLP: Natural Language Processing), 
las máquinas no pueden leer textos. Solo entienden la frecuencia de los números. 
El paso cero para entrenar a una IA (como ChatGPT) es crear un algoritmo que desmiembre un texto largo y 
convierta las palabras o letras en un diccionario matemático que cuente sus repeticiones.

Tus Datos Crudos:

python


mensaje_encriptado = "misterio"

Tu Tarea Lógica:

Crea tu clásico "Diccionario Acumulador" vacío.
Tienes que recorrer el mensaje letra por letra.
Aplica tu infalible lógica del Group By (la misma de la caja registradora del supermercado): ¿La letra ya existe registrada en el diccionario? Súmale 1. ¿Es una letra totalmente nueva? Créala en el diccionario y asígnale su 1 inicial.
Al imprimir, el Científico de Datos en Jefe espera ver la radiografía numérica exacta del string.
(Un regalo arquitectónico de los creadores de Python: Un String (texto) se comporta exactamente igual que una Lista por debajo del capó. Esto significa que puedes hacer tranquilamente un for letra in mensaje_encriptado: y la máquina desarmará la palabra letra por letra de forma automática).
"""
# Datos
mensaje_encriptado = "misterio"

# Crear un acumulador, para acumular la cantidad de veces que aparece una letra
contador_letra={}

# Vamos a ver si ya la letra existe, comparandola
for letra in mensaje_encriptado:
    if letra in contador_letra:
        contador_letra[letra]+=1
    else:
        contador_letra[letra]=1
print(contador_letra)

# Resultados
"""
1- Dificualtades:
- La verdad no mucha, fue un ejercio fácil
Resultado:
{'m': 1, 'i': 2, 's': 1, 't': 1, 'e': 1, 'r': 1, 'o': 1}
"""