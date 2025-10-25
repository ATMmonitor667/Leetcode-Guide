class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        runningSum = 0
        l = 0
        maxSum = 0
        for r in range(len(fruits)):
            
            window[fruits[r]] = window.get(fruits[r],0)+1
            while len(window) > 2:
                window[fruits[l]]-=1
                if window[fruits[l]] == 0:
                    window.pop(fruits[l])
                
                l+=1
            maxSum = max(maxSum, r-l+1)
        return maxSum