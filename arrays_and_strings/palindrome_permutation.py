import unittest


# Palindrome Permutation: 
# Given a string, write a function to check if it is a permutation of a palin­drome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# Example:
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# Total Time Complexity: O(n)
# The worst case space Complexity: O(n)

def is_palindrom_permutation (input_string):
    input_string = input_string.lower().replace(' ', '')
    counter = {}
    for chr in input_string:
        if chr in counter.keys():
            counter[chr]+=1
        else:
            counter[chr]=1
    return (sum(val % 2 for val in counter.values()) <= 1)


# testing the function "is_palindrom_permutation"
class TestIsPalindromPermutation(unittest.TestCase):

    def test_palindrom_permutation_string(self):
        self.assertTrue(is_palindrom_permutation("Tact Coa"), True)

    def test_case_sensitivity(self):
        self.assertTrue(is_palindrom_permutation("Aa"), True)
    
    def test_empty_string(self):
        self.assertTrue(is_palindrom_permutation(""), True)
    
    def test_single_character(self):
        self.assertTrue(is_palindrom_permutation("a"), True)
    
    def test_not_palindrom_permutation(self):
        self.assertFalse(is_palindrom_permutation("abcdef"), False)
    
    def test_duplicate_permutation(self):
        self.assertTrue(is_palindrom_permutation("abcdebcea"), True)
    
    def test_case_sensitivity_with_space(self):
        self.assertTrue(is_palindrom_permutation("Aa bB"), True)    
    
    def test_special_characters(self):
        self.assertFalse(is_palindrom_permutation("www.google.com"), False)
        
    def test_mixed_characters(self):
        self.assertTrue(is_palindrom_permutation("abc33abc"), True)


if __name__ == '__main__':
    unittest.main()
