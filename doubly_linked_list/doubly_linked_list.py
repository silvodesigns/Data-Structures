"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev= None, next= None):
        self.prev = prev
        self.value = value
        self.next = next
             
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = None
        self.tail = None
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if self.head is None and self.tail is None:
            self.length += 1 
            self.head = new_node
            self.tail = new_node
        else:
            self.length += 1 
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
            
         
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
       cur = self.head
       #return None if head is None
       if self.head is None:
           return None
       #if there is only one Node
       elif self.head.next is None:
           head = self.head
           self.head = None
           self.tail = None
           self.length -= 1
           return head.value
       #if more than one Node
       value = cur.value
       self.head = self.head.next
       self.head.prev = None
       self.length -= 1
       return value
       

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return None
        elif self.head.next:
            cur = self.head
            while cur.next:
                cur = cur.next
            self.tail = cur
            removed = self.tail
            self.tail = removed.prev
            self.tail.next = None
            return removed
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #first check if list is not empty
        if self.head is None:
            return None
        #check if the node is already at head
        if self.head.value == node:
            return self.head
        #if not already at head
            #check if the node to move is tail
        if self.tail.value == node:
            move = self.tail
            to = self.head
            newTail = move.prev
            to.prev = move
            move.next = to
            newTail.next = None
            self.head = move
            return self.head
            #lets find the position of the node in the list
            #and reconfigure it to be at the head position
            #and move over one step to the right the Node that was at head already
        else:
            cur = self.head
            while cur.value != node:
                cur = cur.next
            move = cur
            to = self.head
            move.prev.next = move.next
            move.next.prev = move.prev
            self.head.prev = move
            move.next = to
            self.head = move
            return self.head

            

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
           #check if list is empty
        if self.head is None:
            return None
        #check if is already in there
        if self.tail.value == node:
            return self.tail
        #check if the value to move is head
        if self.head.value == node:
            move = self.head
            to = self.tail
            newHead = move.next
            move.next.prev = None
            self.head = newHead
            to.next = move
            move.next = None
            self.tail = move
            return self.tail
        else:
            cur = self.head
            while cur.value != node:
                cur = cur.next
            move = cur
            to = self.tail
            move.prev.next = move.next
            move.next.prev = move.prev
            to.next = move
            move.next = None
            self.tail = move
            return self.tail

         

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #deletes the Node if it is the only one present
            cur = self.head
            while cur: #run until cur is None
                if cur.value == node and cur == self.head:
                    if not cur.next:
                        cur = None
                        self.head = None
                        return 
                    #case 2: the Node to be deleted is head, but LL is not empty
                    else:
                        nxt = cur.next
                        cur.next = None
                        nxt.prev = None
                        cur = None
                        self.head = nxt
                        return
               #will become True in any iteration of the loop where cur.data equals Node
                elif cur.value == node:
                
                    #case 3
                    if cur.next:
                        nxt = cur.next
                        prev = cur.prev
                        prev.next = nxt
                        nxt.prev = prev
                        cur.next = None
                        cur.prev = None
                        cur = None
                        return
                    else:
                        prev = cur.prev
                        prev.next = None
                        cur.prev = None
                        cur= None
                        return

                cur = cur.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass




