class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            cur = nums[i - 1]
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= cur:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - cur]

        return dp[n][target]