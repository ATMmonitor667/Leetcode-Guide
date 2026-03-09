class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        ans = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                sum = 1
                atual = num + 1
                while atual in num_set:
                    sum += 1
                    atual += 1
                ans = max(ans, sum)

        return ans