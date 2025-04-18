class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def reverse_print_list(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None
        temp = self.tail
        if self.length == 1:
            self.make_empty()
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def pop_first(self):
        if not self.head:
            return None
        temp = self.head
        if self.length == 1:
            self.make_empty()
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
        return temp
    
    def get(self, index):
        if not self.head:
            return None
        if (index < 0 or index >= self.length):
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-index-1):
                temp = temp.prev
        return temp
       
# without using get method
    # def set_index(self, index, value):
    #     if not self.head or (index < 0 and index >= self.length):
    #         return False
    #     temp = self.head
    #     if index < self.length/2:
    #         for _ in range(index):
    #             temp = temp.next
    #     else:
    #         temp = self.tail
    #         for _ in range(self.length-index-1):
    #             temp = temp.prev
    #     temp.value = value
    #     return True

    def set_index(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        newNode = Node(value)
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp = self.get(index)
            # print(temp)
            if temp:
                newNode.prev = temp.prev
                temp.prev.next = newNode
                newNode.next = temp
                temp.prev = newNode
            else:
                self.head = newNode
                self.tail = newNode
            self.length += 1
        return True

    def remove(self, index):
        if not self.head or (index < 0 and index >= self.length):
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        
        temp = self.get(index)

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        
        self.length -= 1 
        return temp

print("creating DLL with 7")
myDLL = DoublyLinkedList(7)
print("appening 8")
myDLL.append(8)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("make empty:")
myDLL.make_empty()
print("appending 1")
myDLL.append(1)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("appending 2:")
myDLL.append(2)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("first Pop:")
print(myDLL.pop().value)
print("second Pop:")
print(myDLL.pop().value)
print("Third Pop:")
print(myDLL.pop())
print("prepend 1")
myDLL.prepend(1)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("prepend 2:")
myDLL.prepend(2)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("first pop_first:")
print(myDLL.pop_first().value)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("second pop_first:")
print(myDLL.pop_first().value)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("third pop_first:")
print(myDLL.pop_first())
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("appending 0")
myDLL.append(0)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("appending 1:")
myDLL.append(1)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("appending 2:")
myDLL.append(2)
print("original order:")
myDLL.print_list()
print("reverse order:")
myDLL.reverse_print_list()
print("getting index 1")
print(myDLL.get(1).value)
print("original order:")
myDLL.print_list()
print("getting index 0")
print(myDLL.get(0).value)
print("original order:")
myDLL.print_list()
print("getting index 1")
print(myDLL.get(1).value)
print("original order:")
myDLL.print_list()
print("getting index 2")
print(myDLL.get(2).value)
print("original order:")
myDLL.print_list()
print("setting index 2 as 4")
print(myDLL.set_index(2,4))
print("original order:")
myDLL.print_list()
print("setting index 1 as 2")
print(myDLL.set_index(1,2))
print("original order:")
myDLL.print_list()
print(myDLL.insert(1,1))
print("original order:")
myDLL.print_list()
print(myDLL.insert(3,3))
print("original order:")
myDLL.print_list()
print(myDLL.insert(0,-1))
print("original order:")
myDLL.print_list()
print("removing index 0:")
print(myDLL.remove(0).value)
print("original order:")
myDLL.print_list()
print(f"removing index {myDLL.length-1}:")
print(myDLL.remove(myDLL.length-1).value)
print("original order:")
myDLL.print_list()