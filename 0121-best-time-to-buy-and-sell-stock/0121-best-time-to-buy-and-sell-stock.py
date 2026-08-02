class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        l = 0
        r = len(prices)-1
        globalAnswer = 0
        prefix = [prices[0]]
        suffix = [prices[-1]]
        prefixIndex = set()
        suffixIndex = set()
        for i in range(len(prices)):
            if prefix[-1] > prices[i]:
                prefix.append(prices[i])
                prefixIndex.add(i)
        suffix = [(prices[-1], len(prices)-1)]
        for i in range(len(prices)-1, -1, -1):
            if suffix[-1] < prices[i]:
                suffix.append(prices[i])
                suffixIndex.add(i)
        val = 0
        
        print(suffix, "why")
        print(prefix, "hi")
        '''
        minprefix = [prices[0]]
        for i in range(1, len(prices)):
            minprefix.append(min(minprefix[-1], prices[i]))
        maxi = float('-inf')
        for i in range(len(prices)):
            maxi = max(maxi, prices[i] - minprefix[i])
        return maxi 