# Bubble Sort
lista = [5,3,2,1,5,7,9]

for i in range(len(lista)):
  for j in range(len(lista)):
    print(lista[j])
    print(lista[i] > lista[j])
    if(lista[i] < lista[j]):
        aux = lista[j]
        lista[j] = lista[i]
        lista[i] = aux
      
  print("---------------")  
print(lista)