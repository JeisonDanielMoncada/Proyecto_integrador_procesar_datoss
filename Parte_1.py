import numpy as np

from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edad = data["age"]

promedio_edad = np.mean(edad)


print(edad)
print(promedio_edad)