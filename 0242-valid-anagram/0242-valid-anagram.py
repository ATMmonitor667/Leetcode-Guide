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
        for i in t:
            if i in count1:
                count1[i]-=1
            if count1[i] == 0:
                del count1[i]
        return len(count1) == 0
        