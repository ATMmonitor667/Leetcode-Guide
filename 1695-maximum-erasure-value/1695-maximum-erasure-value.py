class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        globalScore = 0
        window = set()
        score = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in window:
                score-=nums[l]
                window.remove(nums[l])
                l+=1
            score+= nums[r]
            window.add(nums[r])
            globalScore = max(globalScore, score)
        return globalScore
                


