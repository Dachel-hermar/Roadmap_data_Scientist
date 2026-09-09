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

*(Más reglas se irán añadiendo conforme se avance en el Roadmap...)*
