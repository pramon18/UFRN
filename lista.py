# Lista Encadeada Simples
# Encadeamento em só uma direção

class Node:
  def __init__(self, value = None) -> None:
    self.value = value
    self.next = None
    pass
  
class List:
  def __init__(self, head = None) -> None:
    self.head = head
    pass
  
  def list_head(self):
    return self.head
  
  def push(self, node):
    if node != None and isinstance(node, Node):
      if self.head == None:
        self.head = node
      else:
        node.next = self.head
        self.head = node
    pass
  
def mostrar_lista(node):
  if(node == None):
    return

  if(isinstance(node, Node)):
    print(node.value)
    mostrar_lista(node.next)
  pass

if __name__ == '__main__':
  list = List()
  mostrar_lista(list.list_head())
  list.push(Node(1))
  mostrar_lista(list.list_head())
  list.push(Node(2))
  mostrar_lista(list.list_head())
  list.push(Node(3))
  mostrar_lista(list.list_head())
  list.push(Node(4))
  mostrar_lista(list.list_head())