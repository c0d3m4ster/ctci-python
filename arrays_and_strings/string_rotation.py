import unittest


# String Rotation:
# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").

def is_substring(s1, s2):
    return s2 in s1

def is_rotation(s1, s2):    
    if len(s1) != len(s2) or len(s1) == 0:
        return False    
    
    concat = s1 + s1    
    return is_substring(concat, s2)



class TestIsRotation(unittest.TestCase):
    def test_a_rotation_example(self):
        s1 = 'waterbottle'
        s2 = 'erbottlewat'
        self.assertTrue(is_rotation(s1, s2), True)


if __name__ == "__main__":
    unittest.main()
