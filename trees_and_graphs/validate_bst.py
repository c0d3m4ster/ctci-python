import unittest

# Validate BST: Implement a function to check 
# if a binary tree is a binary search tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    def is_bst(self):
        return self._is_bst(self.root, float('-inf'), float('inf'))

    def _is_bst(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.value < max_value):
            return False
        return (self._is_bst(node.left, min_value, node.value) and 
                self._is_bst(node.right, node.value, max_value))


# Unit Tests
class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()

    def test_empty_tree(self):
        # An empty tree is a valid BST
        self.assertTrue(self.tree.is_bst())

    def test_single_node(self):
        # A single-node tree is a valid BST
        self.tree.insert(10)
        self.assertTrue(self.tree.is_bst())

    def test_valid_bst(self):
        # Testing a valid BST
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(15)
        self.assertTrue(self.tree.is_bst())

    def test_invalid_bst(self):
        # Testing an invalid BST
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(12)
        self.tree.insert(11)  # This makes it invalid as 11 < 12 but is in right subtree
        self.assertFalse(self.tree.is_bst())

if __name__ == '__main__':
    unittest.main()