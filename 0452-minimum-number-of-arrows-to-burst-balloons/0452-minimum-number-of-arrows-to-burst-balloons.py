class Solution(object):
    def findMinArrowShots(self, points):
        """
        1373
        :type points: List[List[int]]
        :rtype: int
        first sort the balloons
        and then find the intersection
        if the intersections are the same count does not increase
        once there is no overlap count +=1

        [1,6] [2,8] [7,12] [10,16]
        """
        if not points:
            return 0
        points.sort()
        count = 1
        arrow = [points[0][0], points[0][1]]
        for i in range(1, len(points)):
            start, end = points[i][0], points[i][1]
            if start <= arrow[1]:
                arrow = [start, min(arrow[1], end)]
            else:
                count += 1
                arrow = [start, end]
        return count
        