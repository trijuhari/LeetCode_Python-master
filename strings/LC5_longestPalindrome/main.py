# Given a string s, find the longest palindromic substring in s
# --- Example
# longestPalindrome("cbbd") --> "bb"
# longestPalindrome("abba") --> "abba"
# longestPalindrome("a") --> "a"

 

class Solution:
    def longestPalindrome(self, s):
        res = ""
        for  i in range(len(s)):
            current = self.expand_around_middle(s, i, i)
            in_between = self.expand_around_middle(s,i,i+1)
            res = max(res, current, in_between, key= len)
        return res
    def expand_around_middle(self,s,left, right):
        while left >= 0  and right < len(s) and s[left]== s[right]:
            left -=1 
            right +=1
        return s[left+1:right]

 