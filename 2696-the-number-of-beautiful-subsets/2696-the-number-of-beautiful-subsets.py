class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0

        def dfs(index, path):
            nonlocal res
            if index == len(nums):
                if path:         
                    res += 1
                return

            dfs(index + 1, path)

            curr = nums[index]
            ok = True
            for val in path:
                if abs(val - curr) == k:
                    ok = False
                    break
            if ok:
                dfs(index + 1, path + [curr])

        dfs(0, [])
        return res
        