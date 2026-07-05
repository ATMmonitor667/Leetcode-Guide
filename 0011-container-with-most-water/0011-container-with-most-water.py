class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height)-1
        nums = height
        while i < j:
            area = min(nums[i], nums[j]) * (j - i)
            maxArea = max(maxArea, area)

            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1
        return maxArea


        