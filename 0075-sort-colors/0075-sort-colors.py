class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        index = 0

        for value in range(3):
            for _ in range(count[value]):
                nums[index] = value
                index += 1
