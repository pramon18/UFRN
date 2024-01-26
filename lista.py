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
  
  def push(self, node):
    if node != None and isinstance(node, Node):
      if self.head == None:
        self.head = node
      else:
        node.next = self.head
        self.head = node