class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        myDict = {}
        for x in nums:
            myDict[x] = myDict.get(x, 0) + 1

        sorted_items = sorted(myDict.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(min(k, len(sorted_items))):
            res.append(sorted_items[i][0])
        return res

        
        