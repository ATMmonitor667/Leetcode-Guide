class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        index = 0,1,2,3,4, 5
        nums = [4,5,6,23,45] []
        [1,2,3]
        [], index = 0
        nums[index] = [1]
        path = [] or [1], index = 0
        nums[index] = [2] index = 1
        add [2] or not [2]
        path = [] or [2] or [1] or [1, 2] 
        index = 2
        num[index] = 3
        add [3] or not [3]
        path = [] or [3] or [2] or [2,3]  or [1] or [1,3] or [1, 2] or [1,2,3]
        index == 3
        res = []

        """
        res = []
        def dfs(index, path):
            if index > len(nums):
                return 
            if index == len(nums):
                res.append(path[:])
                return 
            else:
                dfs(index+1, path+[nums[index]])
                dfs(index+1, path)
        dfs(0, [])
        return res