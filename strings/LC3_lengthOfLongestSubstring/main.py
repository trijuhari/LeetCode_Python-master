class Solution:
    def lengthOfLongestSubstring(self, s):
        length =0
        l = 0
        seen ={}
        for i in range (len(s)):
            char = s[i]
            if char in seen and seen[char] >= l :
                l = seen[char] + 1 
            else:
                length = max(length, i -l+1)
            seen[char] = i
        return length
