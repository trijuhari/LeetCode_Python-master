class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hasil_s = self.stack_s(s)
        hasil_t = self.stack_s(t)
        return  hasil_s == hasil_t
    
    @staticmethod
    def stack_s(s):
        stack_s = []
        for char in s:
            if char != '#' : 
                stack_s.append(char)
            else:
                stack_s.pop()

        return ( "".join(sorted(stack_s))   )

    