class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index , end_index ):
        if self.head:
            if start_index < 0 and end_index > self.length-1:
                return None
            dummy = Node(0)
            dummy.next = self.head
            current = self.head
            before = dummy
            after = current.next
            start_before = None
            # start_current = None
            print(f"range({end_index+1})",range(end_index+1))
            for i in range(end_index+1):
                print("i:",i)
                if i == start_index:
                    print("i == start_index", i == start_index)
                    start_before = before
                    # start_current = current
                if i == end_index:
                    print("i == end_index", i == end_index)
                    current.next = before
                    start_before.next.next = after
                    start_before.next = current
                    self.head = dummy.next
                    break
                if i > start_index and i < end_index:
                    current.next = before
                before = current
                current = after
                # if after:
                after = after.next
        
                
        


    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# print("Original linked list: ")
# linked_list.print_list()

print("Reversed sublist (2, 4): ")
# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)

linked_list.print_list()

print("Reversed entire linked list: ")
# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)

linked_list.print_list()

# print("Reversed sublist of length 1 (3, 3): ")
# # Reverse a sublist of length 1 within the linked list
# linked_list.reverse_between(3, 3)

# linked_list.print_list()

# # Reverse an empty linked list
# empty_list = LinkedList(0)
# empty_list.make_empty()
# empty_list.reverse_between(0, 0)
# print("Reversed empty linked list: ")
# empty_list.print_list()

# print("Reversed sublist of length 2 (0, 1): ")
# # Reverse a sublist of length 1 within the linked list
# linked_list.reverse_between(0, 1)

# linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    Reversed sublist of length 2 (0, 1):
    4
    3
    5
    2
    1
    
"""
