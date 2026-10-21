# Bootcamp Final: El ERP Personal (Fase 4 - Fase 5)

## Visión del Proyecto
El estudiante ha detectado que los retos anteriores han sido "digeridos" (plantillas base). Para forzar la asimilación real de la Arquitectura de Software, construiremos 10 aplicaciones monolíticas que resuelvan problemas reales de su vida diaria. Todos los proyectos estarán respaldados por Bases de Datos (SQLite3) persistentes, programados estrictamente con Programación Orientada a Objetos, e integrados entre sí.

Este bootcamp marca la transición definitiva hacia Pandas y Data Analysis.

## Reglas del Bootcamp
1. **Cero Código Base:** El mentor no entregará plantillas pre-fabricadas. Solo dará requisitos de negocio.
2. **Persistencia Total:** Toda aplicación debe conectarse a `sqlite3`. Nada vive solo en RAM.
3. **Módulos:** Ningún proyecto debe programarse en un solo archivo. Se exigirá el uso de `import`.
4. **Data Storytelling:** El objetivo final de cada sistema es escupir "Reportes Estadísticos" que guíen las decisiones financieras del estudiante.

---

## Los 10 Proyectos (El Ecosistema)

### 📦 1. Sistema de Inventario y Optimización de Compras
- **Problema:** Registrar productos de supermercado, rastrear stock y descubrir en qué supermercado es más barato comprar cada cosa.
- **Tecnologías:** OOP Clásica, SQL (CRUD, GROUP BY), Entornos Virtuales.
- **Entregable:** Un reporte estadístico de optimización de precios.

### 💸 2. Analizador de Flujo de Efectivo (Gastos Domésticos)
- **Problema:** Control de gastos de pareja (Ahorro, Inversiones, Tabaco, Alquiler). Debe comunicarse con la base de datos del Proyecto 1 para no duplicar datos de comida.
- **Tecnologías:** Herencia de Clases, SQL `JOIN`, Funciones Lambda para cálculo de métricas (ej. % de ingresos gastado en tabaco).

### 🏛️ 3. Simulador Fiscal IRPF (Madrid)
- **Problema:** Cálculo del Impuesto sobre la Renta de las Personas Físicas según los tramos autonómicos de la Comunidad de Madrid.
- **Tecnologías:** Algoritmia avanzada de tramos fiscales, Decoradores de Clase (`@classmethod`) para actualizar los tramos del gobierno, `map`/`filter`.

### ⏱️ 4. Gestor de Suscripciones y Fugas de Capital
- **Problema:** Rastrear pagos recurrentes (Netflix, Gimnasio, Software) y predecir el impacto anual en las finanzas.
- **Tecnologías:** Librería `datetime`, Generadores (`yield`) para simular meses futuros.

### 📈 5. Portafolio de Inversiones y Ahorro Compuesto
- **Problema:** Registrar aportes mensuales de ahorro e inversiones, y proyectar su crecimiento a 10 años.
- **Tecnologías:** OOP (Métodos Dunder para comparar rentabilidades), SQL.

### 🚬 6. Rastreador de Reducción de Hábitos (Health Tracker)
- **Problema:** Monitorizar la reducción del consumo de tabaco de la pareja, cruzando el impacto en la salud con el ahorro financiero en tiempo real.
- **Tecnologías:** `filter`, SQL `HAVING`, correlación de variables.

### 📚 7. Cerebro Digital (Gestor de Conocimiento y Roadmap)
- **Problema:** Una base de datos para almacenar resúmenes de libros, cursos de Data Science y snippets de código.
- **Tecnologías:** NLP básico (búsqueda de palabras clave en SQL con `LIKE`), List Comprehensions.

### ✈️ 8. Radar de Viajes y Vacaciones
- **Problema:** Guardar un historial de cotizaciones de vuelos y hoteles para analizar la estacionalidad de precios a lo largo del año.
- **Tecnologías:** SQL `ORDER BY`, Agrupaciones lógicas.

### 🚗 9. Calculadora de Depreciación y Activos Fijos
- **Problema:** Controlar el valor real de los equipos tecnológicos (Laptops, Teléfonos) y calcular cuándo es financieramente rentable venderlos/renovarlos.
- **Tecnologías:** Algoritmos de amortización, Polimorfismo (Distintos tipos de activos deprecian a distinto ritmo).

### 👑 10. El "Dashboard" C-Level (Integración Total)
- **Problema:** Las 9 aplicaciones anteriores operan en bases de datos separadas o tablas distintas.
- **Tu Misión Máxima:** Crear un archivo maestro (El CEO) que importe los 9 proyectos usando `import`, consulte todas las bases de datos de forma asíncrona, y genere un **Reporte Financiero y de Vida General** consolidado.

---

## User Review Required
> [!IMPORTANT]  
> Arquitecto, revisa estos 10 sistemas. ¿Cumplen con tu visión de automatizar tu vida real? Si apruebas el plan, crearemos tu Entorno Virtual y comenzaremos con la arquitectura del Proyecto 1.
