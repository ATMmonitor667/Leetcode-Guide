class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        ans = 0
        score = 0
        iterations = len(piles)/3
        j = len(piles)-1
        while iterations:
            score += piles[j-1]
            j-=2
            iterations -=1
        return score