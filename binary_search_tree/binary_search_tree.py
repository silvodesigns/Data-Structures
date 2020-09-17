"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check weather the new node's value is less than current node's value
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        #check weather the new node's value is greater or egual to curr node value
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #base case
        #IF VALUE OF THIS NODE MATCHES THE TARGET THEN WE'VE FOUND 
        #WHAT WE LOOKING FOR
        if self.value == target:
            return True
        #how do we move closer to the base?
        if target < self.value:
            #we need to go left
            #what if there is no left child
            if not self.left:
            #then value cant be in the tree
                return False
            #what if there is ?
            else:
            #call contains of left child
                return self.left.contains(target)
        else:
            #we need to go right
            #what if there is no right child
            if not self.right:
            #then value cant be in the tree
                return False
            #what if there is ?
            else:
            #call contains of left child
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #the max value will always be the right most value
        #recursive
        # keep going right till right no more
        #base case: there is no right child
        if not self.right:
            return self.value
        #otherwise, call, get max on the right child
        return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
