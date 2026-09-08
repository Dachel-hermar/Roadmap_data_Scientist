"""
💻 Reto 7/10: Filtro de Contraseñas (Sector Ciberseguridad)

El Contexto: Eres el analista de seguridad de una base de datos de usuarios. 
Por normativa legal, una contraseña es "Segura" solo si tiene 8 o más caracteres. 
Tus Datos: contrasenas = ["12345", "admin1234", "qwerty", "super_secreta_99"]

Tu Tarea: Escribe el código que cuente cuántas contraseñas Seguras hay, y cuántas Inseguras (vas a necesitar dos contadores diferentes iniciados en 0). 
Al final del bucle, imprime ambos resultados. (Pista Hacker de Sintaxis: Al igual que len(lista) te da la cantidad de posiciones en una caja, len(texto) te da la cantidad de letras que tiene una palabra. 
Por ejemplo: len("hola") devuelve un 4 numérico).
"""
# Listado de contraseñas
contrasenas = ["12345", "admin1234", "qwerty", "super_secreta_99"]

# variables de contraseñas Válidas e Inválidas
contrasenas_validas=0
contrasenas_invalidas= 0

# Para que una contraseña se válida debe de tener 8 o más carácteres
for item in range(len(contrasenas)):
    if len(contrasenas[item]) < 8:
        contrasenas_invalidas += 1
        
    else:
        contrasenas_validas +=1
# Imprimir la cantidad de contraseñas validas e invalidas encontradas
print(f'Existe una cantidad de\n Contraseñas Invalidas: {contrasenas_invalidas}\n Contraseñas Validas: {contrasenas_validas}')