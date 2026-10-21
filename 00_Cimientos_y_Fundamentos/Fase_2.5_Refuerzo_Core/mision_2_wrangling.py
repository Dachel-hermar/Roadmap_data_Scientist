"""
El Contexto de Negocio: El equipo de ventas exportó un reporte de ganancias desde un viejo servidor de MS-DOS. 
El documento es un desastre. Cada línea contiene basura estática, márgenes en blanco innecesarios, saltos ocultos 
y un delimitador nefasto (|||). 

Para empeorar todo, por un bug en el servidor, el nombre de todos los clientes viene infectado con un código 
técnico de 7 caracteres pegado al inicio (Ej: "TX-999_").

Tu Arquitectura de Limpieza Quirúrgica:

La Partición Global: Hazle un .strip() a toda la variable data_cruda para matar los saltos de línea y espacios del principio 
y el final de toda la masa de texto. Luego, encadénale un .split("\n") para romper ese párrafo en una Lista estricta, 
donde cada elemento sea una fila independiente.

El Bucle Destripador: Crea un for para iterar esa nueva lista. 

Adentro, usa tu nuevo poder de Unpacking (Desempaquetado) combinado con un .split(). 
Divide la fila usando el delimitador feo y asígnalo al vuelo: empresa, monto, estado = fila.split("|||").

La Cirugía Fina (El Slicing):
Aplícale un .strip() individual a tus tres nuevas variables para matar los espacios blancos laterales que quedaron pegados.
¡Aplica el Rebanado Espacial (Slicing)! Como la variable empresa siempre está infectada por 7 caracteres basura 
(ej. TX-999_Corp_Gamer), usa la sintaxis matemática de Slicing de corchetes [7:] para decapitar el string 
y guardar desde la posición 7 hasta el final (quedándote solo con el nombre real).
Casteo Estructural: Convierte la variable del monto a Entero (int).
Reporte Final: Imprime cada fila limpia y estética: "✅ Empresa: [nombre_real] | Monto: $[monto] | Estado: [estado]".
"""

# Pega esta masa de texto dañado directamente en tu script
data_cruda = """
   TX-999_Corp_Gamer||| 5000|||Aprobado   
TX-888_Tech_Global   |||8500|||  Pendiente
   TX-777_Zeta_Ind|||    1200|||Rechazado
"""
# vamos a visualizar bien los datos antes de realizar cualquier limpieza
print(f'Crudos: {[data_cruda]}')
# Ahora vamos a usar el strip()
data_sin_espacio = data_cruda.strip()
print(f"Limpia: [{data_sin_espacio}]") #-> Ya podemos ver que los espacios se limpiaron, del principio y final
# Separar el parrafo en listas estrictas
filas= data_sin_espacio.split('\n')
print(f'{filas}')

# Desempacar
for fila in filas:
   company, monto , estado= fila.split("|||")
   # Aquí la desinfección se vuelve permanente en la memoria:
   company = company.strip()
   monto = monto.strip()
   estado = estado.strip()
   # Y AHORA SÍ, ya que la variable está limpia de verdad, le cortas la cabeza:
   company_name_clean = company[7:]
    # Covirtiendo monto a un numero entero
   monto_convertido=int(monto)
   print(f"✅ Empresa: {company_name_clean} | Monto: ${monto_convertido} | Estado: {estado}")


   
