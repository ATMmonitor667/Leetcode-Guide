class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        0 0 0 0 0 0 0 0 0 0 = 0 means off and 1 means on
        1 0 1 0 1 0 1 0 1 0 =  
        Test for small cases and then go to larger ones
        1, turn = 1 bulb
        1 0 = 1 bulb 
        1 0 0 = 1 bulb
        1 0 0 1 =  2 bulbs
        1 0 0 1 1 = 3 bulbs
        1 0 0 1 1 1 = 4 bulbs
        1 0 0 1 1 1 1 = 5 bulbs
        1 0 0 1 1 1 1 0 = 5 bulbs
        1 0 0 1 1 1 1 0 1 = 6 
        1 0 0 1 1 1 1 0 1 0 = 6
        1 0 0 1 1 1 1 0 1 0 
        """
        return int(sqrt(n))