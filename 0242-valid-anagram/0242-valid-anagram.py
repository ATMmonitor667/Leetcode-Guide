class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count1 = Counter(s)
        count2 = Counter(t)
        if len(count1) != len(count2):
            return False
        for k,v in count1.items():
            if v != count2[k]:
                return False
        return True
        