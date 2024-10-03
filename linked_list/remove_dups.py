import unittest


# Remove Dups:
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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

    def remove_duplicates(self):        
        current = self.head        
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next


class TestRemoveDups(unittest.TestCase):
    def test_long_string(self):
        linked_list_1 = LinkedList([1, 2, 3, 2, 2, 4, 1])
        linked_list_2 = LinkedList([1, 2, 3, 4])
        linked_list_1.remove_duplicates()        
        self.assertTrue(linked_list_2 == linked_list_1)

    def test_empty_list(self):
        linked_list_1 = LinkedList([])
        linked_list_2 = LinkedList([])
        linked_list_1.remove_duplicates()
        self.assertTrue(linked_list_2 == linked_list_1)

    def test_single_element(self):
        linked_list_1 = LinkedList([5])
        linked_list_2 = LinkedList([5])
        linked_list_1.remove_duplicates()
        self.assertTrue(linked_list_2 == linked_list_1)

    def test_all_identical_elements(self):
        linked_list_1 = LinkedList([7, 7, 7])
        linked_list_2 = LinkedList([7])
        linked_list_1.remove_duplicates()
        self.assertTrue(linked_list_2 == linked_list_1)

if __name__ == '__main__':
    unittest.main()