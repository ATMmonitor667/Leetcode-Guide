class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq = [0] * 26
        base = ord('a')

        for ch in s:
            freq[ord(ch) - base] += 1
        for ch in t:
            idx = ord(ch) - base
            freq[idx] -= 1
            if freq[idx] < 0:
                return False

        return True


        