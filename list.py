# Lista Encadeada Simples (List)
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
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    pass
  
  def is_empty(self):
    return self.head == None
  
  def list_head(self):
    return self.head
  
  def list_tail(self):
    return self.tail
  
  def find(self, id):
    if self.is_empty():
      return None
    
    node = self.head
    while node != None:
      if node.id == id:
        return node
      node = node.next
    return None
  
  def push(self, node):
    if isinstance(node, Node):
      if self.is_empty():        
          self.head = node
          self.tail = node
          return
      self.tail.next = node
      self.tail = node
    pass
  
  def remove(self, id):
    if self.is_empty():
      print("Lista Vazia... :(")
      return
    
    node = self.find(id)
    print(node)
    if node == None:
      print("Item não existe na lista... :(")
      return
    
    # Node está na cabeça
    if node == self.head:
      self.head = self.head.next
      node.next = None
      return
      
    # Node está na cauda
    if node == self.tail:
      temp = self.head
      while temp.next != node:
        temp = temp.next
        pass 
      temp.next = None
      return
    
    # Node está no meio da lista
    temp = self.head
    while temp.next != node:
      temp = temp.next
      pass
    temp.next = node.next
    node.next = None
    pass
        
  
  def print_list(self):
    if self.is_empty():
      print("Lista Vazia... :(")
      return

    terminator = 0
    node = self.head
    while node != None:
      print(node)
      node = node.next
      terminator = len(str(node)) if len(str(node)) > terminator else terminator
    print(terminator * "-")
    pass

if __name__ == '__main__':
  list = List()
  list.print_list()
  list.push(Node(1, "João"))
  list.print_list()
  list.push(Node(2, "Maria"))
  list.print_list()
  list.push(Node(3, "José"))
  list.print_list()
  list.push(Node(4, "Outro"))
  list.print_list()
  print(list.find(3))
  print(list.find(99))
  list.remove(1)
  list.remove(3)
  list.remove(2)
  list.remove(4)
  list.print_list()
  list.print_list()