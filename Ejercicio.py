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


print ("VALORES MÁXIMOS")  
valor_maximo = caracteristica.sort_values()  
print("Valor máximo: " +  
str(valoresOrdenados[len(valoresOrdenados)-1])) 

for num in notas_mates:
  if num > valor_maximo or valor_maximo == None:
  print(valor_maximo)
for num in notas_lectura:
  if num > valor_maximo or valor_maximo == None:
  print(valor_maximo)
for num in notas_escritura:
  if num > valor_maximo or valor_maximo == None:
  print(valor_maximo)

print ("VALORES MÍNIMOS")  
valor_minimo = caracteristica.sort_values()    
print("Valor mínimo: "+str(valoresOrdenados [0])) 

for num in notas_mates:
  if num < valor_minimo or valor_minimo == None:
  print(valor_minimo)
for num in notas_lectura:
  if num < valor_minimo or valor_minimo == None:
  print(valor_minimo)
for num in notas_escritura:
  if num < valor_minimo or valor_minimo == None:
  print(valor_minimo)

print("NOTAS MEDIAS") 
suma_de_las_notas_mates = sum(notas_mates)
media_notas_mates = suma_de_las_notas_mates/1
print("La nota media en mates es{}".format(media_notas_mates))

suma_de_las_notas_lectura = sum(notas_lectura)
media_notas_lectura = suma_de_las_notas_lectura/1
print("La nota media en lectura es{}".format(media_notas_lectura))

suma_de_las_notas_escritura = sum(notas_escritura)
media_notas_escritura = suma_de_las_notas_escritura/1
print("La nota media en escritura es{}".format(media_notas_escritura))

