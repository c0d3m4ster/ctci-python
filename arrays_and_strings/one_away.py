import unittest


# One Away: 
# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are
# one edit (or zero edits) away.
#
# EXAMPLE
# pale, pal   -> true
# pales, pale -> true
# pale, bale  -> true
# pale, bake  -> false

def one_insert(s1, s2):
    # we assume s1 is one character longer
    i, j = 0, 0
    count = 0
    while (i<len(s1)) and (j<len(s2)):
        if s1[i]!=s2[j]:
            count+=1
            i+=1
        else:
            i+=1
            j+=1
        if count>1:
            return False
    return True

def one_away(s1, s2):
    len1, len2 = len(s1), len(s2)

    # If the length difference is more than 1, return False
    if abs(len1 - len2)>1:
        return False
    
    # check for replace a character
    if len1==len2:
        count = 0
        for i in range(len1):
            if s1[i]!=s2[i]:
                count+=1
            if count>1:
                return False
        return True
    # check for remove or insert a character             
    else:
        if len1>len2:
            return one_insert(s1, s2)
        else:
            return one_insert(s2, s1)


# testing the function "one_away"
class TestOneAway(unittest.TestCase):

    def test_one_insert(self):
        self.assertTrue(one_away('pale', 'ple'), True)

    def test_one_remove(self):
        self.assertTrue(one_away('pales', 'pale'), True)
    
    def test_one_replace(self):
        self.assertTrue(one_away('pale', 'bale'), True)
    
    def test_two_replace(self):
        self.assertFalse(one_away('pale', 'bake'), False)
    
    def test_two_insert(self):
        self.assertFalse(one_away('pal', 'palee'), False)
    
    def test_two_remove(self):
        self.assertFalse(one_away('pale', 'pa'), False)


if __name__ == '__main__':
    unittest.main()
