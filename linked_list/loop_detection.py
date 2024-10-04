import unittest

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

    def create_loop(self, target_data):        
        loop_start_node = None
        last_node = self.head        
        while last_node and last_node.next:
            last_node = last_node.next                
        current = self.head        
        while current:
            if current.data == target_data:
                loop_start_node = current
                break
            current = current.next               
        if loop_start_node and last_node:
            last_node.next = loop_start_node

    def is_corrupted(self):
        fast = slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break        
        if fast is None or fast.next is None:
            return None        
        slow = self.head
        while fast is not slow:
            fast = fast.next
            slow = slow.next        
        return fast        
    
    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)


class TestIntersectingLinkedList(unittest.TestCase):

    def test_is_corrupted(self):
        linked_list = LinkedList(['A', 'B', 'C', 'D', 'E', 'C'])                
        linked_list.create_loop('C')       
        output_node = linked_list.is_corrupted()        
        self.assertEqual(output_node.data, 'C')    

    def test_is_not_corrupted(self):
        linked_list = LinkedList(['A', 'B', 'C', 'D', 'E', 'C'])
        output_node = linked_list.is_corrupted()        
        self.assertEqual(output_node, None)

if __name__ == '__main__':
    unittest.main()