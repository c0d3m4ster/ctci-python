import unittest


# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

def are_permutation(input_string_1, input_string_2):
    # early exit if lengths are different
    if len(input_string_1) != len(input_string_2):
        return False
    
    counter = 0
    for char in input_string_1:
        counter += ord(char)
    for char in input_string_2:
        counter -= ord(char)
    if counter==0:
        return True
    else:
        return False 


# testing the function "are_permutation"
class TestArePermutation(unittest.TestCase):

    def test_not_permuted(self):
        self.assertFalse(are_permutation('abcd', 'acbx'))
    
    def test_permuted_numbers(self):
        self.assertTrue(are_permutation('7928.15', '5128.97'))
    
    def test_repeated_letters(self):
        self.assertFalse(are_permutation('Hello', 'Helloo'))

    def test_permuted_letters(self):
        self.assertTrue(are_permutation('Azbcx', 'cAzxb'))
    
    def test_permuted_with_spaces(self):
        self.assertTrue(are_permutation('A dog', 'Ad og'))

    def test_permuted_special_characters(self):
        self.assertTrue(are_permutation('*%@$)', '%)@$*'))
    
    def test_permuted_letters_and_numbers(self):
        self.assertTrue(are_permutation('a4_paper0', 'a_paper40'))

    def test_repeated_numbers(self):
        self.assertFalse(are_permutation('541111', '154'))

    def test_not_permuted_letters(self):
        self.assertFalse(are_permutation('a ', 'a'))

if __name__ == '__main__':
    unittest.main()
