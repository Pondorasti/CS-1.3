
class LinkedList:
  class Node:
    def __init__(self, data, node):
      self.data = data
      self.next = node

  def __init__(self):
    self.head = None
    self.tail = None

  
  def prepend(self, data):
    # TODO: handle tail
    self.head = self.Node(data, self.head)
     

  def __str__(self):
    ans = ""
    node = self.head
    while node:
      ans += f"{node.data} -> "
      node = node.next
    
    return ans