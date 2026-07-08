class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = sum(1 for ch in s if ch == "1")
        left = 0
        best = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1

            best = max(best, left + right)

        return best