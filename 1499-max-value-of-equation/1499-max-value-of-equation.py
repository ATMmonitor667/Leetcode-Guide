class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        queue = deque()
        maxVal = float('-inf')
        for x,y in points:
            while queue and abs(queue[0][0] - x) > k:
                queue.popleft()
            
            if queue:
                maxVal = max(maxVal, y+x+queue[0][1])
            
            while queue and queue[-1][1] <= y-x:
                queue.pop()
            
            queue.append((x, y-x))
            
        return maxVal