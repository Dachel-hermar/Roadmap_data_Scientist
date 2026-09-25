"""
Bootcamp Ejercicio 9/10: La Trilogía del Caos - Parte 2 (El Data Pipeline)

REGLAS MILITARES:
1. Todo encapsulado en una Función (def).
2. Tienes un solo "Permiso Especial" de Teoría Nueva (ver la pista del split).
"""

# REQUERIMIENTO DE NEGOCIO (PROYECTO DE DATA CLEANING):
# Eres un Data Engineer. Un servidor viejo te entregó un listado de clientes registrados.
# Como es normal en el mundo real, los datos están asquerosamente sucios. Hay espacios en blanco 
# extra, mayúsculas mezcladas, separadores y errores de red en medio de los datos.
#
# Construye una función 'limpiar_datos' que reciba esa lista de registros crudos.
# 1. Crea un diccionario vacío llamado 'usuarios_validos'.
# 2. Recorre la lista de registros crudos con un bucle 'for'.
# 3. Aplica limpieza de datos (Data Cleaning) a CADA registro paso a paso:
#    - Usa try/except. Si algo explota limpiando el texto, el 'except' debe usar 'continue' para ignorar esa fila corrupta.
#    - PISTA NUEVA: Usa el método .split(":") para partir el texto en dos pedazos. 
#      Ejemplo: partes = registro.split(":") -> partes[0] será el nombre, partes[1] será la edad.
#    - Aplica todo lo que sabes al nombre (partes[0]): límpiale los espacios basura con .strip(), 
#      reemplaza los guiones bajos "_" por espacios normales " " usando .replace("_", " "), 
#      y ponlo bonito con .title().
#    - Convierte la edad (partes[1]) a número entero (int).
# 4. Filtro de negocio: Si la edad es MAYOR O IGUAL a 18, guárdalo en tu diccionario 'usuarios_validos' 
#    (Llave = nombre limpio, Valor = edad en número).
# 5. Devuelve (return) el diccionario limpio.

registros_crudos = [
    "  juan_perez:25  ", 
    " ana_lopez:17 ",      # Menor de edad, no debe entrar al dict
    "CARLOS_GOMEZ:40", 
    "error_fatal_red_502", # Fila corrupta, hará explotar al split(). El try/except debe interceptarlo.
    " maria_diaz:22 "
]

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def limpiar_datos(registros):
    usuarios_validos={}
    iteraciones = 0
    for registro in registros:
            iteraciones+=1
            try:
                #print(registro)
                # Para poder normalizar la lista de variables, es necesario proceder a una limpieza del mismo
                # Como cuando realizo el bucle para verficar los datos este me arroja una cadena por cada iteraccion, la cual
                # como podemos apreciar esta separada por : por lo cual procedemos a limpiar cada una de las cadenas, separandola
                # Por el caracter : así se me queda separada en la cantidad de partes que exista ese caracter
                parte=registro.split(":") #  Con esto separo la lista por el carácter :
                #print(f' En la iteración {iteraciones}, el tamo de la cadena es {len(parte)}') # esto me da el tamaño de la cadena, por cada iteración
                # Dado que la cadena se dividio como máximo en 2 vamos a ver como quedan esas separaciones y que son
                #print(f'Primera parte {parte[0]}')
                #print(f' Segunda parte {parte[1]}')

                # Hemos podido comprobar que en la iteración 5 hay un problema, ya que esta cadena se compone por un solo elemento, para ello usaremos un try\except para capturar el error
                # Ahora limpiaremos los espacios en blanco de los nombres, que son la parte del índice 0
                espacios_limpios= parte[0].strip() # Con esto limpio los espacios antes y despúes de la cadena
                # print(espacios_limpios) # Hemos podido comprobar que se limpiaron los espacios
                # Ahora pasarmos a remover los guiones bajos
                nombre_unificado = espacios_limpios.replace("_", " ") # Con esto logro remplazar los _undescore por tab
                # print(nombre_unificado)
                # Con todo esto hemos normalizado todos los valores de la parte 0 de la cadena o de la nueva cadena
                titulo= nombre_unificado.title()
                # Ahora pasaremos a la segunda Parte de la cadena
                # Como ya sabemos que valores la componen, y en su mayoría son valores que representan en este caso la edad
                # vamos a ver el tipo de los valores
                # print(type(parte[1]))
                # Hemos podido verificar que son de tipo str, por lo que para trabajar mejor con ello vamos a convertirlos en enteros
                edad = int(parte[1])
                #Comprobamos si ahora son enteros
                # print(type(edad)) # Efectivamente son enteros

                # Una vez normalizados todos los valores, pasamos a crear nuestro diccionario, cumpliendo con los filtros del negocio
                if edad >=18:
                     usuarios_validos[titulo]=edad
                
            except Exception as e:
                 print(f"Se ha encontrado un error {e}")
                 continue

    return usuarios_validos

# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Llama a tu función aquí pasándole la lista registros_crudos.
usuarios= limpiar_datos(registros_crudos)
# Imprime el resultado. Debería ser exactamente: 
# {'Juan Perez': 25, 'Carlos Gomez': 40, 'Maria Diaz': 22}
print(usuarios)
# Si no lo guardaba en variables no se aplicaba el cambio