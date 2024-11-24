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
