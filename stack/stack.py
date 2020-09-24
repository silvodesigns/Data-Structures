"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def pop(self):
        if self.length() == 0:
            return None
        #find last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        #find one before last
        before_last = self.head
        while before_last.next != last_node:
            before_last = before_last.next
        #erase last node and make one before last point to None
        last_node = None
        before_last.next = None
        
               
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop()

#     def print_stack(self):
#         for x in self.storage:
#             print(x)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length()

    def push(self, value):
        self.storage.push(value)

    def pop(self):
         return self.storage.pop()

    def print_stack(self):
        self.storage.print_list()
    
    

myStack = Stack()
myStack.push("a")
myStack.push("b")
myStack.push("c")
myStack.print_stack()
myStack.pop()
myStack.print_stack()





