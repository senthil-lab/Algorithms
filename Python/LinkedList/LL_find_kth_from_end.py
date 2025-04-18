class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
def find_kth_from_end(ll, k):
    
    kthNode = ll.head
    temp = ll.head
    
    for i in range(k):
        print(i)
        if kthNode is not None:
            kthNode = kthNode.next
        else:
            return None
        
    while kthNode is not None:
        temp = temp.next
        kthNode = kthNode.next

    return temp

my_linked_list = LinkedList(1)
# my_linked_list.head = None
# my_linked_list.tail = None

my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)


k = 0
result = find_kth_from_end(my_linked_list, k)

print(result)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

