import unittest


# Imagine a (literal) stack of plates. If the stack gets too high, 
# it might topple. Therefore, in real life, we would likely start 
# a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. 
# SetOfStacks should be composed of several stacks and should 
# create a new stack once the previous one exceeds capacity. 
# SetOfStacks. push() and SetOfStacks. pop() should behave 
# identically to a single stack (that is, pop () should return 
# the same values as it would if there were just a single stack). 
# Follow up: Implement a function popAt ( int index) which performs 
# a pop operation on a specific sub-stack.


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def push(self, value):
        if len(self.items) < self.capacity:
            self.items.append(value)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.items:
            raise Exception("Stack is empty")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class SetOfStacks:
    def __init__(self, capacity=10):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if not self.stacks or len(self.stacks[-1].items) >= self.capacity:
            new_stack = Stack(self.capacity)
            new_stack.push(value)
            self.stacks.append(new_stack)
        else:
            self.stacks[-1].push(value)

    def pop(self):
        if not self.stacks:
            raise Exception("No stacks available")
        
        top_stack = self.stacks[-1]
        value = top_stack.pop()
        
        if top_stack.is_empty():
            self.stacks.pop()  # Remove the empty stack
        
        return value

    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Stack index out of range")
        
        stack_to_pop = self.stacks[index]
        value = stack_to_pop.pop()
        
        if stack_to_pop.is_empty():
            del self.stacks[index]  # Remove the empty stack
        
        return value

class TestSetOfStacks(unittest.TestCase):
    
    def setUp(self):
        self.set_of_stacks = SetOfStacks(capacity=2)

    def test_push_and_pop(self):
        self.set_of_stacks.push(1)
        self.set_of_stacks.push(2)
        
        # Should create a new stack after reaching capacity
        self.set_of_stacks.push(3)
        
        # Pop should return the last pushed item
        self.assertEqual(self.set_of_stacks.pop(), 3)
        
        # Pop should return 2
        self.assertEqual(self.set_of_stacks.pop(), 2)
        
        # Pop should return 1
        self.assertEqual(self.set_of_stacks.pop(), 1)

    def test_pop_empty_stack(self):
        with self.assertRaises(Exception) as context:
            self.set_of_stacks.pop()
        
        self.assertTrue("No stacks available" in str(context.exception))

    def test_pop_at_specific_index(self):
        self.set_of_stacks.push(1)
        self.set_of_stacks.push(2)
        self.set_of_stacks.push(3)  # New stack created
        
        # Pop from the first stack
        popped_value = self.set_of_stacks.pop_at(0)
        
        # Should return 2 since it's the last pushed item in the first stack
        self.assertEqual(popped_value, 2)

    def test_pop_at_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.set_of_stacks.pop_at(0)  # No stacks yet
        
        self.assertTrue("Stack index out of range" in str(context.exception))

# Run the tests
if __name__ == '__main__':
    unittest.main()