class Solution:
    def isPalindrome(self, s):
        palindrome = ''
        for i in  s.lower():
            if i.isalnum() == True:
                palindrome = palindrome + i 
        return palindrome == palindrome[::-1]
            
class Solution_2:
    def isPalindrome(self,s):
        import re
        s = re.sub(r'[\W_]','',s).lower()
        left = 0
        right = len(s) -1
        while  left < right:
            if s[left] != s[right]:
                return False
            left+= 1 
            right -=1
        return True
        