import unittest


# Three in One: Describe how you could use a single array to implement three stacks

class ThreeStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = [0] * capacity
        self.sizes = [0] * 3

    def push(self, stack_num, value):
        if self.sizes[stack_num] >= self.capacity // 3:
            raise Exception("Stack Overflow")
        index = self._get_top_index(stack_num) + 1
        self.values[index] = value
        self.sizes[stack_num] += 1

    def pop(self, stack_num):
        if self.sizes[stack_num] == 0:
            raise Exception("Stack Underflow")
        index = self._get_top_index(stack_num)
        value = self.values[index]
        self.values[index] = 0
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.sizes[stack_num] == 0:
            raise Exception("Stack is empty")
        return self.values[self._get_top_index(stack_num)]

    def _get_top_index(self, stack_num):
        offset = (self.capacity // 3) * stack_num
        return offset + self.sizes[stack_num] - 1

# Unit Tests
class TestThreeStacks(unittest.TestCase):

    def setUp(self):
        # Total capacity for all stacks combined is 9
        self.stacks = ThreeStacks(9)

    def test_push_and_pop(self):
        # Test pushing and popping from stack 0
        self.stacks.push(0, 10)
        self.stacks.push(0, 20)
        self.assertEqual(self.stacks.pop(0), 20)
        
        # Test pushing and popping from stack 1
        self.stacks.push(1, 30)
        self.assertEqual(self.stacks.pop(1), 30)

    def test_peek(self):
        # Test peeking at the top element
        self.stacks.push(2, 40)
        self.assertEqual(self.stacks.peek(2), 40)
        
        # Ensure peek does not remove the element
        self.assertEqual(self.stacks.peek(2), 40)

    def test_stack_overflow(self):
        # Fill up stack 0 to its limit
        for i in range(3):  # Since capacity is 9, each stack can hold up to 3 elements
            self.stacks.push(0, i + 10)
        
        with self.assertRaises(Exception) as context:
            self.stacks.push(0, 99)  # This should raise Stack Overflow
        self.assertTrue("Stack Overflow" in str(context.exception))

    def test_stack_underflow(self):
        with self.assertRaises(Exception) as context:
            self.stacks.pop(1)  # This should raise Stack Underflow since it's empty
        
        self.assertTrue("Stack Underflow" in str(context.exception))

    def test_peek_empty_stack(self):
        with self.assertRaises(Exception) as context:
            self.stacks.peek(2)  # This should raise an exception since stack is empty
        
        self.assertTrue("Stack is empty" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
