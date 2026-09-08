"""
De t a p
Anteriormente, calculó la estadística de prueba para el problema de dos muestras de si el peso medio de los envíos es menor para los envíos que no llegaron tarde (tarde == "No") en comparación con los envíos que llegaron tarde (tarde == "Sí"). Para tomar decisiones al respecto, es necesario transformar el estadístico de prueba con una función de distribución acumulativa para obtener un valor p.

Recordemos las hipótesis:

: El peso medio de los envíos que no llegaron tarde es el mismo que el peso medio de los envíos que llegaron tarde.

: El peso medio de los envíos que no llegaron tarde es menor que el peso medio de los envíos que llegaron tarde.

Statistica testului, t_stat, está disponible, al igual que los tamaños de muestra para cada grupo, n_no y n_sí. Utilice un nivel de significancia de alfa = 0,05.

t también ha sido importado de scipy.stats.
"""

# Calculate the degrees of freedom
degrees_of_freedom = (n_yes + n_no) - 2

# Calculate the p-value from the test stat
p_value = t.cdf(t_stat, df=degrees_of_freedom)

# Print the p_value
print(p_value)