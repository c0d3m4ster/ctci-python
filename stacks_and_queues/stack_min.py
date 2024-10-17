import unittest


# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in O(1) time

class MinStack:
    def __init__(self):
        self.stack = []      # store elements
        self.min_stack = []  # store minimums

    def push(self, value):
        self.stack.append(value)        
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()            
            if value == self.min_stack[-1]:
                self.min_stack.pop()
            return value
        raise IndexError("pop from empty stack")

    def min(self):
        if not self.min_stack:
            raise IndexError("min from empty stack")
        return self.min_stack[-1]

class TestMinStack(unittest.TestCase):
    
    def setUp(self):
        self.min_stack = MinStack()

    def test_push_and_min(self):
        self.min_stack.push(3)
        self.assertEqual(self.min_stack.min(), 3)
        
        self.min_stack.push(5)
        self.assertEqual(self.min_stack.min(), 3)
        
        self.min_stack.push(2)
        self.assertEqual(self.min_stack.min(), 2)
        
        self.min_stack.push(1)
        self.assertEqual(self.min_stack.min(), 1)
        
        self.min_stack.push(4)        
        self.assertEqual(self.min_stack.min(), 1)

    def test_pop_and_min(self):
        self.min_stack.push(3)
        self.min_stack.push(5)
        self.min_stack.push(2)
        
        self.assertEqual(self.min_stack.pop(), 2)
        self.assertEqual(self.min_stack.min(), 3)
        
        self.assertEqual(self.min_stack.pop(), 5)
        self.assertEqual(self.min_stack.min(), 3)
        
        self.assertEqual(self.min_stack.pop(), 3)
        
    def test_empty_pop_and_min(self):
        with self.assertRaises(IndexError):
            self.min_stack.pop()                 
            
        with self.assertRaises(IndexError):
            self.min_stack.min()                       

# Run the tests
if __name__ == '__main__':
    unittest.main()
