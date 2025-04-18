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
        if self.length > 0:
            lastItem = self.tail
            if self.length == 1:
                self.make_empty()
            else:
                temp = self.head
                while temp.next is not None:
                    lastTemp = temp
                    temp = temp.next
                self.tail = lastTemp
                self.length -= 1
            lastTemp.next = None
        return lastItem
        
    def pop_first(self):
        firstItem = None
        if self.length > 0:
            firstItem = self.head
            if self.length == 1:
                self.make_empty()
            else:
                self.head = firstItem.next
                self.length -= 1
            firstItem.next = None
        return firstItem
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # counter = 0
        # while temp is not None:
        #     if counter == index:
        #         return temp
        #     temp = temp.next
        #     counter += 1
        # return None        
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index-1)
        outputNode = temp.next
        temp.next = outputNode.next
        outputNode.next = None
        self.length -= 1
        return outputNode
    # if no restriction on updating length attribute
    # def reverse(self):
    #     if self.length > 1:
    #         tempLength = self.length
    #         newNode = self.pop_first()
    #         tempTail = newNode

    #         for _ in range(self.length):
    #             nextNode = self.pop_first()
    #             nextNode.next = newNode
    #             newNode = nextNode
            
    #         self.head = newNode
    #         self.tail = tempTail
    #         self.length = tempLength
    #     return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True



        






# create a LinkedList

# myLinkedList = LinkedList(4)

# testing append

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

# testing pop

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

# testing prepend

# myLinkedList = LinkedList(2)
# print('Appending item:', 3)
# myLinkedList.append(3)
# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')
# myLinkedList.print_list()
# print('prepending item:', 1)
# myLinkedList.prepend(1)
# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')
# myLinkedList.print_list()
# print(myLinkedList.head.next.next.value)

# testing pop_first
# print('creating LinkedList with node:', 1)
# myLinkedList = LinkedList(1)
# print('Appending item:', 2)
# myLinkedList.append(2)
# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')
# myLinkedList.print_list()
# print('pop first first time:')
# print('Poped item:', myLinkedList.pop_first().value, '\n')
# print('Head:', myLinkedList.head.value)
# print('Tail:', myLinkedList.tail.value)
# print('Length:', myLinkedList.length, '\n')
# myLinkedList.print_list()
# print('pop first second time:')
# print('Poped item:', myLinkedList.pop_first().value, '\n')
# print('Head:', myLinkedList.head)
# print('Tail:', myLinkedList.tail)
# print('Length:', myLinkedList.length, '\n')
# myLinkedList.print_list()
# print('pop first third time:')
# print('Poped item:', myLinkedList.pop_first(), '\n')
# print('Head:', myLinkedList.head)
# print('Tail:', myLinkedList.tail)
# print('Length:', myLinkedList.length, '\n')
# myLinkedList.print_list()

# testing get
# myLinedList = LinkedList(0)
# myLinedList.make_empty()
# myLinedList.append(1)
# myLinedList.append(2)
# myLinedList.append(3)

# print(myLinedList.get(2).value)

# testing set_value
# myLinkedList = LinkedList(11)
# myLinkedList.append(3)
# myLinkedList.append(23)
# myLinkedList.append(7)
# print('LL before set_value():')
# myLinkedList.print_list()
# myLinkedList.set_value(1,4)
# print('\nLL after set_value():')
# myLinkedList.print_list()

# testing insert
# my_linked_list = LinkedList(1)
# my_linked_list.append(3)
# print('LL before insert():')
# my_linked_list.print_list()
# my_linked_list.insert(1,2)
# print('\nLL after insert(2) in middle:')
# my_linked_list.print_list()
# my_linked_list.insert(0,0)
# print('\nLL after insert(0) at beginning:')
# my_linked_list.print_list()
# my_linked_list.insert(4,4)
# print('\nLL after insert(4) at end:')
# my_linked_list.print_list()
# """
#     EXPECTED OUTPUT:
#     ----------------
#     LL before insert():
#     1
#     3
#     LL after insert(2) in middle:
#     1
#     2
#     3
#     LL after insert(0) at beginning:
#     0
#     1
#     2
#     3
#     LL after insert(4) at end:
#     0
#     1
#     2
#     3
#     4
# """

# testing remove
# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# print('LL before remove():')
# my_linked_list.print_list()
# print('\nRemoved node:')
# print(my_linked_list.remove(2).value)
# print('LL after remove() in middle:')
# my_linked_list.print_list()
# print('\nRemoved node:')
# print(my_linked_list.remove(0).value)
# print('LL after remove() of first node:')
# my_linked_list.print_list()
# print('\nRemoved node:')
# print(my_linked_list.remove(2).value)
# print('LL after remove() of last node:')
# my_linked_list.print_list()
# """
#     EXPECTED OUTPUT:
#     ----------------
#     LL before remove():
#     1
#     2
#     3
#     4
#     5
#     Removed node:
#     3
#     LL after remove() in middle:
#     1
#     2
#     4
#     5
#     Removed node:
#     1
#     LL after remove() of first node:
#     2
#     4
#     5
#     Removed node:
#     5
#     LL after remove() of last node:
#     2
#     4
# """

# testing reverse
my_linked_list = LinkedList(1)
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.append(1)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()
my_linked_list.make_empty()
my_linked_list.print_list()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.reverse()
my_linked_list.append(3)
my_linked_list.print_list()
my_linked_list.reverse()
print(my_linked_list.length)
my_linked_list.append(4)
print(my_linked_list.length)



