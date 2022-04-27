import pandas as pd

notas = pd.read_csv("Student_Performance_new.csv", header = 0)
notas_mates = list(notas["math percentage"])
notas_lectura = list(notas["reading score percentage"])
notas_escritura = list(notas["writing score percentage"])

m = len(notas_mates)