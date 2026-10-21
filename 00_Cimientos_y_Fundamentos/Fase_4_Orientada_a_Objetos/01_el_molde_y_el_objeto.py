class CientificoDatos:
    # 1. EL CONSTRUCTOR (Le inyectamos la memoria inicial a la caja fuerte)
    def __init__(self, nombre_ingresado, lenguaje_ingresado, etpa_aprendizaje):
        self.nombre = nombre_ingresado
        self.lenguaje = lenguaje_ingresado
        self.etapa= etpa_aprendizaje
        self.energia = 100  # Todos nacen con 100

    # 2. LAS HABILIDADES (Métodos). ¡Ojo! Siempre deben recibir "self" como primer parámetro para poder mirarse al espejo.
    def trabajar(self):
        # El objeto usa su espejo "self" para leer y mutar su propia memoria
        print(f"\n💻 [{self.nombre}] está escribiendo código en {self.lenguaje}...")
        self.energia = self.energia - 20
        print(f"🔋 Energía restante: {self.energia}%")
        print(f"Carlos es un programador: {self.etapa}")

    def tomar_cafe(self):
        print(f"\n☕ [{self.nombre}] se tomó un espresso doble.")
        self.energia = self.energia + 15
        print(f"🔋 Energía recuperada: {self.energia}%")

# ==========================================
# LA FÁBRICA Y LA SIMULACIÓN (Afuera de la clase)
# ==========================================

# 1. Instanciamos (fabricamos) el objeto
carlos = CientificoDatos("Carlos", "Python", 1)
dachel= CientificoDatos("Dachel", "Iniciando", "python")
print(f"--- Sistema: Nació {carlos.nombre} con {carlos.energia}% de energía ---")

# 2. El objeto interactúa con el mundo (Observa detenidamente los paréntesis)
carlos.trabajar()
carlos.trabajar()
carlos.tomar_cafe()
carlos.trabajar()

dachel.trabajar()
dachel.tomar_cafe()
dachel.trabajar()
print(f"\n📊 ESTADO FINAL -> Energía de Carlos: {carlos.energia}% | Energía de Dachel: {dachel.energia}%")