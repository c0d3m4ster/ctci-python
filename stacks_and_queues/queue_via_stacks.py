import unittest


# Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, value):
        self.stack_in.append(value)

    def pop(self):
        if not self.stack_out:  # If stack_out is empty, transfer elements
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:  # If stack_out is still empty, raise an error
            raise Exception("Queue is empty")
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:  # If stack_out is empty, transfer elements
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:  # If stack_out is still empty, raise an error
            raise Exception("Queue is empty")
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out

class TestMyQueue(unittest.TestCase):

    def setUp(self):
        self.queue = MyQueue()

    def test_push_and_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        
        # Pop should return the first element pushed (FIFO)
        self.assertEqual(self.queue.pop(), 1)
        
        # After popping 1, the next pop should return 2
        self.assertEqual(self.queue.pop(), 2)

    def test_pop_empty_queue(self):
        with self.assertRaises(Exception) as context:
            self.queue.pop()
        
        self.assertTrue("Queue is empty" in str(context.exception))

    def test_peek(self):
        self.queue.push(1)
        self.queue.push(2)
        
        # Peek should return the first element without removing it
        self.assertEqual(self.queue.peek(), 1)
        
        # Pop should still return the first element
        self.assertEqual(self.queue.pop(), 1)

    def test_peek_empty_queue(self):
        with self.assertRaises(Exception) as context:
            self.queue.peek()
        
        self.assertTrue("Queue is empty" in str(context.exception))

    def test_is_empty(self):
        # Queue should be empty initially
        self.assertTrue(self.queue.is_empty())
        
        # After pushing an element, it should not be empty
        self.queue.push(1)
        self.assertFalse(self.queue.is_empty())
        
        # After popping the element, it should be empty again
        self.queue.pop()
        self.assertTrue(self.queue.is_empty())

# Run the tests
if __name__ == '__main__':
    unittest.main()