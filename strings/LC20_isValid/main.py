class Solution:
    def isValid(self, s):
        stack = []
        pair_hash_map = {"(": ")", "{":"}","[":"]"}
        for char in   s:
            if   char in pair_hash_map:
                stack.append(char)
                print(stack)
            elif len(stack) == 0 or pair_hash_map[stack.pop()] != char:
                return False
        return  len(stack) == 0
# a = Solution()
# print(a.isValid('([{}])'))