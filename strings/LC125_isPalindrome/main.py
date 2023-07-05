class Solution:
    def isPalindrome(self, s):
        palindrome = ''
        for i in  s.lower():
            if i.isalnum() == True:
                palindrome = palindrome + i 
        return palindrome == palindrome[::-1]
            
