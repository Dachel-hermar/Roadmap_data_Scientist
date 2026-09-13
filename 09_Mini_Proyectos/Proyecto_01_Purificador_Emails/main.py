"""
========================================================================
MINI-PROYECTO 1: EL PURIFICADOR DE DATOS (File Handling, Sets y Tuplas)
Etiqueta: [NIVEL PORTAFOLIO] 🏆
========================================================================

CONTEXTO DE NEGOCIO:
El departamento de Marketing exportó la lista de correos de los clientes registrados. 
Pero el sistema heredado falló y el archivo ('datos_crudos.txt') es un absoluto desastre: 
tiene correos duplicados, espacios en blanco, mayúsculas mezcladas, líneas vacías 
y basura que no son correos.

Tu Misión: Crear un script que lea ese archivo físico desde el disco duro, purifique 
los datos en la memoria RAM, extermine los duplicados matemáticamente, y guarde los 
correos limpios en un archivo de texto totalmente nuevo.

NUEVAS ARMAS TECNOLÓGICAS (LA TEORÍA):

1. Archivos (File Handling): 
   Para leer o escribir un archivo físico usamos el bloque 'with open'. Esto es un escudo 
   de seguridad que abre el archivo y lo cierra automáticamente al terminar, evitando fugas de memoria.
   Ejemplo de LECTURA (modo "r" de read): 
       with open("archivo.txt", "r") as archivo:
           lineas = archivo.readlines() # Esto te devuelve una Lista con todas las líneas
           
   Ejemplo de ESCRITURA (modo "w" de write):
       with open("nuevo.txt", "w") as archivo:
           archivo.write("texto\n") # \n significa salto de línea (Enter)

2. Sets (Conjuntos):
   Una Lista [] permite datos repetidos. Un Set {} es un concepto matemático que NO permite 
   duplicados. Si le inyectas datos repetidos, los aniquila instantáneamente.
   Se inicializa así: correos_unicos = set()
   Se le agregan datos así: correos_unicos.add("juan@gmail.com")

3. Tuplas (Tuples):
   Son primas hermanas de las listas, pero van entre paréntesis () y son INMUTABLES. 
   Una vez creadas, nadie puede hacerles un .append() ni alterarlas. 
   Se usan muchísimo en Data Science para que una función devuelva múltiples variables a la vez.
   Ejemplo: return (total_procesados, total_limpios)

EL RETO:
Construye una función 'purificar_correos(ruta_entrada, ruta_salida)' que:
1. Cree un Set vacío para guardar los correos blindados contra duplicados.
2. Abra y lea todas las líneas de 'ruta_entrada' en modo lectura ("r").
3. Recorra esas líneas con un 'for'. Si la línea está vacía o no tiene el símbolo "@", ignórala.
4. Limpie la línea (quítale los espacios basura y conviértela toda a minúsculas con .lower()).
5. Agrega el correo limpio a tu Set.
6. Abre el archivo 'ruta_salida' en modo escritura ("w") y mediante un 'for' escribe cada correo 
   del Set dentro del nuevo archivo (agrégale un "\n" al final de cada uno para que no queden pegados).
7. La función debe retornar (return) una Tupla con dos números: 
   (Cantidad original de líneas leídas, Cantidad final de correos guardados).
"""



# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================

def purificar_correos(ruta_entrada, ruta_salida):
    """
    Lee un archivo de texto con correos sucios, purifica la data (elimina duplicados, 
    espacios vacíos y mayúsculas) usando un Set, y escribe los resultados en un nuevo archivo.
    
    Args:
        ruta_entrada (str): Ruta absoluta o relativa del archivo crudo a leer.
        ruta_salida (str): Ruta absoluta o relativa donde se guardará el archivo limpio.
        
    Returns:
        tuple: (total_lineas_leidas, total_correos_unicos_guardados)
    """
    correos_blindados = set()
    with open(ruta_entrada, "r") as file:
        lineas = file.readlines()
        
        for linea in lineas:
            if "@" in linea:
                correo_limpio = linea.strip().lower()
                correos_blindados.add(correo_limpio)
            
    with open(ruta_salida, "w") as f:
        for correo in correos_blindados:
            f.write(f"{correo}\n")    

    return (len(lineas), len(correos_blindados))   
                
    


# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Aquí te dejo las rutas preparadas (funcionan porque los archivos están en la misma carpeta).
ruta_crudos = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_01_Purificador_Emails\datos_crudos.txt"
ruta_limpios = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_01_Purificador_Emails\correos_purificados.txt"

# 1. Llamamos a la función usando "Desempaquetado (Unpacking)" para atrapar los dos números de la Tupla.
leidos, limpios = purificar_correos(ruta_crudos, ruta_limpios)

# 2. Imprimimos el reporte estético de la capa de Interfaz de Usuario (UI).
print("=" * 40)
print(" REPORTE DE PURIFICACIÓN DE CORREOS")
print("=" * 40)
print(f"Líneas crudas analizadas:   {leidos}")
print(f"Correos únicos rescatados:  {limpios}")
print(f"Basura y duplicados elim.:  {leidos - limpios}")
print("=" * 40)
print(f"✅ Archivo guardado con éxito en: \n{ruta_limpios}")
