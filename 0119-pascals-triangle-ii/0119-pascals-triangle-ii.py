class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = [[1],[1,1]]
        index = 1
        while index < rowIndex:
            currentRow = triangle[-1]
            newRow = [1]
            for i in range(1,len(currentRow)):
                newRow.append(currentRow[i-1]+currentRow[i])
            triangle.append(newRow+[1])
            index+=1
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        return triangle[-1]