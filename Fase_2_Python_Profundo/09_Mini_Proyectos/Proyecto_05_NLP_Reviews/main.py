"""
========================================================================
MINI-PROYECTO 5: EL ANALISTA DE SENTIMIENTO (NLP Básico)
========================================================================

CONTEXTO DE NEGOCIO:
El departamento de Marketing te ha pasado un archivo de texto plano 
('reseñas.txt') con comentarios de clientes sobre el nuevo producto.

Quieren saber rápidamente cuáles son las palabras más repetidas por los 
clientes para descubrir si el "sentimiento" general es positivo ("excelente") 
o negativo ("malo").

Para hacer esto, vamos a crear el motor base de cualquier IA de 
Procesamiento de Lenguaje Natural (NLP): Un "Contador de Frecuencias".

LA TEORÍA (Contadores en Diccionarios):
Los diccionarios son perfectos para contar cosas. La llave es la palabra, 
y el valor es el contador de cuántas veces ha aparecido.

    frecuencias = {}
    palabra = "excelente"
    
    if palabra in frecuencias:
        frecuencias[palabra] += 1  # Si ya existe, súmale 1
    else:
        frecuencias[palabra] = 1   # Si no existe, créala con valor 1

EL RETO:
Construye una función 'analizar_reseñas(ruta_txt, ruta_json)' que:
1. Cree un diccionario vacío `contador_palabras = {}`.
2. Abra el archivo de texto en modo "r".
3. Lea el archivo línea por línea con un bucle `for`.
4. En cada línea, tienes que "Limpiar los datos":
   - Quita los saltos de línea y convierte todo a minúsculas (`.strip().lower()`)
   - Reemplaza las comas y los puntos por espacios en blanco (`.replace(",", "").replace(".", "")`)
   - Divide la oración en una lista de palabras usando `.split(" ")`
5. Ahora que tienes una lista de palabras limpias, usa UN SEGUNDO BUCLE FOR 
   (un bucle anidado) para recorrer esa lista palabra por palabra.
6. Aplica la lógica del Contador de Diccionarios a cada palabra.
7. Al terminar TODO, abre el archivo JSON de salida en modo "w" y guarda tu 
   diccionario de frecuencias usando `json.dump()`.

¡Aplica ingeniería inversa a los textos!
"""

import json

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def analizar_reseñas(ruta_txt, ruta_json):
    contador_palabras = {}
    with open(ruta_txt, "r") as file:
        lineas= file.readlines()
        #print(lineas) # salida en forma de lista 
        # para limpiar los textos debo de recorrer la list
        for linea in lineas:
            #print(linea)
            comentarios_limpios= linea.strip().lower() # Con esto limpiamos los espacios, y convertimos todo a minúsculas
            #print(comentarios_limpios)
            normalizacion= comentarios_limpios.replace(",", "").replace(".", "")
            #print(normalizacion)
            palabras= normalizacion.split(" ")
            #print(palabras)
            
            for palabra in palabras:
                #print(palabra)               
                if palabra in contador_palabras:
                  contador_palabras[palabra] += 1  # Si ya existe, súmale 1
                else:
                  contador_palabras[palabra] = 1   # Si no existe, créala con valor 
        
    with open(ruta_json,"w") as f:
       json.dump(contador_palabras,f,indent=4)    



# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
ruta_entrada = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_05_NLP_Reviews\reseñas.txt"
ruta_salida = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_05_NLP_Reviews\frecuencias.json"

# Llama a tu función
analizar_reseñas(ruta_entrada,ruta_salida)
