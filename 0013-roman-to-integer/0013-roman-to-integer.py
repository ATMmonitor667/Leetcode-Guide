class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
        total = 0
        for i in range(len(s)-1):
            if seen[s[i]] < seen[s[i+1]]:
                total -= seen[s[i]]
            else:
                total += seen[s[i]]
        total += seen[s[-1]]
        return total

        