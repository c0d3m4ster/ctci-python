import unittest

# Write a program to sort a stack such that the smallest items 
# are on the top. You can use an additional temporary stack, 
# but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

class SortedStack:
    def __init__(self):
        self.stack = []
        self.temporary_stack = []

    def push(self, value):
        # Move elements from main stack to temporary stack if they are larger than the value to be inserted
        while self.stack and self.stack[-1] > value:
            self.temporary_stack.append(self.stack.pop())
        
        # Insert the new value
        self.stack.append(value)
        
        # Push everything back from temporary stack
        while self.temporary_stack:
            self.stack.append(self.temporary_stack.pop())

    def pop(self):
        if self.is_empty():
            raise Exception('Stack Underflow')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Unit Tests
class TestSortedStack(unittest.TestCase):

    def setUp(self):
        self.sorted_stack = SortedStack()

    def test_push_and_pop(self):
        self.sorted_stack.push(3)
        self.sorted_stack.push(1)
        self.sorted_stack.push(2)
        
        # The stack should now be sorted with 1 on top
        self.assertEqual(self.sorted_stack.pop(), 1)
        self.assertEqual(self.sorted_stack.pop(), 2)
        self.assertEqual(self.sorted_stack.pop(), 3)

    def test_peek(self):
        self.sorted_stack.push(5)
        self.sorted_stack.push(3)
        
        # Peek should return 3 without removing it
        self.assertEqual(self.sorted_stack.peek(), 3)
        
        # Ensure that peek does not remove the element
        self.assertEqual(self.sorted_stack.pop(), 3)

    def test_empty_stack_exceptions(self):
        with self.assertRaises(Exception) as context:
            self.sorted_stack.pop()  # Should raise Stack Underflow
        
        self.assertTrue("Stack Underflow" in str(context.exception))
        
        with self.assertRaises(Exception) as context:
            self.sorted_stack.peek()  # Should raise Stack is empty
        
        self.assertTrue("Stack is empty" in str(context.exception))

if __name__ == '__main__':
    unittest.main()