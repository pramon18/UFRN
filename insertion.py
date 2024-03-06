# Insertion Sort
lista = [5,3,2,1,5,7,9]

for i in range(1, len(lista)):
  
  # eleger número a ser ordenado
  ### VERIFICAR MELHOR PORQUE ISSO FUNCIONA !!!
  number = lista[i]
  j = i - 1
  while(j >=0 and number < lista[j]):
    lista[j+1] = lista[j]
    j = j - 1
  lista[j + 1] = number
  print("---------------")  
  print(lista)
  print("---------------")  
print(lista)