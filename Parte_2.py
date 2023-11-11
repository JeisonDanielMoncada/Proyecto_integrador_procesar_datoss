import pandas as pd

import numpy as np

from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edad = data["age"]

promedio_edad = np.mean(edad)

df = pd.DataFrame(data)

df_dead = df[df["is_dead"] == 1]
df_alive = df[df["is_dead"] == 0]

mean_age_dead = df_dead["age"].mean()
mean_age_alive = df_alive["age"].mean()


