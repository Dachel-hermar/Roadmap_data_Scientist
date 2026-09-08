"""
Calcular un intervalo de confianza
Si da una estimación única de una estadística de muestra, es probable que se equivoque en cierta medida. 

Por ejemplo, la proporción hipotética de envíos tardíos fue del 6%. 
Incluso si la evidencia sugiere la hipótesis nula de que la proporción de envíos tardíos es igual a esto, 
para cualquier muestra nueva de envíos, es probable que la proporción sea un poco diferente debido a la variabilidad del muestreo. 
En consecuencia, es una buena idea indicar un intervalo de confianza. 
Es decir, "estamos 95% 'confiados' en que la proporción de envíos retrasados está entre A y B" (para algún valor de A y B).

Muestreo en Python demostrado dos métodos para calcular intervalos de confianza. 
Aquí, utilizará cuantiles de la distribución bootstrap para calcular el intervalo de confianza.

late_prop_samp y late_shipments_boot_distn sunt disponibile; pandas y numpy están cargados de sus alias habituales.
"""
import numpy as np
# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))
