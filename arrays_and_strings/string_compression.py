import unittest


# String Compression:
# Implement a method to perform basic string compression
# using the counts of repeated characters.
# For example, the string "aabcccccaaa" would become "a2blc5a3".
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).


def string_compression(input_string):
    output = []
    compressed = False    
    for i in range(len(input_string)):        
        if i==0:
            counter = 1
        elif input_string[i] != input_string[i - 1]:
            output.append(input_string[i-1] + str(counter))
            if (counter>1) and (not compressed):
                compressed = True
            counter = 1
        elif i == len(input_string)-1:
            counter += 1
            output.append(input_string[i] + str(counter))
            if (counter>1) and (not compressed):
                compressed = True
        else:
            counter += 1    
    if compressed:
        return ''.join(output)
    else:
        return input_string


# testing the function "string_compression"
class TestStringCompression(unittest.TestCase):

    def test_compressed(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
    
    def test_not_compressed(self):
        self.assertEqual(string_compression("abca"), "abca")
    
    def test_case_sensitive(self):
        self.assertEqual(string_compression("aAbcAa"), "aAbcAa")

    def test_empty_string(self):
        self.assertEqual(string_compression(""), "")

    def test_single_character(self):
        self.assertEqual(string_compression("q"), "q")

    def test_repeated_single_character(self):
        self.assertEqual(string_compression("www"), "w3")


if __name__ == '__main__':
    unittest.main()
