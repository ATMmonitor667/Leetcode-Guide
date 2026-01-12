class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(i, path):
            if i == len(nums):
                res.append(path[:])
                return 
            else:
                dfs(i+1,path + [nums[i]])
                dfs(i+1,path)
        dfs(0,[])
        return res


        