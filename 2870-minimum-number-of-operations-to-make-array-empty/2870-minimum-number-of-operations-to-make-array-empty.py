class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        count = Counter(nums)
        for key, value in count.items():
            if value == 1:
                return -1
            if value%3 == 0:
                total += value/3
            else:
                total += value//3+1
        return total

        