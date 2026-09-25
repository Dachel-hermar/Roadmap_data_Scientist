"""
👑 Reto 10/10: La Auditoría JSON (El Jefe Final)
Llegamos a la cima de la montaña. 
Vamos a mezclar todo: 
1- el Formato Universal JSON, 
2- bucles, 
3- inyección de Listas, 
4- extracción de Diccionarios y 
5- el Operador Lógico and.

El Contexto: Eres el Ingeniero de Datos del equipo de Riesgos de un banco internacional. 
Te piden generar una auditoría de urgencia. Necesitas extraer los nombres de los clientes que están "en números rojos" (tienen saldo negativo), 
pero solo si su cuenta sigue activa. (Los que tienen cuentas inactivas ya están judicializados por los abogados y no nos importan en este reporte). 

Tus Datos Crudos (Formato JSON):

python


clientes_banco = [
    {"nombre": "Ana", "saldo": 500, "cuenta_activa": True},
    {"nombre": "Luis", "saldo": -50, "cuenta_activa": True},
    {"nombre": "Juan", "saldo": -200, "cuenta_activa": False},
    {"nombre": "Marta", "saldo": -10, "cuenta_activa": True}
]

Tu Tarea Lógica (El Rompecabezas Final):

Crea tu lista de reporte limpia morosos = [].

Inicia tu clásico bucle for para desempacar esta lista masiva. 
(Recuerda: En cada vuelta, tu variable iteradora tomará la forma de un diccionario entero).

La Condición Doble: Usa el operador and. Necesitas que la máquina compruebe dos cosas simultáneamente: 
Que el "saldo" de la vuelta actual sea estrictamente menor a 0, Y que la "cuenta_activa" sea igual a True. 
(Ve directo a la yugular de los datos usando el método .get() que dominaste o el clásico acceso por corchetes).

Si el diccionario cumple con ambas alertas de riesgo, inyecta solamente su nombre en tu lista limpia usando .append().
Imprime el reporte oficial de morosos al finalizar la auditoría.
"""
# Datos:
clientes_banco = [
    {"nombre": "Ana", "saldo": 500, "cuenta_activa": True},
    {"nombre": "Luis", "saldo": -50, "cuenta_activa": True},
    {"nombre": "Juan", "saldo": -200, "cuenta_activa": True},
    {"nombre": "Marta", "saldo": -10, "cuenta_activa": True}
]

# Crear una lista donde almacenar los nombres de los clientes
lista_morosos=[] # Las listas siempre van en corchetes

# Pasos
"""
    el bucle for al formato la lista de clientes en el formato JSON
    Nos da un diccionario con la información de los clinetes
    Como solo, nos interesan los que tienen la cuenta activa, vamos a crear 2 condiciones
    La primera que nos diga si su saldo es negativo 
    La segunda si la cuenta esta activa
    Todo ello en una misma linea ya que de cumplirse ambas condiciones debo de agreagr estos a la lista vacía creada
"""

# Iniciamos un bucle para recorrer la lista dada en formato JSON
for lista in clientes_banco:
    print(lista) # Imprimimos la lista para ver que es lo que nos da
    # Ahora vamos a crear las condicionales
    if lista.get("saldo")< 0 and lista.get("cuenta_activa")==True:
        lista_morosos.append(lista.get("nombre"))
print(f'Las personas morosas son: {lista_morosos}')
