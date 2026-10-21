# 🛠️ Guía Maestra: VS Code para Ciencia de Datos y Jupyter Notebooks

Esta guía resume el funcionamiento interno de **Visual Studio Code** al trabajar con Jupyter Notebooks (`.ipynb`), entornos virtuales de Python (`venv`), selección de Kernels y las herramientas interactivas que aceleran el análisis de datos.

---

## 🧠 1. ¿Qué es el Kernel de Jupyter y por qué importa?

Cuando abres un archivo `.py`, VS Code ejecuta el script de inicio a fin en un proceso que nace y muere.
En un Notebook (`.ipynb`), el código se ejecuta de forma **interactiva y modular en celdas**.

Para que eso sea posible, existe un motor en segundo plano llamado **Kernel**:
- **El Kernel** es un proceso activo que mantiene en la memoria RAM todas las variables, DataFrames, funciones y librerías que vas cargando celda por celda.
- **El Entorno Virtual (`venv`)** es la carpeta donde están instaladas tus librerías (`pandas`, `numpy`, `matplotlib`).

```
┌────────────────────────────────────────────────────────┐
│               Visual Studio Code (UI)                  │
│       [ Celda 1 ] ──> [ Celda 2 ] ──> [ Celda 3 ]      │
└───────────────────────────┬────────────────────────────┘
                            │ (Envía el código de la celda)
                            ▼
┌────────────────────────────────────────────────────────┐
│                   Jupyter Kernel                       │
│        (Proceso `ipykernel` vivo en memoria RAM)        │
│    Mantiene: df, variables, cálculos intermedios...    │
└───────────────────────────┬────────────────────────────┘
                            │ (Usa el Python y librerías de...)
                            ▼
┌────────────────────────────────────────────────────────┐
│           Entorno Virtual (`venv` del proyecto)        │
│       Python 3.12 + Pandas + NumPy + Matplotlib        │
└────────────────────────────────────────────────────────┘
```

> [!CAUTION]
> **El Error Clásico del Principiante:**
> Si tienes instaladas las librerías en tu `venv`, pero el Kernel de VS Code apunta al Python global del sistema, verás el temido error:
> `ModuleNotFoundError: No module named 'pandas'`
> **Causa:** El Kernel está ejecutando el Python equivocado.

---

## 🎯 2. Cómo Seleccionar el Kernel Correcto en VS Code (Paso a Paso)

Cada vez que abras un Notebook (`.ipynb`) en VS Code:

1. **Mira la esquina superior derecha** del Notebook.
2. Verás un botón que dice **`Select Kernel`** (o el nombre de un Python actual).
3. Haz clic sobre él. Se abrirá la paleta de comandos arriba:
   - Selecciona **`Python Environments...`**
   - Elige el entorno virtual de tu proyecto:
     `Python 3.x.x ('venv': venv) .\Bootcamp_ERP_Personal\venv\Scripts\python.exe`
4. **Verificación rápida:**
   En la primera celda del Notebook, ejecuta:
   ```python
   import sys
   print(sys.executable)
   ```
   Debe mostrarte la ruta que termina en `...\Bootcamp_ERP_Personal\venv\Scripts\python.exe`.

---

## ⚡ 3. Atajos de Teclado Imprescindibles (Productividad Pro)

Los Notebooks tienen dos modos:
- **Modo Comando (Azul/Gris):** Para moverte entre celdas y manipular la estructura. Se activa pulsando `Esc`.
- **Modo Edición (Verde):** Para escribir código dentro de una celda. Se activa pulsando `Enter` o haciendo clic dentro.

### 🏃 Ejecución de Celdas:
| Atajo | Acción |
| :--- | :--- |
| `Shift + Enter` | **Ejecuta la celda actual** y salta a la siguiente (o crea una nueva si es la última). *El atajo rey.* |
| `Ctrl + Enter` | **Ejecuta la celda actual** y se queda en ella. |
| `Alt + Enter` | **Ejecuta la celda actual** e inserta una nueva celda debajo inmediatamente. |

### 🛠️ Manipulación de Celdas (En Modo Comando, pulsa `Esc` primero):
| Tecla | Acción |
| :---: | :--- |
| `A` | Inserta una celda vacía **arriba** (*Above*). |
| `B` | Inserta una celda vacía **abajo** (*Below*). |
| `D + D` | (Pulsar la 'D' dos veces seguidas) **Elimina** la celda actual. |
| `M` | Convierte la celda a texto **Markdown** (para notas y conclusiones). |
| `Y` | Convierte la celda a código **Python**. |
| `Z` | Deshace la última acción en celdas (recupera una celda borrada por error). |

---

## 📊 4. Herramientas Avanzadas de VS Code para Datos

### A. El Visor de Variables (*Jupyter Variable View*)
En la barra superior de herramientas del Notebook, haz clic en el icono **`Variables`** (junto a *Clear All Outputs* y *Restart*).
- Se abrirá un panel inferior mostrando **todas las variables activas en memoria**, su tipo (`DataFrame`, `int`, `list`), su tamaño y forma (`10000, 11`).

### B. El Data Viewer (Explorador tipo Excel integrado)
- En el panel de variables, junto a cualquier DataFrame (ej. `df`), verás un pequeño icono con forma de tabla a la izquierda.
- Haz clic sobre él: VS Code abrirá una pestaña interactiva para filtrar, ordenar y buscar dentro del DataFrame como si estuvieras en Excel, pero con la velocidad de memoria de Python.

---

## 🧪 5. Las 3 Reglas de Oro en Notebooks

1. **Orden Lineal Estricto:** Ejecuta las celdas siempre de arriba a abajo. Si ejecutas una celda inferior, cambias una variable y luego vuelves a una celda superior, el estado en memoria será caótico y difícil de reproducir.
2. **El Test de Reproducibilidad:** Antes de dar por terminado un análisis o subir un commit a Git, haz clic en **`Restart Kernel`** y luego en **`Run All`**. Si corre de principio a fin sin errores, tu análisis es científicamente reproducible.
3. **Limpieza de Outputs para Git:** Si el Notebook genera gráficos muy pesados o datos sensibles, puedes usar *Clear All Outputs* antes de hacer commit, o configurar herramientas para no saturar el repositorio.
