import unittest

# Check Balanced: Implement a function to check if a binary tree 
# is balanced. For the purposes of this question, 
# a balanced tree is defined to be a tree such that 
# the heights of the two subtrees of any node never 
# differ by more than one.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def is_balanced(self, root):
        def check_height(node):
            if not node:
                return 0
            
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1

        return check_height(root) != -1


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        # Create a balanced binary tree
        self.balanced_tree = TreeNode(1)
        self.balanced_tree.left = TreeNode(2)
        self.balanced_tree.right = TreeNode(3)
        self.balanced_tree.left.left = TreeNode(4)
        self.balanced_tree.left.right = TreeNode(5)

        # Create an unbalanced binary tree
        self.unbalanced_tree = TreeNode(1)
        self.unbalanced_tree.left = TreeNode(2)
        self.unbalanced_tree.left.left = TreeNode(3)
        self.unbalanced_tree.left.left.left = TreeNode(4)

    def test_balanced(self):
        tree = BinaryTree()
        self.assertTrue(tree.is_balanced(self.balanced_tree))

    def test_unbalanced(self):
        tree = BinaryTree()
        self.assertFalse(tree.is_balanced(self.unbalanced_tree))

    def test_empty_tree(self):
        tree = BinaryTree()
        self.assertTrue(tree.is_balanced(None))  # An empty tree is considered balanced

if __name__ == '__main__':
    unittest.main()