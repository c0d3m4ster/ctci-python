import unittest


# Delete Middle Node: 
# Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) 
# of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, initial_data=None):
        self.head = None
        if initial_data is not None:
            for item in initial_data:
                self.append(item)
    
    def __len__(self):        
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def __eq__(self, other):        
        if len(self) != len(other):
            return False                
        current1 = self.head
        current2 = other.head        
        while current1 and current2:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next            
        return True

    def append(self, data):        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_middle(self, node_to_delete):        
        if node_to_delete is None or node_to_delete.next is None:
            raise ValueError("Cannot delete this node")        
        node_to_delete.data = node_to_delete.next.data
        node_to_delete.next = node_to_delete.next.next


class TestDeleteMiddleNode(unittest.TestCase):
    def test_long_string(self):
        linked_list_1 = LinkedList(['a', 'b', 'c', 'd', 'e', 'f'])
        linked_list_2 = LinkedList(['a', 'b', 'd', 'e', 'f'])
        linked_list_1.delete_middle(linked_list_1.head.next.next)
        self.assertTrue(linked_list_2 == linked_list_1)

    def test_empty_list(self):
        linked_list_1 = LinkedList([])
        with self.assertRaises(ValueError):
            linked_list_1.delete_middle(None)

    def test_single_element(self):
        linked_list_1 = LinkedList(['a'])
        with self.assertRaises(ValueError):
            linked_list_1.delete_middle(linked_list_1.head)

    def test_single_element_no_data(self):
        linked_list_1 = LinkedList(['a'])
        with self.assertRaises(ValueError):
            linked_list_1.delete_middle(None)

    def test_all_identical_elements(self):
        linked_list_1 = LinkedList(['a', 'a', 'a', 'a', 'a'])
        linked_list_2 = LinkedList(['a', 'a', 'a', 'a'])          
        linked_list_1.delete_middle(linked_list_1.head.next)
        self.assertTrue(linked_list_2 == linked_list_1)

if __name__ == '__main__':
    unittest.main()