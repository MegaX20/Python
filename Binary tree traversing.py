# Binary tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            self.postorder_print(self.root, "")
        else:
            print("Traversal type " + traversal_type + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """ root -> left -> right """
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """ left -> root -> right """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """ left -> right -> root """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += str(start.value + "-")
        return traversal

#   3
#  / \
# 2   1


bt = BinaryTree(3)
bt.root.left = Node(2)
bt.root.right = Node(1)