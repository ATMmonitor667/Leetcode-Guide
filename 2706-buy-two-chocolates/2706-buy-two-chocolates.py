class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        val = prices[0]+prices[1]
        if money >= val:
            return money - val
        return money 
        