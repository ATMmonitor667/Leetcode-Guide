class Solution(object):
    def isHappy(self, n):
        seen = set()

        def digitSquareSum(n):
            total = 0
            while n:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = digitSquareSum(n)

        return True