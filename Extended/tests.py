 
# import unittest
# from main import Solution

# obj = Solution()


# class StringTests(unittest.TestCase):

#     def test_1(self):
#         """'9669' returns '9969'"""
#         self.assertEqual(obj.maximum69Number(9669), 9969)

#     def test_2(self):
#         """'9999' returns '9999'"""
#         self.assertEqual(obj.maximum69Number(9999), 9999)

#     def test_3(self):
#         """'9996' returns '9999'"""
#         self.assertEqual(obj.maximum69Number(9996), 9999)
 
# if __name__ == '__main__':
#     unittest.main()

import unittest
from main import Solution
obj = Solution()
class MinmaxTest(unittest.TestCase):
        def test_1(self):
            """ '9669' return '9969'"""
            self.assertEqual(obj.maximum69Number(9669),9969)
        def test_2(self):
                """ '9999' return '9999'"""
                self.assertEqual(obj.maximum69Number(9999),9999)
        def test_3(self):
            """ '9996' return '9999'"""

            self.assertEqual(obj.maximum69Number(9996),9999)

if __name__ == '__main__':
    unittest.main()