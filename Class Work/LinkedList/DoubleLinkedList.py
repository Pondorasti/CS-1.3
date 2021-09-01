class DoubleLinkedList:
  
  class Node:
    def __init__(self, data, prev, next):
      self.data = data
      self.prev = prev
      self.next = next

    def __str__(self):
      return f"""Node
  -> data: {self.data}
  -> prev: {self.prev.data if self.prev else None}
  -> next: {self.next.data if self.next else None}
      """
  
  def __init__(self):
    self.head = None
    pass

  def insert(self, data, afterNode):
    '''Insert a new node based on the `data` attribute after the node `afterNode`'''
    # Add new head
    if afterNode is None and self.head is None:
      self.head = self.Node(data, None, None)
      return self.head
    
    # exit early 
    if afterNode is None:
      return None


    newNode = self.Node(data, afterNode, afterNode.next)

    if afterNode.next: # check if it's an end of the list node
      afterNode.next.prev = newNode
    afterNode.next = newNode

    return newNode

  def find(self, data):
    '''Find if a node exists based on the `data` attribute. If it exists it returns the node itself, otherwise None'''
    currentNode = self.head

    while currentNode:
      if currentNode.data is data:
        return currentNode

      currentNode = currentNode.next

    return None

  def remove(self, nodeToDelete):
    '''Remove the provided node. On success it returns the deleted node, otherwise `None`'''
    if nodeToDelete is None:
      return None
    
    if nodeToDelete.prev:
      nodeToDelete.prev.next = nodeToDelete.next
    if nodeToDelete.next:
      nodeToDelete.next.prev = nodeToDelete.prev

    if nodeToDelete is self.head:
      self.head = nodeToDelete.next

    return nodeToDelete
    
  
  def update(self, nodeToUpdate, newData):
    '''Remove the provided node. On success it returns the deleted node, otherwise `None`'''
    if nodeToUpdate is None:
      return None

    nodeToUpdate.data = newData
    return nodeToUpdate
    

  def __str__(self):
    ans = ""
    currentNode = self.head
    while currentNode:
      ans += f"{currentNode.data} -> "
      currentNode = currentNode.next
    
    return ans


  


  