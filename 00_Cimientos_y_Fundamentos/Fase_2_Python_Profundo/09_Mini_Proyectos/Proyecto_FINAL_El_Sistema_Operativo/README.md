# 📊 Proyecto Final Omega: CRM Analytics & Pipeline ETL

## 📝 Resumen Ejecutivo
Este proyecto consiste en el desarrollo de un **CRM Analítico Financiero** en Python. Su núcleo es un *pipeline* ETL robusto diseñado para procesar archivos de transacciones diarias (CSV), limpiando datos corruptos, evadiendo errores del sistema y deduplicando registros en tiempo real. 

Posteriormente, el sistema cruza esta información transaccional con una base de datos maestra histórica (JSON) para ejecutar operaciones matemáticas y estadísticas de consolidación. El objetivo final es calcular el **Valor Neto Real** de la cartera corporativa, detectando automáticamente al cliente más valioso para facilitar la toma de decisiones estratégicas a nivel directivo.

## 🛠️ Stack Técnico y Arquitectura
- **Lenguaje:** Python 3
- **Arquitectura:** Bucle interactivo (`while True`) con menús de selección.
- **Manejo de Errores:** Bloques `try/except` para evadir *strings* anómalos en columnas numéricas.
- **Estructuras de Datos:** 
  - `Sets` para deduplicación `O(1)` de transacciones.
  - `Diccionarios` como acumuladores estadísticos.
- **File Handling:** Lectura y cruce asíncrono de formatos `.csv` y `.json`.
- **Algoritmia:** Aplicación del Algoritmo de "Búsqueda del Máximo" (Variable Campeón) para rankings de clientes.
