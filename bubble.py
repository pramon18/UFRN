# Bubble Sort
lista = [5,3,2,1,5,7,9]

for i in range(len(lista)):
  for j in range(len(lista)-1):
    print(lista[j])
    print(lista[j + 1])
    print(lista[j] > lista[j + 1])
    if(lista[j] > lista[j + 1]):
        aux = lista[j]
        lista[j] = lista[j + 1]
        lista[j + 1] = aux
      
  print("---------------")  
print(lista)