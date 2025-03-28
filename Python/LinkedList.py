class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
        return True

    def prepend(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1
        return True


    def pop(self):
        lastItem = None
        if self.length == 0:
            return None
        lastItem = self.tail
        if self.length == 1:
            self.make_empty()
            return lastItem
        else:
            temp = self.head
            while temp.next is not None:
                lastTemp = temp
                temp = temp.next
            self.tail = lastTemp
            lastTemp.next = None
            self.length -= 1
            return lastItem

# myLinkedList = LinkedList(4)

# myLinkedList = LinkedList(1)
# myLinkedList.make_empty()

# print('Appending item:', 2)
# myLinkedList.append(2)

# print('Appending item:', 3)
# myLinkedList.append(3)

# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')

# print('Linked List:')
# myLinkedList.print_list()

# print('Poped item:', myLinkedList.pop(), '\n')

# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')

# print('Linked List:')
# myLinkedList.print_list()

# print('Poped item:', myLinkedList.pop(), '\n')

# # print('Head:', myLinkedList.head.value)
# # print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')

# print('Linked List:')
# myLinkedList.print_list()

# print('Poped item:', myLinkedList.pop(), '\n')

# # print('Head:', myLinkedList.head.value)
# # print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')

# print('Linked List:')
# myLinkedList.print_list()

# print('Appending item:', 4)
# myLinkedList.append(4)

# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')

# print('Linked List:')
# myLinkedList.print_list()

# checking prepend
myLinkedList = LinkedList(2)

print('Appending item:', 3)
myLinkedList.append(3)

myLinkedList.print_list()

print('prepending item:', 1)
myLinkedList.prepend(1)

myLinkedList.print_list()



