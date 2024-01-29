# Pilha (Stack)
# LIFO

class Node:
  def __init__(self, id = None, value = None) -> None:
    self.id = id
    self.value = value
    self.previous = None
    pass

  def __str__(self) -> str:
    return str(self.id) + " " + str(self.value)

class Stack:  
  def __init__(self) -> None:
    self.top = None
    pass
  
  # Mostra o elemento do topo da pilha sem remover
  def stack_top(self):
    return self.top
  
  # Verifica pilha vazia
  def is_empty(self):
    return self.top == None

  # Remove o elemento do topo da pilha
  def pop(self):
    if not self.is_empty():
      temp = self.top
      self.top = self.top.previous
      return temp
    
  def push(self, node):
    if isinstance(node, Node):
      if self.is_empty():
        self.top = node
        return
            
      node.previous = self.top
      self.top = node        
      
  def print_stack(self):
    if self.is_empty(): 
      print("The stack is empty... :(")
      return
    
    terminator = 0    
    node = self.top
    while node != None:
      print(node)
      node = node.previous
      terminator = len(str(node)) if len(str(node)) > terminator else terminator
    print(terminator*"-")
    pass
    
if __name__ == '__main__':
  pilha = Stack()
  pilha.print_stack()
  pilha.push(Node(1, "João"))
  pilha.print_stack()
  pilha.push(Node(2, "Maria"))
  pilha.print_stack()
  pilha.push(Node(3, "José"))
  pilha.print_stack()
  pilha.push(Node(4, "Pedro"))
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()
  pilha.pop()
  pilha.print_stack()