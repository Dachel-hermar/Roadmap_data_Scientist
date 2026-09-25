"""
RETO 3 del 3x3: El Motor Analítico (Atributos de Estructuras Complejas)

Contexto de Negocio:
Encapsular la lógica financiera de un departamento dentro de un Objeto inteligente 
que utilice Listas en su memoria interna, sentando las bases para entender Pandas.

Tu Misión:
1. La Entidad: Define la clase `MotorFinanciero`.
2. El Estado (__init__): Debe recibir solo el `nombre_departamento`.
   - Guarda el nombre en `self.nombre`.
   - Inicializa una lista vacía para las finanzas: `self.registros = []`.
3. Comportamiento 1 (`registrar_ingreso`): Recibe un `monto`.
   - Agrégalo a la lista privada del objeto usando `append()`.
4. Comportamiento 2 (`imprimir_totales`): No recibe parámetros extras.
   - Usa la función `sum()` sobre `self.registros` e imprime el gran total acumulado.
5. Las Pruebas (Fábrica):
   - Instancia el motor para "Neurología".
   - Regístrale 3 ingresos (Llama 3 veces a `registrar_ingreso`).
   - Llama a `imprimir_totales()`.
"""

# ==========================================
# 1. EL MOLDE (La Entidad Analítica)
# ==========================================
# Escribe tu clase aquí abajo...
class MotorFinanciero:
    """
    Clase que define el comportamiento de las finanzas de los distintos departamentos del Hospital
    """
    def __init__(self, nombre_departamento):
        """
        Función de Estado esperado del comportamiento a la hora de instanciar la clase
        Args:
        self-> El espejo, metodo para inyectar en memoria los parametros dados
        nombre_departamento: Argumento dado se refiere al nombre del departamento
        """
        self.departamento= nombre_departamento
        self.finanzas=[]

    def registar_ingresos(self, monto):
        """
        Función encargada de registrar las finanzas de los departamentos

        Args:

        monto: monto ingresado por el departamento
        """
        self.finanzas.append(monto)

    def imprimir_totales(self):
        """
        Función encargada de el total de las finanzas departamentales
        """
        total= sum(self.finanzas)
        print(f"las finanzas totales del departamento {self.departamento} son de {total}")





# ==========================================
# 2. LA FÁBRICA (Pruebas del Motor)
# ==========================================
# Instancia y prueba tu clase aquí abajo...
neurología= MotorFinanciero("Neurología")
neurología.registar_ingresos(500)
neurología.registar_ingresos(890)
neurología.registar_ingresos(-1000)
neurología.imprimir_totales()

cardiologia= MotorFinanciero("Cardiología")

cardiologia.registar_ingresos(400)
cardiologia.registar_ingresos(500)
cardiologia.imprimir_totales()

print(f'{neurología.finanzas.append(90)}')
print(neurología.finanzas)
