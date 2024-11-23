import unittest


# Minimal Tree: Given a sorted (increasing order) array 
# with unique integer elements, write an algo­rithm
# to create a binary search tree with minimal height.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MinimalTree:
    def __init__(self, sorted_array):
        self.root = self._create_bst(sorted_array)

    def _create_bst(self, sorted_array):
        if not sorted_array:
            return None
        
        mid = len(sorted_array) // 2
        node = TreeNode(sorted_array[mid])
        
        node.left = self._create_bst(sorted_array[:mid])
        node.right = self._create_bst(sorted_array[mid+1:])
        
        return node

# Example of usage:
# sorted_array = [1, 2, 3, 4, 5, 6, 7]
# bst = MinimalTree(sorted_array)
# print(bst.root.value)  # Should output the root of the BST



class TestMinimalTree(unittest.TestCase):

    def test_minimal_tree(self):
        sorted_array = [1, 2, 3, 4, 5, 6, 7]
        bst = MinimalTree(sorted_array)
        
        # Check root value
        self.assertEqual(bst.root.value, 4)
        
        # Check left subtree
        self.assertEqual(bst.root.left.value, 2)
        self.assertEqual(bst.root.left.left.value, 1)
        self.assertEqual(bst.root.left.right.value, 3)

        # Check right subtree
        self.assertEqual(bst.root.right.value, 6)
        self.assertEqual(bst.root.right.left.value, 5)
        self.assertEqual(bst.root.right.right.value, 7)

    def test_empty_array(self):
        bst = MinimalTree([])
        self.assertIsNone(bst.root)

if __name__ == '__main__':
    unittest.main()