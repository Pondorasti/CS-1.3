from LinkedList import LinkedList 
from DoubleLinkedList import DoubleLinkedList


ll = LinkedList()

ll.prepend(7)
ll.prepend(14)
ll.prepend(100)

print(ll)


dll = DoubleLinkedList()

dll.insert(3, None)
print(dll)

dllHead = dll.find(3)
print(dllHead)

dll.insert(5, dllHead)
dll.insert(7, dllHead)
dll.insert(9, dllHead)
print(dll)


deletedNode = dll.remove(dllHead)
# print(deletedNode)

print(dll)
# print(dll.find(9))

updatedNode = dll.update(dll.find(9), "Ahmed")
print(dll)
print(updatedNode)

L1=[1,2,3,4,5]
print (L1[-2])