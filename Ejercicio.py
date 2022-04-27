def calculoMediana(caracteristica):  
   mediana = 0  
   caracteristica = caracteristica.sort_values()  
   caracteristica = caracteristica.reset_index(drop=True)  
   n = self. caracteristica.count()  
   par = False;  
   if (n % 2 == 0):  
       print("La cantidad de observaciones es par.")  
       par = True  
  
   if par:  
       rango = (n / 2); 
       rangoPython = rango-1 
       valor1 = caracteristica[rangoPython]  
       valor2 = caracteristica[rangoPython+1]  
       mediana = valor1 +((valor2-valor1)/2)  
   else:  
       rango = ((n + 1) / 2)  
       rangoPython = rango - 1  
       mediana = caracteristica [rangoPython]  
  
   return mediana 