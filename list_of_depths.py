import unittest
from collections import deque

# List of Depths: Given a binary tree, design an algorithm which
# creates a linked list of all the nodes at each depth 
# (e.g., if you have a tree with depth D, 
# you'll have D linked lists).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def binaryTreeToLists(self, root):
        if root is None:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_length = len(queue)
            dummy_head = ListNode(0)  # Dummy head for the linked list
            last_node = dummy_head
            
            for _ in range(level_length):
                node = queue.popleft()
                last_node.next = ListNode(node.val)  # Create new ListNode
                last_node = last_node.next  # Move to the end of the list
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(dummy_head.next)  # Append the linked list for this level
        
        return result

# Unit Tests
class TestBinaryTreeToLists(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_tree(self):
        # Constructing the binary tree:
        #       1
        #      / \
        #     2   3
        #    /
        #   4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        result = self.solution.binaryTreeToLists(root)

        # Convert result to lists for easier comparison
        def to_list(head):
            result_list = []
            while head:
                result_list.append(head.val)
                head = head.next
            return result_list
        
        expected_output = [[1], [2, 3], [4]]
        actual_output = [to_list(lst) for lst in result]
        
        self.assertEqual(actual_output, expected_output)

    def test_empty_tree(self):
        self.assertEqual(self.solution.binaryTreeToLists(None), [])

if __name__ == '__main__':
    unittest.main()