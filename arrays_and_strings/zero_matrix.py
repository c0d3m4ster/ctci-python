import unittest

# Zero Matrix: 
# Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0]) if m>0 else 0
        
    rows = set()
    cols = set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix


class TestZeroMatix(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertEqual(zero_matrix([]), [])
    
    def test_non_zero_element_matrix(self):
        M_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        M_out = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(zero_matrix(M_in), M_out)

    def test_one_zero_element_matrix(self):
        M_in = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
        M_out = [[0, 0, 0], [4, 5, 0], [7, 8, 0]]
        self.assertEqual(zero_matrix(M_in), M_out)

    def test_two_zero_element_matrix(self):
        M_in = [[1, 2, 0], [4, 5, 6], [0, 8, 9]]
        M_out = [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
        self.assertEqual(zero_matrix(M_in), M_out)

    def test_three_zero_element_matrix(self):
        M_in = [[1, 2, 0], [4, 0, 6], [0, 8, 9]]
        M_out = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(zero_matrix(M_in), M_out)

if __name__ == "__main__":
    unittest.main()
