class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        pilelen = len(piles)-1
        pileSum = sum(piles)
        memo = {}
        def dfs(index, Alice):
            if index == pilelen:
                return Alice > pileSum - Alice
            if (index, Alice) in memo:
                return memo[(index, Alice)]
            else:
                return dfs(index+1, Alice + piles[index]) or dfs(index+1, Alice + piles[pilelen-index])
        return dfs(0, 0)