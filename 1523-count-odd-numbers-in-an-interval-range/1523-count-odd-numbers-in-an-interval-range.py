class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high - low)//2 + 1 if high%2 == 1 or low%2 == 1 else (high - low)//2
        