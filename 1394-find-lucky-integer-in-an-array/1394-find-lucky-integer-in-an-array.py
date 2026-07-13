class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hold = 0

        count = Counter(arr)
        for k,v in count.items():
            if k == v:
                hold = max(hold,k)
                

        return hold if hold != 0 else -1 