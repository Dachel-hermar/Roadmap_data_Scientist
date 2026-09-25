# 📖 Manifiesto de Clean Code y Buenas Prácticas

Este documento es un archivo vivo. Aquí iré anotando todas las reglas de oro, convenciones de la industria y estándares de arquitectura que voy aprendiendo en mi Roadmap. El objetivo no es solo que mi código funcione, sino que sea profesional, optimizado y legible para otros ingenieros.

---

## 1. Nomenclatura de Bucles (La Regla "Singular in Plural")
**La Regla:** Al crear un bucle `for` para leer listas o bases de datos, **NUNCA** se debe usar el mismo nombre para la variable que itera y para la lista original. Se debe usar estrictamente el formato Singular en Plural.
**El Peligro (Colisión de Memoria):** Escribir `for clientes in clientes:` es una trampa mortal. Python permite que el bucle corra, pero sobreescribe y destruye la lista original en la memoria, reemplazándola únicamente por el último dato que leyó.
**La Solución Profesional:**
```python
# MALA PRÁCTICA (Destruye datos)
for facturas in facturas:
    print(facturas)

# BUENA PRÁCTICA (Mantiene los datos a salvo)
for factura in facturas:
for cliente in base_clientes:
for producto in inventario:
```

---

## 2. El Bug Fantasma y el Hábito QA
**La Regla:** El hecho de que la consola te dé la respuesta correcta en el primer intento no significa que tu arquitectura funcione. Siempre debes ponerte el sombrero de QA Tester y alterar los datos para forzar los "Edge Cases".
**El Peligro:** Olvidar un `else` o dejar un código mal indentado a la izquierda. Esto provoca que la máquina ejecute el comando de forma **incondicional**, saltándose todas tus reglas de negocio y corrompiendo la lógica.

---

## 3. Programación Defensiva (El Guardia de Seguridad)
**La Regla:** Al diseñar una Función (`def`), los filtros de seguridad (ej. validar que un dato no sea texto si se espera un número) siempre van al principio del código como condicionales.
**El Peligro:** Si la lógica vulnerable corre antes que la verificación, la función explotará fatalmente. Si el dato de entrada está corrupto, la función debe abortar usando `return` inmediatamente ("Garbage in, garbage out").

---

## 4. El Botón de Suicidio (Identación del Return)
**La Regla:** El comando `return` asesina la función y expulsa el dato inmediatamente.
**El Peligro:** Si colocas un `return` con una sangría incorrecta (indentado ADENTRO de un bucle `for` o `while`), el bucle se ejecutará exactamente una vez y luego se autodestruirá, dejándote con la ilusión de que tus datos desaparecieron mágicamente.

---

## 5. Mutabilidad vs Reasignación (Operaciones CRUD)
**La Regla:** Los métodos nativos de colecciones de datos (ej. `lista.pop()`, `lista.remove()`, `lista.insert()`) mutan el objeto en tiempo real y en su misma celda de memoria (In-Place).
**El Peligro:** No debes intentar reasignarlos a una variable (`lista = lista.remove()`), porque esos comandos destruyen o alteran la lista pero devuelven `None`. En cambio, métodos de textos inmutables como `.strip()` SÍ requieren reasignación.

---

## 6. Bucles Infinitos y el Asesino Zombi (while True)
**La Regla:** El patrón `while True:` es legítimo para mantener un sistema vivo (menús interactivos), pero SIEMPRE requiere un disparador de emergencia `break` programado en su interior.
**El Entorno:** Si un bucle infinito falla o se bloquea, el editor (IDE) te dejará atrapado en un proceso zombi en segundo plano. La herramienta definitiva del Arquitecto para asesinar el proceso es `Ctrl + C` en la terminal.

---

*(Más reglas se irán añadiendo conforme se avance en el Roadmap...)*
