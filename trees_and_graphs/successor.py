import unittest

# Successor: Write an algorithm to find the "next" node 
# (i.e., in-order successor) of a given node in 
# a binary search tree. You may assume that 
# each node has a link to its parent.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right

    def find_successor(self, node):
        # Case 1: Node has a right child
        if node.right:
            return self._min_value_node(node.right)
        
        # Case 2: No right child, go up to find successor
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        
        return parent

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Unit Tests
class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BST()
        # Creating a sample BST
        values = [20, 10, 30, 5, 15, 25, 35]
        for value in values:
            self.bst.insert(value)

    def test_successor_of_leaf_node(self):
        leaf_node = self.bst.root.left.right  # Node with value 15
        successor = self.bst.find_successor(leaf_node)
        self.assertEqual(successor.value, 20)  # Successor should be 20

    def test_successor_of_node_with_right_child(self):
        node_with_right_child = self.bst.root.left  # Node with value 10
        successor = self.bst.find_successor(node_with_right_child)
        self.assertEqual(successor.value, 15)  # Successor should be 15

    def test_successor_of_maximum_node(self):
        max_node = self.bst.root.right.right  # Node with value 35 (max)
        successor = self.bst.find_successor(max_node)
        self.assertIsNone(successor)  # Should be None since it's max

if __name__ == '__main__':
    unittest.main()