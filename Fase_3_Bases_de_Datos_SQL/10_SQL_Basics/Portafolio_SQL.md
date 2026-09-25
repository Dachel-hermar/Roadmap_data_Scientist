# 📂 Portafolio de Consultas SQL

Este documento sirve como registro oficial (Log) de todas las consultas, misiones y retos superados durante el entrenamiento. 
Al separar el código final aquí, mantenemos nuestro archivo de ejecución (`consulta.sql`) limpio y evitamos errores en el pipeline, mientras construimos una vitrina perfecta para que los reclutadores en GitHub vean nuestro progreso.

---

## Lo primero es consultar nuestras tablas en las base de datos, si nadie te dio el Diagrama Entidad-Relación
```sql
SELECT name 
FROM sqlite_master 
WHERE type = 'table';
```

**2. Descubrir las Columnas y las Llaves Primarias (PK)**
*Para mapear la estructura interna de una tabla y descubrir sus Llaves Primarias usamos comandos de sistema interno como PRAGMA (en SQLite).*
```python
# Escáner de Metadatos ejecutado desde Python
cursor.execute("PRAGMA table_info(empleados)")
```
*Si el último valor de la tupla (`pk`) es 1, hemos encontrado la Llave Primaria.*

---

## 🛠️ Misión 1 a 6: Fundamentos de Extracción

**Misión 06: La Auditoría de Comisiones (Filtros, Joins y Agrupaciones)**
*El Director Comercial necesitaba saber qué empleados superaron los $1000 dólares en ventas para pagar bonos.*
```sql
SELECT empleados.nombre, SUM(ventas.monto) AS ventas_totales
FROM empleados
INNER JOIN ventas ON empleados.id_empleado = ventas.id_empleado
GROUP BY empleados.nombre
HAVING SUM(ventas.monto) > 1000
ORDER BY ventas_totales DESC;
```
*Conclusión de Negocios: Elena Martínez aplastó la cuota mensual con 2350 dólares. Ana Garcia no quedó muy atrás con 2300 dólares. Se aprueba un bono a ambas empleadas.*

---

## 🔥 La Forja: Bootcamp de 10 Retos Corporativos

**Reto 1: Auditoría de Salarios en Tecnología**
/*
 Finanzas necesita que extraigas únicamente el nombre y
el salario de los empleados que pertenecen al departamento de 'IT' y que, además, ganan estrictamente más de $55,000. 
El reporte debe imprimirse ordenado, mostrando el salario más alto en la parte superior.
*/
```sql
SELECT nombre, salario 
FROM empleados 
WHERE departamento='IT' AND salario > 55000
ORDER BY salario DESC;
```
** Conclusiones**
> Como podemos observar solamente hay dos trabajadores que cumplen con el criterio de Finanzas para su análisis.David Ruiz con un salario de 60000 euros y Fernando Torres con un salrio de 58000, este último es el nuevo fichaje del departamento

**⚔️ Reto 2: El Censo de Recursos Humanos**
> El área de Talento Humano quiere medir la densidad poblacional de la empresa. Necesitan un reporte de solo dos columnas: El nombre del departamento y la cantidad total de personas que trabajan en cada uno. (Pista de Arquitectura: en lugar de sumar el dinero con SUM, agrupa y usa la función matemática de contar: COUNT(id_empleado)).
```sql
SELECT departamento, count(id_empleado) AS total_empleados
FROM empleados
GROUP BY departamento;
```
**Conclusiones**
/*
El nuemro de trabajadores por departamento son los siguientes:
 IT             |                 2 |
| Marketing      |                 2 |
| Ventas         |                 3
*/

**⚔️ Reto 3: El Espía Interdepartamental**
> El Gerente de Ventas está furioso porque sospecha que empleados de otras áreas están registrando ventas sin permiso. Cruza tu tabla de empleados con la tabla de ventas. Necesito un reporte que muestre el nombre, el departamento y el producto vendido, pero EXCLUYENDO rotundamente a los empleados que pertenezcan a 'Ventas'. (Pista de Lógica: El operador "Diferente a" o "No es igual a" en SQL se escribe como !=).
```sql
SELECT empleados.nombre, empleados.departamento, ventas.producto
FROM empleados
INNER JOIN ventas ON empleados.id_empleado = ventas.id_empleado
WHERE empleados.departamento != 'Ventas';
```
**Conclusiones**
> "Auditoría completada. 0 incidencias. Nadie te está robando ventas."