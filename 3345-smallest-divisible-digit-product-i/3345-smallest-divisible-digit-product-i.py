class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit(num):
            prod = 1
            while num>0:
                digit = num%10
                prod = digit * prod
                num = num//10
            return prod
        num = n
        while True:
            prod = digit(num)
            if prod%t == 0:
                return num
            num+=1
        