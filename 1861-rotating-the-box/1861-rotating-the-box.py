class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        1) Transform each row by shifting all '#' to the right
           within segments separated by '*'
        2) Rotate the transformed matrix 90° clockwise
        """

        rows, cols = len(boxGrid), len(boxGrid[0])

        def rowTransform(arr):
            res = arr[:]                  
            start = 0
            for i in range(len(arr) + 1):
                if i == len(arr) or arr[i] == "*":
                    stones = arr[start:i].count("#")
                    for k in range(start, i):
                        res[k] = "."
                    for k in range(i - stones, i):
                        res[k] = "#"
                    start = i + 1
            return res

        transform = []
        for i in range(rows):
            transform.append(rowTransform(boxGrid[i]))
        rotated = [[None for _ in range(rows)] for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - 1 - r] = transform[r][c]

        return rotated
