"""
💻 Reto 4/10: Interés Compuesto (Sector Casino/Banca)

El Contexto: Un cliente entra con un capital inicial de 10 euros a un algoritmo de trading de alto riesgo. 
Si la operación "Gana", dobla su capital actual. Si "Pierde", el capital se reduce a la mitad. 
Tus Datos: capital = 10 operaciones = ["Gana", "Pierde", "Gana", "Gana"]

Tu Tarea: Recorre la lista de operaciones. Modifica dinámicamente el capital multiplicándolo por 2 o dividiéndolo entre 2, 
dependiendo de la palabra que encuentres. Al final del bucle, imprime: "El cliente se retira con [X] euros". 

"""

# Mis datos 
capital = 10 # Capital incial
operaciones = ["Gana", "Pierde", "Gana", "Gana"] # Cantidad de operaciones
capital_final = 0

# bucle for
for item in operaciones:
    if item == "Gana":
        capital *= 2
        capital_final = capital
    else:
        capital /= 2
        capital_final = capital
print(f'"El cliente se retira con {capital_final} euros"')