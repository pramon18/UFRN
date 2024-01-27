# Lista Encadeada Simples
# Encadeamento em só uma direção

class Node:
  def __init__(self, id = None, data = None) -> None:
    self.id = id
    self.data = data
    self.next = None
    pass
  
  def __str__(self) -> str:
    return str(self.id) + " " + str(self.data)
  
class List:
  def __init__(self, head = None) -> None:
    self.head = head
    pass
  
  def is_empty(self):
    return self.head == None
  
  def list_head(self):
    return self.head
  
  def list_tail(self):
    if self.is_empty(): 
      return None
    
    node = self.head
    while node.next != None:
      node = node.next
    return node
  
  def push(self, node):
    if isinstance(node, Node):
      if self.is_empty():        
          self.head = node
          return
      tail = self.list_tail()
      tail.next = node    
    pass
  
  def mostrar_lista(self):
    if self.is_empty():
      print("Lista Vazia... :(")
      return

    node = self.head
    while node != None:
      print(node)
      node = node.next
    print("-" * 7)
    pass

if __name__ == '__main__':
  list = List()
  list.mostrar_lista()
  list.push(Node(1, "João"))
  list.mostrar_lista()
  list.push(Node(2, "Maria"))
  list.mostrar_lista()
  list.push(Node(3, "José"))
  list.mostrar_lista()
  list.push(Node(4, "Outro"))
  list.mostrar_lista()