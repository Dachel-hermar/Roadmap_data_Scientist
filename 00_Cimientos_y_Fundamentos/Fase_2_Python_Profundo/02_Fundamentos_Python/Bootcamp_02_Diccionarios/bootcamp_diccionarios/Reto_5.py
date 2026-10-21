"""
💻 Reto 5/10: La Gran Fusión Bancaria (Sector Finanzas)
El Contexto de Negocio: Eres el Data Engineer de un banco de élite.
 Tu banco acaba de comprar y absorber a un banco regional más pequeño. 
 Tu misión crítica es migrar los datos financieros. 
 Tienes que diseñar el algoritmo que fusione y consolide las bases de datos de clientes en un solo gran registro maestro. 
 
 Regla de Negocio: Si un cliente ya tenía una cuenta abierta en ambas sucursales, su dinero debe sumarse para que no pierda saldo. Si el cliente solo existía en una de las dos sucursales, su cuenta simplemente debe registrarse tal cual en el nuevo sistema.

Tus Datos Crudos:

python


sucursal_norte = {"Juan": 500, "Maria": 1200, "Pedro": 300}
sucursal_sur = {"Ana": 400, "Juan": 200, "Pedro": 100, "Luis": 800}
El Objetivo Final (Lo que espera tu Jefe): Al final de la ejecución de tu script, 
el sistema debe imprimir una nueva estructura de datos (por ejemplo, banco_unificado) 
que luzca matemáticamente exacta a esto: {"Juan": 700, "Maria": 1200, "Pedro": 400, "Ana": 400, "Luis": 800}

(Mi única y última pista: Roma no se construyó en un solo día... ni con un solo bucle).
"""
# Datos de clientes
sucursal_norte = {"Juan": 500, "Maria": 1200, "Pedro": 300}
sucursal_sur = {"Ana": 400, "Juan": 200, "Pedro": 100, "Luis": 800}

"""
Objetivo:
1-Unificar las bases de datos, en una sola
2- Siya existe el cliente, sumar el saldo
3- Imprimir la nueva base de datos al finalizar
"""
# Pseudocódigo y lógica de negocio
"""
1-Creación de la variable que va a funcionar como BBDD
Para crear una únoca base de datos consolidada, necesitamos, primero crear un diccionario clave-valor, donde este tendrá
como clave el nombre del cliente y valor el saldo del cliente para ello vamos a nombrar ese nuevo diccionario como banco_unificado={}
**IMPORTANTE**~ El diccionario va a inicializarse vacío
2-Lectura de mis bases de datos
Para saber los datos que tengo primero debo de recorrer las distintas bases de datos para extraer sus datos, propiamente dicho
Ahora como el objetivo no es duplicar, si no unificar, para ello puedo hacerlo con bucles anidados, ya que recorrería el primer diccionario
extraería su valor y despúes recorrería el segundo, ya una vez tenga ambas claves las compararía si una se encuentra dentro de otra entonces sumo, sus valores y la agrego al diccionario nuevo

3- Finalemente imprimo por pantalla el mismo
"""
# inicializo la variable
banco_unificado={}

# Bucle for
for nombre_norte, values_norte in sucursal_norte.items():
    banco_unificado[nombre_norte]=values_norte
    

for nombre_sur, values_sur in sucursal_sur.items():
    if nombre_sur in banco_unificado:
        banco_unificado[nombre_sur]+= values_sur
    else:
        banco_unificado[nombre_sur]= values_sur
            
print(banco_unificado)
            
# Problemas encontrados
"""
1- Al principio creamos un bucle anidado, creyendo que sería más fácil ya que compararíamos si un valor existe dentro de ese otro diccionario
Resultados:
Que el bucle sumaba en repetidas ocasiones el mismo valor, danod una salida como la siguiente
{'Juan': 1100, 'Ana': 1200, 'Pedro': 400, 'Luis': 2400, 'Maria': 1200}
2- despúes manteniendo ese mismo bucle anidado fuimos a tratar de hacer que en ves de comprobar directamennte con el comparador in
si la llave se encontraba dentro del diccionario, tratamos de comparar las llaves directamente y si estas eran igual, sumar sus valores
lo que nos llevo a que solamente se imprimieran las llaves que eran iguales, y cunado creamos el bucle else para el resto, volvía a hacer lo del principio
Dando salidas como estas:
{'Juan': 700, 'Pedro': 400} ó estas {'Juan': 500, 'Luis': 800, 'Maria': 1200, 'Pedro': 300}

Resultados:
Separar los bucles y comparar con bucles separados

Tareas a estudiar, caundo anidar y cuando no anidar bucles, por el momento, 
"""