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
