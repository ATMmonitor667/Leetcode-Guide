class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        
        neg = n < 0
        n = abs(n)

        product = 1.0

        while n > 0:
            if n % 2 == 1:      
                product *= x
            x *= x             
            n //= 2             

        return 1.0 / product if neg else product

        