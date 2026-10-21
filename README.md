<div align="center">

# 🚀 Data Science & Machine Learning Engineering Roadmap
### *From Business Requirements to Production-Grade Data Pipelines & Systems*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Cloud%20Supabase-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://supabase.com)
[![Architecture](https://img.shields.io/badge/Architecture-Clean%20MVC%20%7C%20OOP-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
[![MLOps](https://img.shields.io/badge/MLOps-Pipelines%20Ready-success?style=for-the-badge&logo=fastapi)](https://github.com/Dachel-hermar/Roadmap_data_Scientist)
[![Git Versioning](https://img.shields.io/badge/Versioning-SemVer%20Tags-blueviolet?style=for-the-badge&logo=git)](https://github.com/Dachel-hermar/Roadmap_data_Scientist/tags)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://github.com/Dachel-hermar/Roadmap_data_Scientist)

<p align="center">
  <b>Author:</b> Dachel Hermar &bull; Aspiring Data Scientist & ML Engineer<br>
  <i>"El código aislado en un notebook no sirve; el verdadero valor reside en pipelines reproducibles conectados a sistemas de negocio reales."</i>
</p>

---

</div>

## 📌 Executive Summary

Este repositorio documenta mi trayectoria estructurada hacia la **Ciencia de Datos y el Machine Learning de Grado Productivo**. A diferencia de los programas formativos convencionales basados en tutoriales pasivos y scripts aislados, este proyecto está forjado bajo **estándares estrictos de Ingeniería de Software (Clean Code, MVC, POO Avanzada, SQL Relacional en la Nube y Principios MLOps)**.

Aquí no encontrarás scripts huérfanos: cada módulo resuelve un problema de negocio real, persiste datos en un clúster PostgreSQL en la nube, implementa pruebas de regresión y está versionado semánticamente mediante Git Tags.

---

## 🏛️ Arquitectura del Repositorio (Monorepo)

El repositorio sigue un patrón modular limpio (*Separation of Concerns*), segregando los cimientos algorítmicos, los sistemas empresariales y la documentación técnica:

```text
Roadmap_data_Scientist/
│
├── 📂 Bootcamp_ERP_Personal/              # Motores y Sistemas Empresariales End-to-End
│   ├── 🛒 01_Inventario_Supermercado/      # Motor CRUD, Optimización de Precios & MVC
│   ├── 💸 02_Flujo_Efectivo/              # Cruces Inter-DB, Limpieza Algorítmica & SQL JOIN
│   ├── 🏛️ 03_Simulador_IRPF/              # Motor Fiscal Progresivo (@classmethod, map & filter)
│   ├── ⏱️ 04_Gestor_Suscripciones/        # Simulación Temporal con datetime & yield (En desarrollo)
│   ├── 📊 05_a_10_Modulos_Avanzados/      # Inversiones, Hábitos, Radar & Dashboard C-Level
│   ├── ⚙️ venv/                           # Entorno virtual aislado con librerías científicas
│   └── 🔒 .env                            # Credenciales cifradas de base de datos en la nube
│
├── 📂 00_Cimientos_y_Fundamentos/          # La Forja Algorítmica Inicial
│   ├── 🧠 Fase_1_Logica_y_Cimientos/      # Pseudocódigo, algoritmos atómicos & hipótesis
│   ├── 💻 Fase_2_Python_Profundo/         # Estructuras de datos (HashMaps, JSON, Lists)
│   ├── 🔄 Fase_2.5_Refuerzo_Core/         # Data Wrangling, Scopes e Inmutabilidad
│   ├── 🗄️ Fase_3_Bases_de_Datos_SQL/      # SQL Profundo (CRUD, HAVING, Subqueries)
│   └── 🧬 Fase_4_Orientada_a_Objetos/     # POO Pura (Dunder methods, Herencia, Polimorfismo)
│
├── 📂 docs/                               # Documentación Técnica & Bitácora de Aprendizaje
│   ├── 📜 Plan_Estudio_y_Reglas_Maestras.md# El Contrato de 12 Meses y las 16 Reglas
│   ├── 🗺️ Plan_de_Implementacion.md       # Pliego de condiciones de los 10 Proyectos
│   ├── 📓 Diario_Aprendizaje.md           # Explicaciones conceptuales y reflexiones
│   └── 📍 project_state.md                # Bitácora viva de estado y próximos pasos
│
└── 📄 README.md                           # Escaparate técnico y guía de ejecución
```

---

## 💼 Portafolio de Sistemas Desarrollados

### [🛒 01. Sistema de Inventario y Optimización de Compras](file:///C:/Roadmap_data_Scientist/Bootcamp_ERP_Personal/01_Inventario_Supermercado)
- **Problema de Negocio:** Rastrear variaciones de stock e identificar analíticamente en qué supermercado es más económico adquirir cada canasta de productos.
- **Patrones & Arquitectura:** Arquitectura Modelo-Vista-Controlador (MVC), persistencia estricta en PostgreSQL Cloud (Supabase), consultas agregadas (`GROUP BY`, `ROUND`, `SUM`), despacho dinámico de clases.
- **Git Release Tag:** `v1.0-inventario`

### [💸 02. Analizador de Flujo de Efectivo y Control Presupuestario](file:///C:/Roadmap_data_Scientist/Bootcamp_ERP_Personal/02_Flujo_Efectivo)
- **Problema de Negocio:** Integración interdepartamental de gastos domésticos vs. inyecciones de capital, con alertas automáticas de desviación presupuestaria.
- **Patrones & Arquitectura:** Herencia de clases (`super()`), motor propio de extracción y limpieza de texto no estructurado sin regex, cruce relacional con `SQL INNER JOIN` + `GROUP BY` contra tablas de metas financieras, y evaluación ágil con **Funciones Lambda**.
- **Git Release Tag:** `v2.0-flujo-efectivo`

### [🏛️ 03. Simulador Fiscal Progresivo IRPF (Comunidad de Madrid)](file:///C:/Roadmap_data_Scientist/Bootcamp_ERP_Personal/03_Simulador_IRPF)
- **Problema de Negocio:** Cálculo automatizado de liquidación fiscal anual de IRPF bajo la legislación autonómica de Madrid, separando retenciones a cuenta y desgravaciones por alquiler.
- **Patrones & Arquitectura:** Algoritmo progresivo por bloques (*water-bucket model*), decoradores `@classmethod` para actualización dinámica de leyes impositivas en caliente, programación funcional pura (**`filter`** y **`map`**) sobre registros transaccionales, y reporte ejecutivo de *Data Storytelling*.
- **Git Release Tag:** `v3.0-simulador-irpf`

### [🔮 Próxima Frontera: Fase 4 - Data Science & MLOps Pipelines]
- **Enfoque:** Análisis exploratorio (EDA), inferencia estadística, testeo de hipótesis ($p$-value, Test A/B) y feature engineering sobre datasets masivos del mundo real (Kaggle), conectados con **Pandas, NumPy, Scikit-Learn y Dashboards interactivos en Streamlit**.

---

## ⚙️ Principios de Ingeniería y Metodología de Trabajo

El desarrollo en este repositorio sigue **16 Reglas Maestras** diseñadas para asegurar calidad de nivel empresarial:

1. **La Regla del 3x3:** Por cada 3 conceptos técnicos nuevos, se resuelven 3 algoritmos de negocio a ciegas sin plantillas de apoyo.
2. **El Guardián del Óxido (Spaced Repetition):** Ninguna herramienta se abandona; los nuevos módulos integran forzosamente tecnologías de fases anteriores.
3. **Data Storytelling Obligatorio:** Todo script técnico culmina en un informe con conclusiones estratégicas de negocio.
4. **Arquitectura antes que Sintaxis:** Ningún código se pica sin modelado previo de datos y análisis de flujo.
5. **Regla 16 - Principio de Producción & MLOps:** Cero scripts aislados. Todo modelo o análisis estadístico debe formar parte de un pipeline automatizado, reproducible y desplegable en producción.

---

## 🚀 Guía de Instalación y Ejecución Rápida

Para replicar el entorno de desarrollo y ejecutar los sistemas en local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/Dachel-hermar/Roadmap_data_Scientist.git
cd Roadmap_data_Scientist
```

### 2. Configurar el Entorno Virtual e Instalar Dependencias
```bash
# En Windows PowerShell:
python -m venv Bootcamp_ERP_Personal/venv
& "Bootcamp_ERP_Personal/venv/Scripts/Activate.ps1"
pip install -r requirements.txt   # o instalar: pandas numpy psycopg2-binary python-dotenv matplotlib seaborn
```

### 3. Configurar Credenciales (.env)
Crea un archivo `.env` dentro de `Bootcamp_ERP_Personal/` con tu cadena de conexión PostgreSQL:
```env
DATABASE_URL=postgresql://usuario:password@host:5432/postgres
```

### 4. Ejecutar Cualquiera de los Módulos
```bash
# Ejemplo: Ejecutar el Simulador Fiscal IRPF Madrid
python Bootcamp_ERP_Personal/03_Simulador_IRPF/simulador_irpf.py

# Ejemplo: Ejecutar el Analizador de Flujo de Efectivo
python "Bootcamp_ERP_Personal/02_Flujo_Efectivo/main_financiero.py"
```

---

## 📈 Roadmap de Aprendizaje (12 Meses)

```mermaid
gantt
    title Plan Maestro de Especialización en Data Science
    dateFormat  YYYY-MM-DD
    section Fase 1 & 2
    Lógica y Fundamentos             :done, 2026-08-01, 2026-09-01
    section Fase 3
    Python Profundo & Algoritmia     :done, 2026-09-01, 2026-09-20
    SQL Relacional & Nube            :done, 2026-09-20, 2026-10-05
    POO & Arquitectura ERP           :done, 2026-10-05, 2026-10-21
    section Fase 4
    Estadística, NumPy & Pandas      :active, 2026-10-22, 2026-12-01
    EDA, Visualización & Kaggle      : 2026-12-01, 2027-01-15
    section Fase 5 & 6
    Machine Learning (Scikit-Learn)  : 2027-01-15, 2027-03-01
    MLOps, Pipelines & Despliegue    : 2027-03-01, 2027-04-15
    Deep Learning (PyTorch) & NLP    : 2027-04-15, 2027-06-01
```

---

<div align="center">

### 📬 Contacto y Networking

¿Tienes sugerencias sobre la arquitectura o quieres debatir sobre pipelines de datos? ¡Conectemos!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Dachel_Hermar-0A66C2?style=flat-square&logo=linkedin)](https://github.com/Dachel-hermar/Roadmap_data_Scientist)
[![GitHub](https://img.shields.io/badge/GitHub-Dachel--hermar-181717?style=flat-square&logo=github)](https://github.com/Dachel-hermar)

</div>
