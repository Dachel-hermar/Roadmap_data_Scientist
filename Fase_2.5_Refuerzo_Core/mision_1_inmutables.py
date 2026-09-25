"""
El Contexto de Negocio: El sistema de ciberseguridad detectó miles de intentos de inicio de sesión. 
Tienes una lista con datos que vienen en pares (Dirección IP y Usuario). 
El problema es que el sistema repite los registros múltiples veces y necesitamos limpiarlo de inmediato.
Tu Arquitectura a implementar:

El Poder del Set: Transforma esa lista llena de Tuplas directamente en un set. Los sets odian a los clones, 
así que vaporizará a los duplicados en microsegundos. Una vez limpio, conviértelo de nuevo en una lista 
(A este truco en la industria le llamamos el Casting list(set(data))).

El Unpacking de Tuplas (Desempaquetado): 
En la Fase 2, tú escribías ip = registro[0] y usuario = registro[1]. Eso es código Junior. 
Los desarrolladores Senior extraen las tuplas directamente en la declaración del bucle. 
(Pista arquitectónica: for ip, usuario in lista_limpia:).
Imprime de forma estética: "🚨 Alerta: El usuario [usuario] intentó entrar desde la IP [ip]".
"""
# Pega esta data cruda en tu archivo
registros_crudos = [
    ("192.168.1.1", "carlos_admin"),
    ("10.0.0.5", "sofia_ventas"),
    ("192.168.1.1", "carlos_admin"), # Duplicado por error de sistema
    ("192.168.1.1", "carlos_admin"), # Duplicado masivo
    ("172.16.0.2", "hacker_ruso"),
    ("10.0.0.5", "sofia_ventas")     # Duplicado
]
# Transformando la lista de tuplas en un set para eliminar duplicados
registros_limpios = list(set(registros_crudos))
print(registros_limpios)
print("Registros limpios (sin duplicados):")
for ip, usuario in registros_limpios:
    print(f"🚨 Alerta: El usuario {usuario} intentó entrar desde la IP {ip}")