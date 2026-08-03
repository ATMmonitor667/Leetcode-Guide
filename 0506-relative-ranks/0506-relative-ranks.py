class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        scores = score
        sortedScores = sorted(scores, reverse = True)
        hashMap = {}
        for index, value in enumerate(sortedScores):
            hashMap[value] = index
        ans = []
        for i in range(len(scores)):
            if hashMap[scores[i]] == 0:
                ans.append("Gold Medal")
            elif hashMap[scores[i]] == 1:
                ans.append("Silver Medal")
            elif hashMap[scores[i]] == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(hashMap[scores[i]] + 1))
        return ans
        