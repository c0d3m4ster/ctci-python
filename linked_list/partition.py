import unittest


# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input:3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

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

    def partition(self, data):        
        less_head = Node(None)  
        equal_head = Node(None)  
        greater_head = Node(None)

        less_current = less_head
        equal_current = equal_head
        greater_current = greater_head

        current = self.head

        while current:
            next_node = current.next  
            if current.data < data:
                less_current.next = current
                less_current = less_current.next
            elif current.data == data:
                equal_current.next = current
                equal_current = equal_current.next
            else:
                greater_current.next = current
                greater_current = greater_current.next
            
            current.next = None  
            current = next_node
        
        greater_current.next = None  
        less_current.next = equal_head.next
        equal_current.next = greater_head.next       
        self.head = less_head.next        
        return self
    
    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)


class TestPartitionLinkedList(unittest.TestCase):
    def test_long_list(self):
        linked_list_1 = LinkedList([3, 5, 8, 5, 10, 2, 1])
        linked_list_2 = LinkedList([3, 2, 1, 5, 5, 8, 10])        
        linked_list_1.partition(5)
        self.assertTrue(linked_list_2 == linked_list_1)

    def test_empty_list(self):
        linked_list_1 = LinkedList([])
        linked_list_1.partition(5)
        self.assertTrue(linked_list_1 == LinkedList([]))

    def test_single_element(self):
        linked_list_1 = LinkedList([5])
        linked_list_1.partition(5)
        self.assertTrue(linked_list_1 == LinkedList([5]))

    def test_single_element_no_data(self):
        linked_list_1 = LinkedList([])
        linked_list_1.partition(3)
        self.assertTrue(linked_list_1 == LinkedList([]))

    def test_all_identical_elements(self):
        linked_list_1 = LinkedList([5, 5, 5])
        linked_list_2 = LinkedList([5, 5, 5])
        linked_list_1.partition(5)
        self.assertTrue(linked_list_2 == linked_list_1)

if __name__ == '__main__':
    unittest.main()