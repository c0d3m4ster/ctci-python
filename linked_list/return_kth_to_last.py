import unittest


# Return Kth to Last: 
# Implement an algorithm to find the kth to last element of a singly linked list.

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
    
    def append(self, data):        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def kth_to_last(self, k):
        if k <= 0:
            return None
        
        p1 = self.head
        p2 = self.head        
        for _ in range(k):
            if p1 is None:
                return None
            p1 = p1.next
                
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2.data if p2 else None


class TestKthToLast(unittest.TestCase):
    def test_long_string(self):
        linked_list = LinkedList([1, 2, 3, 4, 5])          
        self.assertTrue(linked_list.kth_to_last(2) == 4)

    def test_empty_list(self):
        linked_list = LinkedList([])          
        self.assertTrue(linked_list.kth_to_last(1) == None)

    def test_single_element(self):
        linked_list = LinkedList([2])          
        self.assertTrue(linked_list.kth_to_last(1) == 2)

    def test_all_identical_elements(self):
        linked_list = LinkedList([1, 1, 1])          
        self.assertTrue(linked_list.kth_to_last(1) == 1)

    def test_k_greater_than_length(self):
        linked_list = LinkedList([1, 2])          
        self.assertTrue(linked_list.kth_to_last(3) == None)

    def test_negative_k(self):
        linked_list = LinkedList([1, 2, 3])          
        self.assertTrue(linked_list.kth_to_last(-1) == None)

if __name__ == '__main__':
    unittest.main()