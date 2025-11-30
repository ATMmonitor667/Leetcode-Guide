class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0 for _ in range(len(nums))]
        odd = [i for i in nums if i % 2 == 1]
        even = [j for j in nums if j % 2 == 0]
        x = 0   
        y = 0  
        idx = 0
        while idx < len(nums):
            if idx % 2 == 0:
                ans[idx] = even[x]
                x += 1
            else:
                ans[idx] = odd[y]
                y += 1
            idx += 1

        return ans


        