"""
RETO 4: La Bóveda Infranqueable (Encapsulamiento y Privacidad)

Contexto de Negocio:
Un banco suizo necesita crear una bóveda digital. El problema de los retos anteriores 
es que cualquier programador podía saltarse los métodos y alterar los atributos 
directamente escribiendo `objeto.saldo = 9999999` desde afuera.
Tu objetivo es usar el "Doble Guion Bajo" (__) para volver invisible el dinero.

Tu Misión:
1. La Entidad: Crea la clase `BovedaSecreta`.
2. El Estado Privado (__init__): El constructor exigirá `password_configurado` y `dinero_inicial`.
   - Guarda el password normal: `self.password = password_configurado`.
   - ¡VUELVE PRIVADO EL DINERO!: Guárdalo usando doble guion bajo al inicio: `self.__dinero = dinero_inicial`.
3. El Comportamiento (Getter): Como el dinero es invisible desde afuera, crea un método 
   llamado `ver_dinero(self, intento_password)`.
   - Si el `intento_password` coincide con `self.password`, imprime o retorna el `self.__dinero`.
   - Si no coincide, imprime "❌ Acceso Denegado. Alarma activada."
4. Las Pruebas (Fábrica):
   - Instancia la bóveda con el password "Suiza123" y $50000.
   - Prueba A (Ataque Hacker): Intenta imprimir `boveda.__dinero` desde afuera. ¡Debería darte un error brutal (AttributeError)! Comenta esa línea después de probarla.
   - Prueba B (Fallo): Llama a `boveda.ver_dinero("hacker")`. (Debe rechazar).
   - Prueba C (Éxito): Llama a `boveda.ver_dinero("Suiza123")`. (Debe mostrar el dinero).
"""

# ==========================================
# 1. EL MOLDE (La Entidad Blindada)
# ==========================================
# Escribe tu clase aquí abajo...
class BovedaSecreta:
    """
    Clase que guarda la información de la clave y el dinero de la boveda
    """
    def __init__(self, password_configurado, dinero_inicial):
        """
        funcion que define el Estado privado de la boveda
        Args:
        self: espejo, inyecta el objeto de paramentro en memoria
        password_configurado: Contraseña única
        dinero_inicial: dinero total que se encuentra dentro de la boveda al incio
        """
        self.password=password_configurado
        self.__dinero= dinero_inicial # el método.__ vuelve una variable invisible desde afuera de la caja

    def ver_dinero(self, intento_password):
        """
        Función o metodo que nos permite ver el dinero desde fuera de la caja

        Args:
        intento_password: Contraseña aportada por el usuario por pantalla
        """
        if intento_password==self.password:
            return self.__dinero
        else:
            print(f"❌ Acceso Denegado. Alarma activada.")

    




# ==========================================
# 2. LA FÁBRICA (Pruebas de Hackeo)
# ==========================================
# Instancia y prueba tu clase aquí abajo...
usuario=BovedaSecreta("Suiza123",50000)
while True:
   
   try:
       contrasena= input(f"ingresa una contraseña:  ")
       if isinstance(contrasena,str):
           usuario.ver_dinero(contrasena)
           
   except Exception as e:
       print(f'Error detectado {e}')
       continue

   
#print(usuario.__dinero) # Si trato de acceder al objeto directamente, no puedo ya que python me arroja un error AttributeError, diciendome que el objeto no tiene atributo que le estoy pidiendo, dandome la pista que debo de llaamr al metodo ver_dinero



