class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def reverse(num):
            return int(''.join(list(str(num))[::-1]))
        lookUp = set()
        for i in nums:
            lookUp.add(i)
            lookUp.add(reverse(i))
        return len(lookUp)

        