class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        no = (high - low)//2
        if high%2 == 1 or low%2 ==1:
            return no+1
        return no
        