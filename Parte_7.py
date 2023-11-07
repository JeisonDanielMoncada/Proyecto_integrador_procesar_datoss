import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('heart_failure_clear.csv')

# Se grafica histograma por edad donde podemos osbervar la cantidad de pacientes y su edad
Edades = df['age']
# aunque al calcular el bins con la raiz cuadrada de la materia nos da 9 con 10 nos da la grafica solicitada
plt.hist(Edades, bins=10,edgecolor='black')
plt.title('Distribucion de Edades')
plt.xlabel('Edades')
plt.ylabel('Cantidad de personas')

plt.show()



# Definir los datos de los hombre y mujeres que son anemmicos, diabeticos, fumadores y muertos
df_anaemia = df.groupby("sex")["anaemia"].sum()
df_diabetes = df.groupby("sex")["diabetes"].sum()
df_smoking = df.groupby("sex")["smoking"].sum()
df_dead = df.groupby("sex")["DEATH_EVENT"].sum()

print(df_anaemia)
print(df_diabetes)
print(df_smoking)
print(df_dead)
df_total_hom= [df_anaemia[1],df_diabetes[1],df_smoking[1], df_dead[1]]
df_total_muje = [df_anaemia[0],df_diabetes[0],df_smoking[0], df_dead[0]]
# # Definir las etiquetas del eje x
etiquetas = ["Anemicos", "Diabéticos", "Fumadores", "Muertos"]

# # Definir el ancho de las barras
ancho = 0.4

# # Crear el gráfico de barras
plt.bar(etiquetas, df_total_hom, width=-ancho, align='edge', label='Hombres')
plt.bar(etiquetas, df_total_muje,width=ancho, align='edge', label='Mujeres')


# # Añadir la leyenda
plt.legend()
plt.title('Histograma Agrupado por Sexo')
plt.xlabel('Categorias')
plt.ylabel('Cantidad')

# # Mostrar el gráfico
plt.show()
