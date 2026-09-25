"""
RETO 12: Arquitectura de Módulos (import)

Contexto de Negocio:
Un proyecto real de Data Science nunca vive en un solo archivo. 
Se divide en "Módulos" (archivos separados). Para conectarlos usamos la palabra reservada `import`.

Tu Misión:
He creado para ti un archivo llamado `matematicas.py` en esta misma carpeta.
Ese archivo tiene dos funciones: `sumar_impuesto(monto)` y `aplicar_descuento(monto, descuento)`.

1. Importación:
   - En la línea de abajo, escribe: `from matematicas import sumar_impuesto, aplicar_descuento`
2. Uso:
   - Imprime el resultado de usar `sumar_impuesto(100)`.
   - Imprime el resultado de usar `aplicar_descuento(100, 0.50)`.
"""

# ==========================================
# 1. LA IMPORTACIÓN (Conectando los archivos)
# ==========================================
# Importa aquí abajo...

from matematicas import sumar_impuesto, aplicar_descuento
print(sumar_impuesto(50))
print(aplicar_descuento(100, 0.50))

# ==========================================
# 2. EL USO (Ejecutando la lógica externa)
# ==========================================
# Usa las funciones importadas aquí abajo...

