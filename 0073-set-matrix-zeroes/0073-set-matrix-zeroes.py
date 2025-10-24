class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
      seenx = set([])
      seeny = set([])
      for i in range(len(matrix)):
          for j in range(len(matrix[i])):
              if matrix[i][j] == 0:
                  seenx.add(i)
                  seeny.add(j)
      for i in range(len(matrix)):
          for j in range(len(matrix[i])):
              if i in seenx  or j in seeny:
                  matrix[i][j] = 0
      return matrix
        