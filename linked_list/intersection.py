import unittest

# Intersection: 
# Given two (singly) linked lists, determine if the two lists intersect.
# Return the intersecting node. 
# Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node 
# (by reference) as the jth node of the second linked list, 
# then they are intersecting.

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

    def __len__(self):        
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def append(self, data):        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def is_intersect(self, other):        
        self_node = self.head                
        while self_node:
            other_node = other.head
            while other_node:
                if self_node.data == other_node.data:
                    return True
                other_node = other_node.next            
            self_node = self_node.next
        return False
    
    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)


class TestIntersectingLinkedList(unittest.TestCase):

    def test_intersecting_linked_list(self):
        linked_list_1 = LinkedList(['a', 'b'])
        linked_list_2 = LinkedList(['b', 'c'])        
        self.assertTrue(linked_list_1.is_intersect(linked_list_2))

    def test_non_intersecting_linked_list(self):
        linked_list_1 = LinkedList(['a', 'b', 'c'])
        linked_list_2 = LinkedList(['g', 'k', 'l'])        
        self.assertFalse(linked_list_1.is_intersect(linked_list_2))

if __name__ == '__main__':
    unittest.main()