"""
========================================================================
PROYECTO FINAL OMEGA: EL SISTEMA OPERATIVO DE DATOS (CRM Analytics)
========================================================================

CONTEXTO DE NEGOCIO (EL JEFE FINAL):
Acabas de ser contratado como el único Data Engineer de una empresa.
Te entregan dos sistemas rotos:
1. 'transacciones_crudas.csv': Un archivo sucio de ventas diarias.
2. 'clientes_base.json': La base de datos maestra con los ingresos 
   históricos y las deudas de los clientes corporativos.

TU MISIÓN ESTELAR (PORTAFOLIO):
Vas a construir una aplicación interactiva que se quede encendida 
en la terminal. El programa debe tener un Menú Principal.

MENÚ PRINCIPAL:
[1] Ejecutar Pipeline ETL (Limpiar CSV y Calcular Nuevas Ventas)
[2] Analizar Base de Datos y Buscar Mejor Cliente
[3] Salir del Sistema
"""

import json

# ==========================================
# ESCRIBE TU ARQUITECTURA AQUÍ ABAJO
# ==========================================
# Paso:1 Definir mi función
def analitica_crm(ruta_csv, ruta_json ):
    """
    la misión de esta función es entrgar un reporte análitico del CRM de la empres

    Args:
    ruta_json: Ruta relativa o absoluta de la base de datos de clientes
    ruta_csv: Ruta relativa o absoluta de las base de datos de transacciones de clientes

    Output:
    pass
    """
    # Paso 2: Construir el Menú del CRM
    ingresos_por_id = {} # Moviendo la caja AFUERA del bucle infinito para que sobreviva
    
    while True:
      try:
        print("\n" + "="*40)
        print("SISTEMA CRM ANALYTICS")
        print("="*40)
        print(f'[1] Ejecutar Pipeline ETL (Limpiar CSV)\n[2] Analizar Base de Datos y Buscar Mejor Cliente\n[3] Salir del Sistema')
        opcion_elegida= int(input('¿Qué opción elige: '))
        
        # Opción 1 ETL
        if opcion_elegida == 1:
          ids_procesados = set()
          with open(ruta_csv, "r") as archivo_csv:
            lineas = archivo_csv.readlines()
            
          for linea in lineas:
            if linea.startswith('id_transaccion'):
                continue
                
            lineas_limpias = linea.strip().split(",")
            id_transaccion = lineas_limpias[0].strip() # TX01
            cliente_id = lineas_limpias[1].strip()     # C001 (Limpiamos los espacios vacíos)
            
            # Lógica del SET para matar duplicados
            if id_transaccion in ids_procesados:
                continue
            ids_procesados.add(id_transaccion)
            
            try:
              valores_numericos = int(lineas_limpias[2])
            except Exception as y:
                print(f"¡ALERTA! Basura detectada y evadida: {y}")
                continue 
                
            # Lógica del Acumulador Matemático
            if cliente_id in ingresos_por_id:
                ingresos_por_id[cliente_id] += valores_numericos
            else:
                ingresos_por_id[cliente_id] = valores_numericos
                
          print(f"✅ ETL Completado. Ingresos extraídos: {ingresos_por_id}")

        # Opción 2 Análisis
        if opcion_elegida == 2:
           if not ingresos_por_id:
               print("⚠️ Debes correr la Opción 1 primero para extraer las ventas nuevas.")
               continue
               
           numero_maximo = -999999 # Empezamos muy abajo por si los netos son negativos
           nombre_cliente = ""
           
           with open(ruta_json, "r") as archivo_json:
              mi_diccionario = json.load(archivo_json)
              
           # Unir los ingresos historicos con los actuales
           for item in mi_diccionario:
              id_actual = item["id_cliente"]
              
              # Si el cliente generó ingresos nuevos hoy, los sacamos del diccionario del ETL. Si no, 0.
              ingreso_nuevo = ingresos_por_id.get(id_actual, 0) 
              
              ingreso_total = item['ingresos_historicos'] + ingreso_nuevo
              valor_neto = ingreso_total - item['deuda_pendiente']
              
              if valor_neto > numero_maximo:
                numero_maximo = valor_neto
                nombre_cliente = item['nombre']
           
           print(f'🏆 El Rey de la Cartera es {nombre_cliente} con ${numero_maximo} de valor real.')
              
        if opcion_elegida == 3:
           print("Apagando sistema...")
           break

      except Exception as e:
          print(f'Error en el menú: {e}')   
          continue         
             
                         
          
            
    
                
        
              





# Rutas de archivos
ruta_archivo_json= r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_FINAL_El_Sistema_Operativo\clientes_base.json"
ruta_archivo_csv= r"C:\Roadmap_data_Scientist\09_Mini_Proyectos\Proyecto_FINAL_El_Sistema_Operativo\transacciones_crudas.csv"

analitica_crm(ruta_archivo_csv, ruta_archivo_json )
