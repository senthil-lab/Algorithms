class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return True
        temp = self.head
        self.head = temp.next
        while temp and temp.next:
            # print(temp.value,"<->", temp.next.value)
            # print(temp.prev)
            # print(temp.next.prev.value)
            # print(temp.next.value)
            # print(temp.next.next.value)
            # print(temp.next.value, temp.prev, temp.next.next.value, temp.value)
            if temp.prev:
                temp.prev.next = temp.next
            temp_prev = temp.prev
            #     print("temp_prev.value:", temp_prev.value)
            # else:
            #     print("temp_prev:", temp_prev)
            temp.prev = temp.next
            # temp.prev,temp.next.prev,temp.next,temp.next.next = temp.next,temp.prev,temp.next.next,temp
            # print("temp.value:",temp.value)
            # print(temp.prev.value,temp.next.prev,temp.next.value,temp.next.next.value)
            # print("temp.prev.value", temp.prev.value)
            temp.next.prev = temp_prev
            # print("temp.next.prev", temp.next.prev)
            temp_next = temp.next
            temp.next = temp.next.next
            # print("temp.next.value", temp.next.value)
            temp_next.next = temp
            # print("temp.next.next.value", temp.next.value)
            # print(temp.value,"<->", temp.next.value)
            # print(self.head.value,"<->", self.head.next.value, "<->", self.head.next.next.value)
            # # break
            # print("temp.value", temp.value)
            if temp.next:
                temp.next.prev = temp
            temp = temp.next
        return True
        


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""