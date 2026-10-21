# 📓 Diario de Aprendizaje: Científico de Datos

Este es el espacio personal para forzar a mi cerebro a traducir el código a conceptos de negocio (Memoria a Largo Plazo). Como dice la Regla 7: "Si no lo puedes explicar con tus propias palabras, no lo has entendido".

---

## 📅 Sesión: Arquitectura Avanzada y Ecosistema Funcional (Fase 4 Completada)

### 💡 Conceptos Clave de Programación Orientada a Objetos (OOP):

**1. El Encapsulamiento y el Estado (`__init__` y `self`)**
*La diferencia entre una función y un objeto es la memoria. Las funciones (Stateless) olvidan todo apenas terminan de procesar. Las Clases (Stateful) crean objetos en la RAM que actúan como "habitaciones privadas". El `__init__` construye la habitación inyectando variables base, y la palabra mágica `self` es la llave magnética que asegura que los métodos solo alteren la información de ESA habitación específica, sin tocar la del vecino.*

**2. La Privacidad Absoluta (El Doble Guion Bajo `__`)**
*Por defecto, Python crea variables públicas. Si un desarrollador junior usa notación de punto (`objeto.saldo = -5000`), puede destruir la contabilidad de la empresa saltándose nuestras validaciones. Para blindar el objeto, usamos el doble guion bajo (`self.__saldo`). Esto "invisibiliza" la variable desde el exterior, obligando al usuario a interactuar con ella EXCLUSIVAMENTE a través de métodos oficiales (Getters y Setters) que contienen reglas de negocio (`if/else`).*

**3. La Genética Corporativa (Herencia y `super()`)**
*Para no violar el principio DRY (Don't Repeat Yourself), creamos una Superclase Madre con la lógica repetitiva (ej. `__init__` con `nombre` y `salario`). Las Clases Hijas (`class Programador(Empleado)`) heredan ese ADN. Para inyectar los datos a la Madre, usamos `super().__init__(nombre, salario)`, liberando a la Hija para que solo se concentre en sus propios atributos especiales.*

**4. El Escuadrón Polimórfico**
*El Polimorfismo es tener métodos con el EXACTO MISMO NOMBRE en diferentes clases, pero que hacen cosas totalmente distintas por dentro. Su poder es Macro: permite meter objetos de distintas clases en una misma Lista, hacer un bucle `for`, y mandar a llamar al método sin usar un solo `if`, ya que Python reconoce inteligentemente el ADN de cada objeto y ejecuta su versión correcta.*

**5. La Magia Dunder (`__str__` y `__len__`)**
*Cuando haces un `print(objeto)` y Python te escupe basura de memoria (`<__main__.Clase at 0x...`), es porque no sabe cómo traducir tu caja. Si sobrescribes el método doble-underscore `__str__(self)`, tú decides cuál será el "rostro" de tu objeto. Lo mismo ocurre con `__len__(self)` para interceptar comandos matemáticos de conteo.*

**6. Los Intercomunicadores (Decoradores de Clase)**
*- **`@staticmethod`**: Una función utilitaria que vive pegada al muro de la fábrica por mero orden, no necesita un `self` porque no altera a ningún auto.*
*- **`@classmethod`**: Usa un `cls` para hablarle a EL MOLDE ENTERO. Si cambias algo aquí, afectas instantáneamente a todos los objetos pasados y futuros de la clase.*

### 💡 Conceptos Clave de Programación Funcional:

**7. List Comprehension y Lambdas**
*- **List Comprehension:** La forma corporativa veloz de comprimir bucles de 4 líneas y un `.append()` en una sola línea entre corchetes `[accion for x in lista]`. Se usa intensamente para limpiar datos en memoria.*
*- **Lambdas:** Funciones anónimas desechables `lambda x: formula` que no ocupan la reserva permanente de la memoria. Perfectas para cálculos simples que solo se usan una vez.*

**8. Turbinas en Lenguaje C (`map` y `filter`)**
*- `map`: Inyecta una función a absolutamente todos los elementos de un iterable para transformarlos masivamente.*
*- `filter`: Pasa un iterable por un colador condicional, destruyendo lo que devuelva `False`.*
*(Se deben envolver en un `list()` para extraer sus resultados, porque por debajo son iteradores perezosos).*

**9. El Agujero Negro Infinito (`*args` y `**kwargs`)**
*Cuando construyes sistemas robustos y no sabes cuántos datos te inyectará un usuario o una tabla SQL:*
*- `*args`: Comprime infinitos argumentos posicionales sueltos en una Tupla.*
*- `**kwargs`: Comprime infinitos argumentos con nombre (`clave="valor"`) en un Diccionario.*

**10. La Pausa del Tiempo (Generadores y `yield`)**
*Si una función debe procesar 10 Millones de bases de datos, un `return` destruiría la RAM. En su lugar, usamos `yield`. Esto expulsa UN solo dato, pausa a la función, y espera pacientemente a que se le ordene continuar con un `next()`. Si lo conectas a un bucle `for`, el bucle jalará los 10 millones de datos de uno por uno sin que la memoria colapse jamás.*

---

## 📅 Sesión: Introducción a SQL Profundo (20/09/2026)

### 💡 Conceptos Clave:

**1. ¿Cuál es la verdadera diferencia entre un `WHERE` y un `HAVING`?**
*Aunque ambos actúan como comandos lógicos de filtro, su momento de ejecución en la arquitectura es diferente:*
*- **WHERE:** Actúa como filtro directo sobre la "columna cruda" (datos originales) **antes** de que ocurra cualquier operación matemática.*
*- **HAVING:** Funciona como filtro **después** de que a las columnas se les ha aplicado un cálculo estadístico o función de agregación (como `SUM` o `MAX`).*

**2. ¿Qué es exactamente el `INNER JOIN`?**
*Es la función relacional que nos permite fusionar dos tablas mediante una llave o ID en común. El `INNER JOIN` representa una **intersección matemática pura**: solamente rescata los registros que existen en AMBAS tablas simultáneamente. Si un dato no tiene su pareja correspondiente en el otro lado, es excluido totalmente del reporte final.*

**3. ¿Para qué sirve el `GROUP BY` y con qué funciones se combina?**
*La cláusula `GROUP BY` sirve para agrupar la salida de la consulta, cortando la base de datos en "cajas" basadas en una variable cualitativa (ej. Departamento).*
*Es **obligatorio** usarla siempre que en nuestro `SELECT` mezclemos columnas de texto descriptivo con **funciones de agregación matemáticas** (`SUM()`, `AVG()`, `MAX()`, `MIN()`, `COUNT()`). Si no usamos el `GROUP BY`, el motor colapsa al intentar mostrar múltiples categorías de texto junto a un solo gran total numérico.*
*(Nota de Arquitectura: Si pasamos múltiples columnas al `GROUP BY`, SQL creará micro-grupos para cada combinación exacta, lo que divide los totales. Para manejar totales macro y micro al mismo tiempo, en un futuro usaremos Window Functions).*

**4. ¿Cómo descubrir Tablas y Columnas en una base de datos desconocida (Metadatos)?**
*Cuando me enfrento a una bóveda SQL ciega sin Diagrama Entidad-Relación, uso los escáneres de metadatos:*
*- Para descubrir **Tablas**: `SELECT name FROM sqlite_master WHERE type = 'table';`*
*- Para descubrir **Columnas y Llaves Primarias**: `PRAGMA table_info(nombre_tabla);`. Esto devuelve una tupla por columna. Si el último valor (`pk`) es 1, esa columna es la Llave Primaria.*

**5. El Pipeline Híbrido (Python 🤝 SQL) y el concepto de `fetchall()`**
*En la industria, SQL rara vez se ejecuta manualmente. Python se conecta mediante un `cursor.execute()`.*
*- Si hacemos un `INSERT INTO`, ejecutamos `conexion.commit()` para sellar la inyección en el disco duro.*
*- Si hacemos un `SELECT`, usamos `cursor.fetchall()`. Esto extrae los resultados desde SQL hacia la memoria RAM de Python convirtiéndolos en una **Lista de Tuplas**, que luego podemos iterar e indexar (ej. `fila[2]`) con un simple bucle `for`.*

**6. Ingeniería de Resiliencia: `IntegrityError` y `try/except`**
*Cuando extraemos datos de JSON y los inyectamos a SQL, puede ocurrir una Colisión de Llaves Primarias (intentar insertar un ID que ya existe). En lugar de dejar que el programa explote, usamos un `try / except sqlite3.IntegrityError:` para ignorar limpiamente el clon y continuar inyectando el resto de los datos.*
*(Nota de Sistemas: Si alguna vez Windows prohíbe borrar un archivo `.db`, es por el **File Locking**. Un cursor de Python anterior no cerró la puerta (`conexion.close()`) y el archivo se quedó bloqueado en la memoria).*

**7. La Familia DQL (Data Query Language / Lenguaje de Consulta) Son los comandos `"Ojos"` (solo miran, no tocan).**
1. *El único Rey*: `SELECT`
2. *Comportamiento*: Entran a la base de datos, toman una "foto" de la información y te la traen. No alteran absolutamente nada del disco duro.
3. *Protocolo en Python*: Aquí SÍ es obligatorio usar `cursor.fetchall()`, porque SQL te está devolviendo físicamente una tabla para que la leas.

**8. La Familia DML (Data Manipulation Language / Lenguaje de Manipulación) Son los comandos `"Manos"` (meten información, la alteran o la destruyen).**
1. *La Trinidad*: `INSERT`, `UPDATE`, `DELETE`.
2. *Comportamiento*: Estos comandos son ejecutores. Van a la bóveda, inyectan un nuevo empleado `(INSERT)`, borran al HDMI `(DELETE)` o cambian un sueldo `(UPDATE)`.
3. *Protocolo en Python*: Estos comandos trabajan en las sombras. Hacen el trabajo sucio y se callan. NO devuelven tablas, por lo que el *fetchall()* no funciona con ellos. Solo requieren una cosa para vivir: que selles su obra con `conexion.commit()`.

---

## 📅 Sesión: Arquitectura MVC, Separación de Capas y SQL Avanzado (27/09/2026)

### 🧠 Conceptos Clave:

**1. El Patrón MVC (Modelo-Vista-Controlador)**
*Una arquitectura profesional separa el software en capas especializadas:*
*- **La Base de Datos (`database.py`)**: El "Sótano". Su única misión es ejecutar `SELECT`, `INSERT`, `GROUP BY` y hablar con el disco duro.*
*- **El Modelo (`models.py`)**: El "Cerebro". Aquí viven nuestras clases OOP (ej. `Compra`). Inyecta el ADN con `__init__`, valida las reglas del negocio, y le ordena al sótano qué guardar. Jamás usa `print()` para hablar con el usuario; solo retorna datos o textos crudos (Separación de Responsabilidades).*
*- **El Controlador (`main.py`)**: El "Cajero Automático". Es lo más tonto posible. Su única misión es mostrar el menú visual (la Vista), atrapar los inputs del usuario, y pasárselos al Cerebro. Atrapa errores con `try/except` para no crashear.*

**2. La Regla de Oro del Big Data: El Motor SQL vs La Memoria RAM de Python**
*- **Mala Arquitectura:** Hacer un `SELECT *` para traer 10,000 registros crudos a Python y usar un bucle `for` o una List Comprehension para filtrarlos o sumarlos. Esto colapsa la memoria RAM y procesa información inútil.*
*- **Buena Arquitectura:** Delegar las matemáticas al motor SQL (que está optimizado en C). Si necesitamos una suma o un filtrado, creamos una función específica en la base de datos usando `SUM()`, `COUNT()`, `GROUP BY` y `WHERE`. SQL procesa el trabajo pesado y solo devuelve un ligero paquete con la respuesta.*

**3. El Escudo Protector `?` (Placeholder) vs El Comodín `%` (Wildcard)**
*- En SQLite3, el símbolo `%` es el comodín para buscar textos parciales (`LIKE '%Atún%'`).*
*- El símbolo `?` es el marcador de parámetros para Python. Inyectar variables usando `?` empaquetadas en una tupla no es solo un capricho sintáctico; es una armadura de titanio contra ataques de **Inyección SQL**. Obliga al motor a tratar el input estrictamente como texto, impidiendo que hackers ejecuten comandos maliciosos como `"; DROP TABLE;"`.*

**4. El Choque del Doble Print**
*Un error de arquitectura común al enviar mensajes desde el Modelo al Controlador. La función `print()` en Python es una acción, y su valor de retorno es `None`. Si el Modelo hace un `return print("Error")`, le envía `None` al Controlador. Si el Controlador luego hace un `print()` sobre ese retorno, imprimirá la palabra `None` en pantalla. Solución: El Modelo retorna un simple *f-string*, y el Controlador hace el único `print()`.*

---

## 📅 Sesión: Inmersión en Data Science, Pandas y Estadística Descriptiva (21/10/2026)

### 🧠 Conceptos Clave y Lecciones Aprendidas:

**1. Arquitectura de Herramientas: Kernel vs. Entorno Virtual (`venv`)**
- En Jupyter Notebooks (`.ipynb`), el código se ejecuta celda por celda de forma modular gracias al **Kernel** (`ipykernel`), un proceso vivo en memoria RAM.
- **El error clásico del Data Scientist novato:** Tener instaladas las librerías en un `venv` pero ejecutar el notebook con el Python global del sistema, lo que genera `ModuleNotFoundError: No module named 'pandas'`.
- **Fallo de Service Worker en VS Code:** Si VS Code muestra `Failed to register a ServiceWorker: The document is in an invalid state`, es un cuelgue del motor Chromium interno de Electron; se resuelve cerrando la ventana completa de VS Code o recargando con `Ctrl + Shift + P` -> `Developer: Reload Window`.

**2. Anatomía de Pandas: `pd.Series` frente a `pd.DataFrame`**
- Una `Series` es una estructura unidimensional (1D) compuesta de Valores + Índice.
- Un `DataFrame` es una estructura bidimensional (2D) que opera conceptualmente como un diccionario de `Series` sincronizadas por el mismo índice.

**3. El Choque Estadístico Fundamental: Media Aritmética vs. Mediana**
- En un dataset de 10.000 ventas de retail, la media de gasto fue de **216,21 €** mientras que la mediana real fue de solo **50,91 €**.
- **Sesgo Positivo (Asimetría hacia la Derecha / Right-Skewed):** Ocurre cuando la Media > Mediana. La media es ultra-sensible a valores atípicos (*outliers*), inflando la percepción de ingresos. La mediana es un estadístico robusto que refleja con fidelidad el comportamiento del cliente típico.
- Conclusión para CFO: Presupuestar asumiendo que cada cliente gasta 216 € llevaría a la quiebra comercial; el 50% de los clientes gasta 50,91 € o menos.

**4. Detección Vectorizada de Nulos**
- En lugar de restar a mano o usar calculadoras, en Pandas combinamos dos métodos vectorizados: `df.isnull().sum()` para contar los `True` de valores faltantes por columna, y `(df.isnull().mean() * 100).round(2)` para medir su porcentaje.

**5. Identificación Automatizada con `.idxmax()` y `.max()`**
- `.max()` devuelve el valor numérico máximo (ej. 2.072 transacciones).
- `.idxmax()` (*Index of Max*) devuelve la etiqueta del índice asociada a dicho máximo (ej. categoría `'Alimentos'`).
- **Optimización de memoria:** En datasets de millones de filas, se calcula el recuento una sola vez (`conteo = df['col'].value_counts()`) y luego se extrae el `.idxmax()` y `.max()`, evitando duplicar el tiempo de CPU.

**6. Indexación Booleana (El `WHERE` de SQL en Pandas)**
- Las operaciones de filtrado se realizan evaluando condiciones lógicas vectorizadas (Máscaras Booleanas).
- Para filtros multivariables:
  - Se sustituye el `AND` por **`&`** y el `OR` por **`|`**.
  - **La regla de los paréntesis:** Cada condición DEBE ir entre paréntesis `(df['city'] == 'Madrid') & (df['total_spend'] > 500)` debido a la precedencia del operador bitwise en Python.

**7. Agrupaciones: El Patrón Split-Apply-Combine (`groupby`)**
- El equivalente exacto al `GROUP BY` de SQL es `df.groupby('city')['total_spend'].agg(['count', 'sum', 'median', 'mean'])`.
- Ordenación con `.sort_values(by='sum', ascending=False)`.
- **La Paradoja de Negocio:** 
  - **Madrid** lidera en recaudación total (757.454 €) por volumen de compras (3.550 pedidos).
  - **Barcelona** parece tener clientes más gastadores si se mira solo la media (223,00 € vs 213,37 €).
  - Pero al auditar la mediana (**52,09 € en Madrid vs 51,34 € en Barcelona**), se descubre que el cliente mediano de Madrid gasta más; la media de Barcelona estaba inflada por compras corporativas atípicas (*outliers*).
- En Jupyter, para presentar tablas interactivas con formato HTML se utiliza `display(dataframe)` o se deja la variable al final de la celda, evitando el texto plano de `print()`.
