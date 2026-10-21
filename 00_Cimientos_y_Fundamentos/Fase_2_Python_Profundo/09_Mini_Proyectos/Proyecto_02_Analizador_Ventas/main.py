"""
========================================================================
MINI-PROYECTO 2: EL ANALIZADOR FINANCIERO (Integración Total)
========================================================================

CONTEXTO DE NEGOCIO:
El gerente comercial te acaba de enviar el corte de caja del día en un archivo 
físico llamado 'ventas_diarias.txt'. Este archivo tiene estructura separada por comas 
(lo que en la industria se conoce como un archivo CSV ligero).
El formato de cada línea es exactamente este:
fecha,producto,correo_del_cliente,precio

El gerente necesita dos cosas urgentes para su junta directiva en 15 minutos:
1. Saber exactamente cuánto dinero en total facturó la empresa hoy (Sumar los precios).
2. Extraer un documento de texto nuevo con la lista de correos de los clientes que 
   compraron hoy, PERO SIN DUPLICADOS, para enviarles una encuesta de satisfacción.
   (Si miras el archivo, verás que Carlos compró 3 cosas, pero solo queremos su correo una vez).

EL RETO Y LAS REGLAS:
Construye una función 'analizar_corte(ruta_entrada, ruta_salida)' que:
1. Defina un Set vacío (para los correos) y un acumulador numérico en 0 (para el dinero).
2. Abra el archivo de ventas en modo lectura ("r").
3. Lea las líneas y, usando un bucle 'for', analice cada venta individual.
   TRAMPA MORTAL: La línea 1 es el encabezado del archivo (las palabras "fecha,producto...").
   Si intentas convertir la palabra "precio" a un número `int`, el programa explotará. 
   ¿Cómo evadirlo? Puedes usar un escudo `try/except`, o usar un `if "precio" in linea: continue`.
4. En cada vuelta del bucle, usa `.split(",")` para partir la línea en 4 pedazos. 
   Identifica en qué índice numérico (0, 1, 2, 3) está el correo y en cuál está el precio.
5. Suma el precio (convirtiéndolo a número) a tu acumulador.
6. Agrega el correo a tu Set matemático.
7. Al terminar el bucle, abre tu archivo de salida en modo escritura ("w") y vacía tu Set ahí.
8. La función debe retornar (return) una Tupla financiera con: 
   (Dinero_Total_Recaudado, Cantidad_de_Clientes_Unicos).
"""

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def analizar_corte(ruta_entrada, ruta_salida):
    """
      Lee un archivo de texto con las ventas diarias, purifica la data (elimina duplicados, 
      espacios vacíos y mayúsculas) usando un Set, y escribe los resultados en un nuevo archivo.
            
       Args:
          ruta_entrada (str): Ruta absoluta o relativa del archivo crudo a leer.
          ruta_salida (str): Ruta absoluta o relativa donde se guardará el archivo limpio.
                
       Returns:
             tuple: (total_facturacion, lista_correos)
        """

    with open(ruta_entrada,"r") as file:
      lineas= file.readlines()
      print(lineas)

      # Como me escupe una lista de datos voy a recorrer la lista con un bucle for
      correos_unicos = set()
      dinero_total = 0
      for linea in lineas:
            listado_limpio = linea.strip().split(",")
            if "precio" in listado_limpio:
                  continue
            correos_unicos.add(listado_limpio[2])
            precio= int(listado_limpio[3]) 
            dinero_total += precio
    with open(ruta_salida, "w") as f:
          for correo in correos_unicos:
              f.write(f"{correo}\n")
    return (dinero_total, len(correos_unicos))

                
    
        
        

      
         
      




# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
# Recuerda usar Rutas Absolutas con la "r" mágica de Windows.
ruta_crudos = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_02_Analizador_Ventas\ventas_diarias.txt"
ruta_limpios = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_02_Analizador_Ventas\total_facturado.txt"

# 1. Llama a tu función.

# 2. Atrapa la tupla en una variable.
dinero, correos = analizar_corte(ruta_crudos, ruta_limpios)
# 3. Imprime un reporte diciendo: "Hoy facturamos $____ de ____ clientes únicos."
print(f'"Hoy facturamos ${dinero} de {correos} clientes únicos."')
