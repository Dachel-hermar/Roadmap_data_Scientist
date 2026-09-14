"""
========================================================================
MINI-PROYECTO 3: EL ARQUITECTO DE DATOS (CRUD + JSON)
========================================================================

CONTEXTO DE NEGOCIO:
Eres el Data Engineer de una tienda de tecnología. Tienes una base de datos 
física en formato JSON ('base_datos.json') que guarda el inventario de la tienda.

Hoy te informan de tres eventos corporativos que acaban de ocurrir:
1. Llegó mercancía nueva: Hay que sumarle 3 unidades al stock del "TECLADO-003".
2. Hubo un error de captura: El "MONITOR-002" en realidad cuesta 300 USD (no 350).
3. Lanzamiento de nuevo producto: Hay que dar de alta un producto completamente 
   nuevo en el sistema:
   ID: "MOUSE-004", Nombre: "Logitech MX Master", Stock: 10, Precio: 99

NUEVAS ARMAS TECNOLÓGICAS (LA TEORÍA):
Para leer o guardar diccionarios en un archivo físico, no podemos usar `.readlines()`
ni `.write()` como hacíamos con el texto puro. Los diccionarios tienen una arquitectura
compleja. Por eso, usamos la librería nativa `json`.

Para leer de un archivo JSON a la memoria RAM (Se convierte en un Diccionario de Python):
    import json
    with open("archivo.json", "r") as file:
        mi_diccionario = json.load(file)

Para escribir de la memoria RAM hacia el disco duro físico:
    with open("archivo.json", "w") as file:
        json.dump(mi_diccionario, file, indent=4) # indent=4 lo pone bonito

EL RETO:
Construye una función 'actualizar_inventario(ruta_json)' que:
1. Abra el archivo JSON en modo lectura ("r") y lo cargue en una variable (Diccionario).
2. [UPDATE] Actualice el stock del TECLADO-003 (sumando 3 al valor actual).
3. [UPDATE] Modifique el precio del MONITOR-002 a 300.
4. [CREATE] Inyecte un nuevo diccionario anidado para el "MOUSE-004".
5. Abra el MISMO archivo JSON en modo escritura ("w") y sobreescriba toda la 
   base de datos usando `json.dump()`.

¡Este es tu primer sistema con memoria persistente! No entres en pánico si 
son muchas líneas, atácalo paso a paso. Muestra la base de datos con un `print()`
antes de guardarla para que tu cerebro entienda qué estás mutando.
"""

import json

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
def actualizar_inventario(ruta_json):
    """
      Lee un archivo JSON con el inventario de la tienda, actualiza los datos según 
      los eventos corporativos y guarda los cambios en el mismo archivo.
            
       Args:
          ruta_json (str): Ruta absoluta o relativa del archivo JSON a leer y actualizar.
                
       Returns:
             None
        """
    # Ahora leeremos el archivo Json con .open
    with open(ruta_json, "r") as file:
        mi_diccionario = json.load(file)

    # [UPDATE]: Vas directo a la vena, sin bucles, sin condicionales if.
    mi_diccionario["TECLADO-003"]["stock"] += 3
    mi_diccionario["MONITOR-002"]["precio_usd"] = 300
    
    # [CREATE]: Para agregar un producto nuevo, simplemente declaras su llave y le asignas su valor.
    mi_diccionario["MOUSE-004"] = {
        "nombre": "Logitech MX Master", 
        "stock": 10, 
        "precio_usd": 99
    }
    
    # Ahora vamos a guardar el diccionario como un archivo (Nivel 1 de indentación)
    with open(ruta_json, "w") as file:
        json.dump(mi_diccionario, file, indent=4)  


# ==========================================
# ZONA DE PRUEBAS (QA)
# ==========================================
ruta_bd = r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_03_Gestor_Inventario\base_datos.json"

# Llama a tu función
actualizar_inventario(ruta_bd)
print("✅ Inventario actualizado con éxito. Revisa tu archivo base_datos.json")
