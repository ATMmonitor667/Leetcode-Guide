class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in range(len(digits)):
            number = number*10+digits[i]
        ans = deque([])
        number = number + 1
        while number:
            digit = number%10
            ans.appendleft(digit)
            number = number / 10
        return list(ans)