class Solution_2:
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

class Solution:
    def lengthOfLongestSubstring(self,s):
        start = 0
        end =  0
        substring =""
        length =0 
        while  end <len(s):
            while start < end and s[end] in substring:
                start +=1
                substring = s[start:end]

            substring += s[end]
            length = max(length, len(substring))
            end +=1 
        return length

