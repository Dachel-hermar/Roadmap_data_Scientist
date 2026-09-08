"""
💻 Reto 8/10: Alerta de Servidores (Sector Cloud / DevOps)
El Contexto: Monitoreas en vivo la temperatura del procesador (CPU) del servidor principal de un Banco. 
Si la temperatura alcanza los 90 grados o más en 3 ocasiones en total durante el día (no importa si no son seguidas), 
el servidor debe apagarse para no quemarse. Tus Datos: temperaturas_cpu = [80, 95, 85, 92, 75, 91, 70]

Tu Tarea: Recorre la lista de lecturas del día. Cuenta cuántas veces la temperatura es mayor o igual a 90. 
Dentro del bucle, haz un control de daños: En el milisegundo en que tu contador de alertas llegue a 3, 
imprime "APAGADO DE EMERGENCIA INICIADO" y destruye el bucle (con break) para salvar la máquina. 

(Bono de maestría: Si termina el día sin llegar a 3 alertas críticas, imprime "Servidor Estable" usando tu famosa técnica avanzada del For-Else).
"""

# Datos actuales 
temperaturas_cpu = [80, 95, 85, 92, 75, 91, 70]

# Creamos este contador para que nos diga cuantas veces se alcanzo la temperatura de 90 grados
temperaturas_altas= 0 # contador de temperaturas altas

# bucle for para recorrer la lista de temperaturas
for temp in temperaturas_cpu:
    if temp >=90:
        temperaturas_altas +=1
        if temperaturas_altas == 3:
            print("APAGADO DE EMERGENCIA INICIADO")
            break
        
      
else:
    print("Servidor Estable")

