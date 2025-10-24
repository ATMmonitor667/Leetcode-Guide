class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def construct(arr):
            val = 10
            ans = 0
            for i in range(len(arr)):
                ans = ans*val+arr[i]
                
            return ans+1
        def modify(num):
            ans = []
            while num:
                print(ans, num)
                digit = num%10
                num = num//10
                ans.append(digit)
            val = ans[::-1]
            return val
        return modify(construct(digits))
