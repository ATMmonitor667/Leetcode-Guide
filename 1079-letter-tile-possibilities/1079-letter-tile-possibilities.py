class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        used = [False] * len(tiles)
        tiles = sorted(tiles)  

        def dfs(path):
            if path:
                res.add(path)
            for i in range(len(tiles)):
                if used[i]:
                    continue
                if i > 0 and tiles[i] == tiles[i-1] and not used[i-1]:
                    continue
                used[i] = True
                dfs(path + tiles[i])
                used[i] = False
        dfs("")
        return len(res)

        