import matplotlib.pyplot as plt


df_anaemia = df.groupby('anaemia').size()
df_diabetes = df.groupby("diabetes").size()
df_smoking = df.groupby("smoking").size()
df_dead = df.groupby("DEATH_EVENT").size()


# Creamos una figura con una cuadrícula de 2x2
plt.subplot(1, 4, 1)
categorias_1 = ['Si', 'No']
valores_1 = [df_anaemia[1],df_anaemia[0]]
plt.pie(valores_1, labels=categorias_1,autopct="%.1f%%")
plt.title("Anemia")

plt.subplot(1, 4, 2)
categorias_2 = ['Si', 'No']
valores_2 = [df_diabetes[1],df_diabetes[0]]
plt.pie(valores_2, labels=categorias_2,autopct="%.1f%%")
plt.title("Diabeticos")

plt.subplot(1, 4, 3)
categorias_3 = ['Si', 'No']
valores_3 = [df_smoking[1],df_smoking[0]]
plt.pie(valores_3, labels=categorias_3,autopct="%.1f%%")
plt.title("Fumadores")

plt.subplot(1, 4, 4)
categorias_4 = ['Si', 'No']
valores_4 = [df_dead[1],df_dead[0]]
plt.pie(valores_4, labels=categorias_4,autopct="%.1f%%")
plt.title("Muertos")

# Ajustar los espacios entre los subgráficos
plt.tight_layout()

# Mostrar la figura con los subgráficos
plt.show()