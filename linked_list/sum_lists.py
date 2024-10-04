# Sum Lists: 
# You have two numbers represented by a linked list, 
# where each node contains a single digit. 
# The digits are stored in reverse order, 
# such that the 1 's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.


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

    def to_number(self, reverse=True):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        if reverse:
            return int("".join(values)[::-1])
        else:
            return int("".join(values))

    def add(self, other, reverse=True):
        self_num = self.to_number(reverse)   
        other_num = other.to_number(reverse)   
        num = self_num + other_num
        if reverse:
            return LinkedList(list(str(num)[::-1]))
        else:
            return LinkedList(list(str(num)))
    
    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.data))
            node = node.next
        return " -> ".join(values)
    

linked_list_1 = LinkedList([7, 1, 6])   # 617
linked_list_2 = LinkedList([5, 9, 2])   # 295

print(linked_list_1.add(linked_list_2)) # 2 -> 1 -> 9



# FOLLOW UP
linked_list_1 = LinkedList([6, 1, 7])   # 617
linked_list_2 = LinkedList([2, 9, 5])   # 295

print(linked_list_1.add(linked_list_2, reverse=False)) # 9 -> 1 -> 2
