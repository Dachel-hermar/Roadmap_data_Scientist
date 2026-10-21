"""
Estadística de prueba media de dos muestras
La prueba de hipótesis para determinar si existe una diferencia entre las medias de dos poblaciones utiliza un tipo diferente de estadística de prueba para las puntuaciones z que vio en el Capítulo 1. Se llama "t" y se puede calcular a partir de tres valores de cada muestra utilizando esta ecuación.

Mientras intenta determinar por qué algunos envíos llegan tarde, es posible que se pregunte si el peso de los envíos que llegaron a tiempo es menos de el peso de los envíos que llegaron tarde. El envíos_tardíos el conjunto de datos se ha dividido en un grupo "sí", donde tarde == "Sí" y un grupo "no" donde tarde == "No". El peso del envío se indica en el peso_kilogramos variable.

Las medias muestrales para los dos grupos están disponibles como xbar_no y xbar_sí. Las desviaciones estándar de la muestra son s_no y s_sí. Los tamaños de muestra son n_no y n_sí. numpy también se carga como np.
"""
# Calculate the numerator of the test statistic
numerator = xbar_yes- xbar_no

# Calculate the denominator of the test statistic
denominator = np.sqrt(s_no ** 2 / n_no + s_yes ** 2 / n_yes)

# Calculate the test statistic
t_stat = numerator/denominator

# Print the test statistic
print(t_stat)

