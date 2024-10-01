import unittest

# Zero Matrix: 
# Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

def zero_matrix(matrix):
    return matrix





class TestZeroMatix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(zero_matrix([]), [])

if __name__ == "__main__":
    unittest.main()
