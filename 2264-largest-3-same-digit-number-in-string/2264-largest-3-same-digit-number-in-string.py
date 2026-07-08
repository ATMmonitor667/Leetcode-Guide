class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        lookup = [str(d) * 3 for d in range(9, -1, -1)]

        for k in lookup:
            if k in num:
                return k

        return ""
                