class Solution(object):
    class UnionFind():
        def __init__(self, vals):
            self.parent = {v: v for v in vals}
            self.rank   = {v: 1 for v in vals}
        def find(self, x):
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        def union(self, a, b):
            rootA = self.find(a)
            rootB = self.find(b)
            if rootA == rootB:
                return
            else:
                if a not in self.parent or b not in self.parent:
                    return
                if self.rank[rootB] > self.rank[rootA]:
                    rootA, rootB = rootB, rootA
                self.parent[rootB] = rootA
                self.rank[rootA]+= self.rank[rootB]
                return True
        def returnMaxRank(self):
            maxi = 0
            for k,v in self.rank.items():
                if maxi < v:
                    maxi = v
            print(self.rank)
            return maxi
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums = list(set(nums))          # remove dups
        DSU = self.UnionFind(nums)
        numset = set(nums)
        for x in nums:
            if x - 1 in numset:
                DSU.union(x, x - 1)
        return DSU.returnMaxRank()