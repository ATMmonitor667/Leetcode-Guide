class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {0: 1}
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            rem = prefix % k
            ans += freq.get(rem, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return ans