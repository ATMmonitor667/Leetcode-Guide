class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
       
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()

        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]
        return t[-1]
            
        