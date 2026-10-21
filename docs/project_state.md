# 📍 Estado del Proyecto: Roadmap Científico de Datos

Este documento sirve como nuestra brújula. Lo revisamos al inicio y al final de cada sesión para saber con exactitud dónde estamos, qué hemos logrado y cuál es el siguiente reto técnico.

---

## 📍 Estado Actual General
- **Fase Actual:** **Fase 4: Análisis de Datos, Pandas y Estadística Descriptiva Aplicada**
- **Laboratorio:** `Fase_4_Analisis_Datos_Pandas/01_Fundamentos_Pandas_y_Estadistica.ipynb`
- **Dataset de Estudio:** `ventas_retail_10k.csv` (10.000 transacciones de comercio electrónico real)
- **Estado de la Sesión:** Módulos 1 al 5 completados con excelencia y documentados en Git.

---

## 🏆 Hitos Completados (Lo que ya dominamos)

### 🧠 Cimientos y Forja Algorítmica (Completado)
- [x] Lógica de Programación y Pseudocódigo en Papel.
- [x] Python Core Profundo: Estructuras de datos (`dict`, `list`, `set`, `tuple`), slicing, scopes, JSON y manejo estructurado de errores (`try/except`).
- [x] Bases de Datos y SQL Profundo: DQL (`SELECT`, `WHERE`, `HAVING`, `GROUP BY`), DML (`INSERT`, `UPDATE`), y Joins relacionales (`INNER`, `LEFT`).
- [x] Programación Orientada a Objetos (POO): Encapsulamiento, Polimorfismo, Métodos Dunder, `@classmethod`, `@property` y arquitectura MVC.
- [x] Paradigma Funcional: Lambdas, `map()`, `filter()` y generadores con `yield`.

### 🛒 Bootcamp ERP Personal (Sistemas Empresariales en Producción)
- [x] **v1.0-inventario:** Sistema de Inventario y Optimización de Compras (Supabase Cloud + MVC).
- [x] **v2.0-flujo-efectivo:** Control de Flujo de Efectivo y Metas de Ahorro (Cruces de tablas, `INNER JOIN`).
- [x] **v3.0-simulador-irpf:** Motor Fiscal de IRPF Progresivo Comunidad de Madrid (Cálculo por tramos con `@classmethod` y pipelines funcionales).

### 📊 Fase 4: Fundamentos de Pandas y Estadística (En Curso Activo - Día 1)
- [x] **Tooling Profesional:** Configuración de VS Code, kernel Jupyter ligado al `venv` (`ipykernel`), resolución de Service Workers y shortcuts de navegación (`Shift+Enter`, `A`, `B`, `DD`).
- [x] **Diagnóstico y Calidad de Datos:** Auditoría de dimensiones con `.shape` y detección vectorizada de nulos con `.isnull().sum()`.
- [x] **El Choque Estadístico:** Media (216,21 €) vs. Mediana (50,91 €). Detección del fenómeno de **Sesgo Positivo (*Right-Skewed*)** e insensibilidad de la mediana ante outliers.
- [x] **Anatomía de Pandas:** Operaciones sobre `pd.Series`, análisis univariante de frecuencias con `.value_counts()` y extracción atómica con `.idxmax()` y `.max()`.
- [x] **Indexación Booleana (El `WHERE` de SQL):** Máscaras lógicas univariables (`total_spend > 1000` con 483 compras VIP) y multivariables con operadores bitwise `&` y paréntesis obligatorios (`(city == 'Madrid') & (total_spend > 500)`).
- [x] **Agrupaciones y Agregaciones (El `GROUP BY` de SQL):** Patrón *Split-Apply-Combine* (`groupby`), múltiples métricas simultáneas (`agg(['count', 'sum', 'median', 'mean'])`), ordenación con `.sort_values()` y presentación interactiva HTML con `display()`.
- [x] **Storytelling y Hallazgo de Negocio:** La Paradoja de Madrid (gana en volumen y recaudación total) vs. Barcelona (aparenta mayor ticket promedio pero tiene menor gasto mediano por compras corporativas atípicas).

---

## 🎯 Próximos Pasos (Sesión de Mañana)
1. **Detección Matemática de Outliers con John Tukey:**
   - Cálculo de Cuartiles $Q_1$ (percentil 25) y $Q_3$ (percentil 75) con `.quantile()`.
   - Cálculo del Rango Intercuartílico ($IQR = Q_3 - Q_1$).
   - Determinación del límite superior: $Límite = Q_3 + (1.5 \times IQR)$ y filtrado de pedidos anómalos.
2. **Visualización Científica con Matplotlib y Seaborn:**
   - Creación del primer Diagrama de Caja y Bigotes (*Boxplot*) para visualizar la dispersión y la cola de outliers.
   - Histograma con Curva de Densidad (KDE) para ver el sesgo positivo gráficamente.
