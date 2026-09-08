"""
Visualizando la diferencia
Antes de comenzar a ejecutar pruebas de hipótesis, es una gran idea realizar un análisis de datos exploratorio; es decir, calcular estadísticas resumidas y visualizar distribuciones.

Aquí, verá la proporción de votos a nivel de condado para el candidato demócrata en 2012 y 2016 sample_dem_data. Dado que los condados son los mismos en ambos años, estas muestras están emparejadas. Las columnas que contienen las muestras son dem_percent_12 y dem_percent_16.

dem_votes_potus_12_16 está disponible como sample_dem_data. pandas y matplotlib.pyplot están cargados de sus alias habituales.
"""
# Calculate the differences from 2012 to 2016
sample_dem_data['diff'] = sample_dem_data['dem_percent_12'] - sample_dem_data['dem_percent_16']

# Find the mean of the diff column
xbar_diff = sample_dem_data['diff'].mean()

# Find the standard deviation of the diff column
s_diff = sample_dem_data['diff'].std()

# Plot a histogram of diff with 20 bins
sample_dem_data['diff'].hist(bins =20)
plt.show()


# Usando ttest()

"""
Calcular manualmente las estadísticas de las pruebas y transformarlas con un CDF para obtener un valor p es un gran esfuerzo comparar dos medias muestrales. La comparación de dos medias muestrales se denomina prueba t y pingouin El paquete Python tiene un .ttest() método para lograrlo. Este método proporciona cierta flexibilidad en la forma en que realiza la prueba.

Como en el ejercicio anterior, explorará la diferencia entre la proporción de votos a nivel de condado para el candidato demócrata en 2012 y 2016 para identificar si la diferencia es significativa. Las hipótesis son las siguientes:

: La proporción de votos democráticos en 2012 y 2016 fue la misma. 
: La proporción de votos democráticos en 2012 y 2016 fue diferente.

sample_dem_data está disponible y tiene las columnas diferencia, dem_percent_12, și dem_percent_16 además del estado y condado nombres. pingouin y ha sido cargado junto con pandas como pd.
"""

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], 
                              y=0, 
                              alternative="two-sided")

# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'], 
                                     y=sample_dem_data['dem_percent_16'], 
                                     paired=True, 
                                     alternative="two-sided")



                              
# Print the paired test results
print(paired_test_results)