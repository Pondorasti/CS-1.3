class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  """Implements a basic linked list"""

  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, new_data):
    

    new_node = Node(new_data)

    if self.head == None:
      self.head = new_node
      self.tail = new_node
      return

    self.tail.next = new_node
    self.tail = new_node

  def prepend(self, new_data):
    new_node = Node(new_data)

    if self.head == None:
      self.head = new_node
      self.tail = new_node
      return

    new_node.next = self.head
    self.head = new_node

  def delete_from_head(self):
    self.head = self.head.next

  def delete_from_tail(self):
    
    current = self.head
    #get the one right before the tail
    while current != None:
      if current.next == self.tail:
        break
      current = current.next
    self.tail = current
    current.next = None

  def print_list(self):
    current = self.head
    while current != None:
      print(current.data)
      current = current.next

  def length(self):
    length = 0
    current = self.head
    while current != None:
      length += 1
      current = current.next

    return length

  def find(self, key):
    current = self.head
    while current != None:
      if current.data[0] == key:
        return current.data
      current = current.next

  def update(self, key, value):
    current = self.head
    while current != None:
      if current.data[0] == key:
        current.data[1] = value
        return 
      current = current.next
  
  def delete(self, key):
    if self.head and self.head.data[0] == key:
      self.head = self.head.next
      return
      
    current = self.head

    while current != None:
      if current.next and current.next.data[0] == key:
        current.next = current.next.next
        return 
      current = current.next

  def items(self):
    items = []
    current = self.head
    while current != None:
      items.append(current.data)
      current = current.next
    return items
    

    