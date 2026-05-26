class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        seen = set()

        def dfs(i):

            if i == len(nums):
                word = ''.join([str(i) for i in nums])
                if word not in seen:
                    seen.add(word)
                    res.append(nums[:])
                return

            for j in range(i, len(nums)):

                nums[i], nums[j] = nums[j], nums[i]

                dfs(i + 1)

                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res
        