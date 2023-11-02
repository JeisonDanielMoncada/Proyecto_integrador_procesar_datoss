import pandas as pd
import numpy as np

df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
def limp(df : pd.DataFrame) -> pd.DataFrame:
    # vamos a buscar duplicados en dataFrame
    dup = df.duplicated().sum()
    if dup < 0 :
        df = df.drop_duplicates()
    # buscamos columna por columna si hay valores faltantes
    for n in (df.isna().any()):
        # si hay valores falantes solo seleccionamos las columnas que les faltan valores
        # y agremos en esos espacion la media de la columna ya que solo estamos trabajando con valores 
        # numericos
        if n == True :
            k= df.isna().any()
            columns=k.index
            h= columns[k]
            mean_age = df[h].mean()
            df[h] = df[h].fillna(mean_age)
    # creamos una fucion llama iqr_c que utiliza los intercuartiles para eliminar valores atipicos
    def iqr_c(Colum : pd.DataFrame) -> None:
        Q1 = Colum.quantile(0.25)
        Q3 = Colum.quantile(0.75)
        IQR = Q3-Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_cleaned = df[(Colum >= lower_bound) & (Colum <= upper_bound)]
        return df_cleaned
    # utilizamos la fucion en cada columna
    for n in (df.isna()):
        df = iqr_c(df[n])
    # creamos la nueva columna por rango de edad
    def categorize_age(x): 
        if x <= 12: return 'Niño'
        elif x <= 19: return 'Adolescente' 
        elif x <= 39: return 'Joven adulto'
        elif x <= 59: return 'Adulto'
        else: return 'Adulto mayor';
    df['age_group'] = df['age'].apply(categorize_age)
    df.to_csv("heart_failure_clear.csv", index=False)
    return df
limp(df)
