import unittest
from main import Solution, Solution_2

obj = Solution()
# obj = Solution_2()
 


class StringTests(unittest.TestCase):

    def test_1(self):
        """'A man, a plan, a canal: Panama' returns True"""
        self.assertEqual(obj.isPalindrome(
            'A man, a plan, a canal: Panama'), True)

    def test_2(self):
        """'love' returns False"""
        self.assertEqual(obj.isPalindrome('love'), False)

    def test_3(self):
        """'' returns True"""
        self.assertEqual(obj.isPalindrome(''), True)

    def test_4(self):
        """'_a__' returns True"""
        self.assertEqual(obj.isPalindrome('_a__'), True)


if __name__ == '__main__':
    unittest.main()
