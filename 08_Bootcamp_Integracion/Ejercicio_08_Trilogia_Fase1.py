"""
Bootcamp Ejercicio 8/10: La Trilogía del Caos - Parte 1 (El Gestor de Gimnasio)

REGLAS MILITARES:
1. Cero teoría nueva.
2. CERO PISTAS. CERO ESTRUCTURAS PREARMADAS.
3. Debes combinar: while True, if/elif/else, mutación de Diccionarios (CRUD) y Control de Errores.
"""

# REQUERIMIENTO DE NEGOCIO (PROYECTO MASIVO FUNCIONAL):
# Eres el Arquitecto de Software de una cadena de Gimnasios 24/7.
# El recepcionista necesita un sistema de consola para gestionar a los socios (Clientes).
#
# Construye una función 'sistema_gimnasio()' que no reciba parámetros.
# 1. Tu base de datos inicial será un diccionario vacío: socios = {}
# 2. Inicia un Bucle Infinito interactivo (Cajero Automático) que le pida al usuario 
#    ingresar una opción numérica (1, 2, 3 o 4):
#
#    - Opción 1 (Inscribir): Pide el nombre del socio y su edad. Si es menor de 18, 
#      imprime "Rechazado: Menor de edad". Si tiene 18 o más, agrégalo a tu diccionario 
#      (Llave = nombre, Valor = "Activo").
#    - Opción 2 (Dar de Baja): Pide el nombre a eliminar. Si el nombre existe en el diccionario, 
#      bórralo (mutación) e imprime "Socio eliminado". Si no existe, imprime "El socio no existe".
#    - Opción 3 (Reporte): Imprime el diccionario completo para ver quién está inscrito.
#    - Opción 4 (Apagar): Imprime "Sistema cerrado" y rompe el bucle infinito.
#
# EL ESCUDO ANTIBALAS:
# Usa 'try/except' donde creas que la estupidez del recepcionista puede hacer explotar el sistema 
# (por ejemplo, si teclea "dos" en lugar de 2, o si pone "veinte" en la edad).
#
# ESTÁS COMPLETAMENTE SOLO EN ESTA. ARMA LA ARQUITECTURA.

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def sistema_gimnasio():
    socios={}
    while True:
        
        print("Seleccione la opción deseada\n Opción 1: (Inscribir)\n Opción 2 (Dar de Baja)\n Opción 3 (Reporte)\nOpción 4 (Apagar) ")
        try:
            
            opcion= int(input("¿Qué opción desea?: "))
            
            if opcion == 1:
                print("---Iniciando Proceso de Insacripción---")
                nombre= input("Por favor ingrese su nombre:  ").title()
                edad = int(input("Por favor ingrese su edad:  "))
                if edad < 18:
                    print("Rechazado: Menor de edad")
                else:
                    socios[nombre]=edad
            print(socios)
            print(f'\n')
                
            if opcion == 2:
                print("---Iniciando proceso de Eliminación---\n Por favor espere")
                nombre_eliminar= input("Por favor ingrese el nombre de la persona a darle de baja: ").title()
                if nombre_eliminar in socios:
                    socios.pop(nombre_eliminar)
                    print("Socio eliminado")
                else:
                    print("El socio no existe")
                print(f'\n')

            if opcion==3:
                print("---Iniciando proceso de lista de clientes----")
                print(f'La lista de clintes es la siguiente: {socios}')
            print(f'\n')

            if opcion == 4:
                print("---Iniciando proceso de cierra del sistema---")
                print("Sistema cerrado\n Hasta Pronto")
                break
                
        except Exception as e:
            print("A ocurrido un error intentelo de nuevo")
            continue
        

    

# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Ejecuta tu función aquí para encender el sistema
sistema_gimnasio()

# Anteriormente habia agragado mi bloque de salvavidas despues de crear el diccionario vacío, 
# Lo que sucedió fue que en cuanto me pidio el sistema la Opcion que quería no me di cuenta y escribi un nombre, lo que hizo que este fallara y se detuviera
# El error fue un ValueError, por lo que movi mi try al inicio de todo despues del while true
# problemas encontrados no se me guarda el diccionario
# Por lo que la opcion 2 y3 no se ejecutan correctamente
# Vale el tema es que el diccionario lo tenía como variable local, lo había puesto despues del try
# Y esta debe de actuar como variable global, antes de iniciar cualquier proceso debo de declararla antes, esto era lo que más tiempo me consumia
# ahora necesito que da igual si el cliente escribe el nombre con la primera en mayusculas, todo en minusculas o bien toto en mayusculas el sitema no lo detecte como error
# La duda viene ¿si debo de convertir desde un incio a lower o upper?