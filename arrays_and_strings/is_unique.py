import unittest


# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?


# We check for uniqueness without using additional data structures like 
# lists, sets and dictionaries

# defining a function to check if an input string has unique characters
def is_unique(input_string, case_insensitive=True):

    # early exit if string length exceeds unique 128 ASCII characters
    if len(input_string) > 128:  
        return False
    
    # if case sensitive is not matter
    if case_insensitive:
        input_string = input_string.lower()
    
    # bit vector is used to track characters in the input string
    bit_vector = 0

    for char in input_string:

        # calculate the bit position based on ASCII value
        bit_position = ord(char)

        # create a single bit 1 at the position corresponding to the ASCII value
        bit_mask = 1 << bit_position

        # checks whether the character has already been set in bit_vector        
        if (bit_vector & bit_mask) > 0:
            # non-unique character already found
            return False
        
        # set the bit at bit_position
        bit_vector |= bit_mask
    
    
    # all characters are unique
    return True


# testing the function "is_unique"
class TestIsUnique(unittest.TestCase):

    def test_long_string(self):
        self.assertFalse(is_unique("a" * 129), False)

    def test_case_sensitivity(self):
        self.assertTrue(is_unique("Aa", case_insensitive=False), True)
    
    def test_empty_string(self):
        self.assertTrue(is_unique(""), True)
    
    def test_single_character(self):
        self.assertTrue(is_unique("a"), True)
    
    def test_unique_characters(self):
        self.assertTrue(is_unique("abcdef"), True)
    
    def test_duplicate_characters(self):
        self.assertFalse(is_unique("abcdea"), False)
    
    def test_case_insensitivity(self):
        self.assertFalse(is_unique("Aa"), False)    
    
    def test_special_characters(self):
        self.assertTrue(is_unique("!@#$%^&*()"), True)
        
    def test_mixed_characters(self):
        self.assertFalse(is_unique("abc123abc"), False)


if __name__ == '__main__':
    unittest.main()
