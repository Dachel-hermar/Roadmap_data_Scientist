🛒 El Reto #1: Sistema de alertas de caducidad en un Supermercado de barrio
El contexto real: Eres dueño de un pequeño supermercado de barrio. Estás perdiendo dinero porque los lácteos y carnes se caducan en los estantes sin que nadie se dé cuenta, y terminas tirándolos. Necesitas estructurar la lógica de un proceso para controlar esto.

Tu tarea: Sin usar lenguajes de programación, descríbeme tu solución paso a paso:

¿Qué datos específicos necesitas conocer de cada producto cuando entra por la puerta del supermercado?
¿Cuál es el paso a paso lógico que el sistema (o un empleado con una libreta) debe hacer todos los días para detectar qué productos caducan hoy o en los próximos 3 días?
¿Qué acciones de negocio tomarías con esos productos a punto de caducar para no perder el dinero?

Datos:
1. El nombre del producto
2. El Id
3. Fecha de caducidad
4. Cantidad de Productos por id

2- Paso Lógico Inventario
1. Revisar fecha actual
2. Abrir libreta de inventario
3. Revisar primera entrada
5. Verificar fecha de caducidad del producto
6. Si fecha de caducidad menor o iagual a 14 días, producto proximo a caducar
7. Agragar a lista de productos próximos a caducar
8. En caso de que la fecha de caducidad se amyor a 14 dias, pasar al siguiente producto
9. Repetir la acción

Acción de Negocio:
1. Los productos próximos a caducar, ubicarlos en una seccion del super de productos proximo a caducar y aplicar descuento

Pyton:
productos_proximo_caducar = []
if producto:
    if (fecha_caducidad - Fecha_actual) <= 14:
        producto_proximo_caducar.add(producto)
    else:
        continue










Aprendizaje:
* Datos completos = La materia prima.
* Bucle = El motor que automatiza el trabajo aburrido.
* Condición = El cerebro que toma decisiones en cada paso.
* Estructura de Datos (Lista) = La caja donde guardas el resultado de valor.