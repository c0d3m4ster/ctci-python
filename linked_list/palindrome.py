import unittest


# palindrome: 
# Implement a function to check if a linked list is a palindrome
# A palindrome is a word or phrase that is the same forwards and backwards
# EXAMPLE
# Input: the linked list a->b->c->b->a
# Result: True

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

    def is_palindrome(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        s = "".join(values)
        return s == s[::-1]
    
    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)


class TestPalindromeLinkedList(unittest.TestCase):

    def test_string_palindrome(self):
        linked_list = LinkedList(['a', 'b', 'c', 'b', 'a'])
        self.assertTrue(linked_list.is_palindrome())

    def test_number_palindrome(self):
        linked_list = LinkedList([1, 2, 3, 4, 3, 2, 1])
        self.assertTrue(linked_list.is_palindrome())

if __name__ == '__main__':
    unittest.main()