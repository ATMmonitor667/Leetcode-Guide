class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        has = {}
        for num in nums:
            has[num] = has.get(num, 0) + 1
        nums.sort(key=lambda x: (has[x], -x))
        return nums
