# Pilha
# LIFO

class No:
  def __init__(self, valor = None) -> None:
    self.valor = valor
    self.anterior = None
    pass

class Pilha:  
  def __init__(self) -> None:
    self.topo = None
    pass
  
  # Mostra o elemento do topo da pilha sem remover
  def top(self):
    return self.topo
  
  # Remove o elemento do topo da pilha
  def pop(self):
    if self.topo != None:
      temp = self.topo
      self.topo = self.topo.anterior
      return temp
    
  def push(self, no):
    if no != None and isinstance(no, No):
      no.anterior = self.topo
      self.topo = no
      
def mostrar_pilha(no):
  if no == None:
    print('---')
    return
  else:
    print(no.valor)
    mostrar_pilha(no.anterior)
    
if __name__ == '__main__':
  pilha = Pilha()
  mostrar_pilha(pilha.top())
  pilha.push(No(1))
  mostrar_pilha(pilha.top())
  pilha.push(No(2))
  mostrar_pilha(pilha.top())
  pilha.push(No(3))
  mostrar_pilha(pilha.top())
  pilha.push(No(4))
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())
  pilha.pop()
  mostrar_pilha(pilha.top())