import plotly.graph_objects as go
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

df = pd.read_csv('heart_failure_clear.csv')

X = df.drop(columns=["DEATH_EVENT", "age_group"]).values
y = df["DEATH_EVENT"].values

X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(X)

fig = px.scatter_3d(
    x=X_embedded[:, 0],
    y=X_embedded[:, 1],
    z=X_embedded[:, 2],
    color=y,
    labels={
        "x": "Componente 1",
        "y": "Componente 2",
        "z": "Componente 3",
        "color": "DEATH_EVENT"
    }
)
   
# Mostrar la gráfica
fig.show()