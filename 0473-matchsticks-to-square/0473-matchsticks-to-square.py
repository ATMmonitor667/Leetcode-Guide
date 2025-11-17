class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        target = sum(matchsticks)//4
        def equals(index, one, two, three, four):
            if index == len(matchsticks):
                return one == two == three == four

            stick = matchsticks[index]
            if one > target:
                return False
            if two > target:
                return False
            if three > target:
                return False
            if four > target:
                return False

            return (
                equals(index + 1, one + stick, two, three, four) or
                equals(index + 1, one, two + stick, three, four) or
                equals(index + 1, one, two, three + stick, four) or
                equals(index + 1, one, two, three, four + stick)
            )
        return equals(0,0,0,0,0)