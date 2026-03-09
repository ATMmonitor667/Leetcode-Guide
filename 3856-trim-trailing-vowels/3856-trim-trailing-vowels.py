class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = set("aeiou")
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] in seen:
                continue
            return s[0:i+1]
        return ""