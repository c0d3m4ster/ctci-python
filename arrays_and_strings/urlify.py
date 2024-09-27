import unittest


# URLify: 
# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end 
# to hold the additional characters, and that you are given the "true"
# length of the string. 
# (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# 
# Input: "Mr John Smith    ", 13
# Output:"Mr%20John%20Smith"


def urlify(input_streang, input_length):
    output = []
    for i, c in enumerate(input_streang):
        if c == ' ' and i<=input_length:
            output.append('%20') 
        else:
            output.append(c)
    return ''.join(output)



# testing the function "urlify"
class TestUrlify(unittest.TestCase):

    def test_urlify(self):
        self.assertTrue(
            urlify(
                "Mr John Smith    ", 13), 
                "Mr%20John%20Smith")
    
    def test_first_space(self):
        self.assertTrue(
            urlify(
                " Initial Characters  ", 19), 
                "%20Initial%20Characters")

    def test_final_space(self):
        self.assertTrue(
            urlify(
                "Final letter is a space  ", 24), 
                "%20Final%20letter%20is%20a%20space%20")

if __name__ == '__main__':
    unittest.main()
