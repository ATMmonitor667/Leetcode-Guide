class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        granted both arrays are sorted

        """
        houses.sort()
        heaters.sort()
        j = 0
        ans = 0
        for h in houses:
            while j + 1 < len(heaters) and abs(h - heaters[j + 1]) <= abs(h - heaters[j]):
                j += 1
            ans = max(ans, abs(h - heaters[j]))

        return ans
