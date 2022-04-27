import pandas as pd

notas = pd.read_csv("Student_Performance_new.csv", header = 0)
notas_mates = list(notas["math percentage"])
notas_lectura = list(notas["reading score percentage"])
notas_escritura = list(notas["writing score percentage"])

m = len(notas_mates)

for i in range (1,m):
  diccionario = {"notas_mates":notas_mates, "notas_lectura":notas_lectura, "notas_escritura":notas_escritura}
  print(1)

print("— CANTIDAD DE OBSERVACIONES --") 
n = caracteristica.count() 
print("Cantidad de observaciones = " + str(n)) 

print ("VALORES MÍNIMOS")  
valoresOrdenados = caracteristica.sort_values()    
print("Valor mínimo: "+str(valoresOrdenados [0]))  
  
print ("VALORES MÁXIMOS")  
valoresOrdenados = caracteristica.sort_values()  
print("Valor máximo: " +  
str(valoresOrdenados[len(valoresOrdenados)-1])) 