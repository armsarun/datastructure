"""
Binary search tree stores the higher value than root value to right leaf
and lower value to left side
It's different from Tree instead of checking all the values we could check based on value and
do the insert and search
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_helper(self.root,new_val)

    def insert_helper(self,current,new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right,new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left,new_val)
            else:
                current.left=Node(new_val)
    def search(self, find_val):
        return self.search_helper(self.root,find_val)

    def search_helper(self,current,find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value > find_val:
                return self.search_helper(current.left,find_val)
            else:
                return self.search_helper(current.right,find_val)
        else:
            return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
