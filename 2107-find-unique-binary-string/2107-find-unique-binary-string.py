class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        nums = set(nums)

        def dfs(index, word):
            if index == n:
                if word not in nums:
                    return word
                return None

            res = dfs(index + 1, word + "0")
            if res:
                return res

            res = dfs(index + 1, word + "1")
            if res:
                return res

            return None

        return dfs(0, "")