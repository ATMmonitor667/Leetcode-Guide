class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0: -1}
        prefix = 0

        for i, x in enumerate(nums):
            prefix += x
            rem = prefix % k if k != 0 else prefix  

            if rem in seen:
                if i - seen[rem] >= 2:   
                    return True
            else:
                seen[rem] = i

        return False


        