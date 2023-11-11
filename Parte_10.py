import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



data= pd.read_csv('heart_failure_clear.csv')

Z= data
Z= (Z.drop(['DEATH_EVENT', 'age', 'age_group'], axis = 1))
X= Z[['anaemia','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','sex','smoking']]

y = data['age']

d = np.corrcoef(X)
print(len(X))
print(len(y))


regression = LinearRegression()

# #     # Ajustar el modelo a los datos
regression.fit(X, y)

new_X = X
predicciones = regression.predict(new_X)
print("Predicciones:", predicciones)

y_pred = regression.predict(X)

mse = mean_squared_error(y, y_pred)
print("Error cuadrático medio (MSE):", mse)
r_squared = regression.score(X, y)
print("Coeficiente de determinación (R²):", r_squared)

# La predicion que se obtiene no es la mas adeacada vamos a intentar retirando algunas variables que componen
# a X

Z= data
Z= (Z.drop(['sex','smoking','time','DEATH_EVENT', 'age', 'age_group'], axis = 1))
X = Z[['anaemia','diabetes','creatinine_phosphokinase','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium']]

y = (data['age'])


regression = LinearRegression()

# #     # Ajustar el modelo a los datos
regression.fit(X, y)

new_X = X
predicciones = regression.predict(new_X)
print("Predicciones:", predicciones)

y_pred = regression.predict(X)

mse = mean_squared_error(y, y_pred)
print("Error cuadrático medio (MSE):", mse)
r_squared = regression.score(X, y)
print("Coeficiente de determinación (R²):", r_squared)

# Despues de realizar validacion retirando algunas variables de X, no observamos algun cambio en nuestra
# prediccion, es posible que los datos de nuestra dataset no sean los mas adecuados para predecir la edad 
# del paciente.