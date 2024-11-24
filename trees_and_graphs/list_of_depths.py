class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_depth_linked_lists(self):
        if not self.root:
            return []

        result = []
        current_level_nodes = [self.root]

        while current_level_nodes:
            # Create a new linked list for the current level
            head = None
            tail = None
            
            next_level_nodes = []
            for node in current_level_nodes:
                # Create a new ListNode for each node at this level
                list_node = ListNode(node.value)
                if head is None:
                    head = list_node
                    tail = list_node
                else:
                    tail.next = list_node
                    tail = list_node
                
                # Add child nodes to the next level's list
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            result.append(head)  # Append the linked list for this level
            current_level_nodes = next_level_nodes  # Move to the next level

        return result


import unittest

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree()
        # Constructing a sample binary tree:
        #         1
        #        / \
        #       2   3
        #      / \   \
        #     4   5   6
        
        self.tree.root = TreeNode(1)
        self.tree.root.left = TreeNode(2)
        self.tree.root.right = TreeNode(3)
        self.tree.root.left.left = TreeNode(4)
        self.tree.root.left.right = TreeNode(5)
        self.tree.root.right.right = TreeNode(6)

    def test_depth_linked_lists(self):
        linked_lists = self.tree.create_depth_linked_lists()
        
        # Check that we have 3 linked lists (for depth 0, 1, and 2)
        self.assertEqual(len(linked_lists), 3)

        # Check values in each linked list at each depth
        depth_0_values = [node.value for node in self._linked_list_to_array(linked_lists[0])]
        depth_1_values = [node.value for node in self._linked_list_to_array(linked_lists[1])]
        depth_2_values = [node.value for node in self._linked_list_to_array(linked_lists[2])]

        self.assertEqual(depth_0_values, [1])          # Depth 0: [1]
        self.assertEqual(depth_1_values, [2, 3])       # Depth 1: [2, 3]
        self.assertEqual(depth_2_values, [4, 5, 6])    # Depth 2: [4, 5, 6]

    def _linked_list_to_array(self, head):
        """ Helper function to convert linked list to array for easy comparison. """
        array = []
        current = head
        while current:
            array.append(current)
            current = current.next
        return array

if __name__ == '__main__':
    unittest.main()
