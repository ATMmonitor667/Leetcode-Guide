class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def rev(i):
            num = int(str(i)[::-1])
            return num
        if num == 0:
            return True 

        for i in range(num):
            if i + rev(i) == num:
                return True
        return False
