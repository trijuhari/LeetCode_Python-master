import unittest
from main import Solution
obj = Solution()

class Backspacestring(unittest.TestCase):
    def test_1(self):
       self.assertEqual(obj.backspaceCompare("ab#c", "ad#c"),True) 
    def test_2(self):
       self.assertEqual(obj.backspaceCompare("ab##",   "c#d#"),True) 
    def test_3(self):
       self.assertEqual(obj.backspaceCompare( "a#c",  "b"),FalseTELE) 

if __name__ == '__main__':
    unittest.main()