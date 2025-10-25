class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        keysNeed = set()
        res = []
        start = (0, 0)

        # build grid and record start + keys
        for i in range(len(grid)):
            inter = []
            for j in range(len(grid[0])):
                ch = grid[i][j]
                inter.append(ch)
                if ch == '@':
                    start = (i, j)
                if ch.isalpha() and ch.islower():
                    keysNeed.add(ch)
            res.append(inter)

        m = len(res)
        n = len(res[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # BFS setup: (cost, r, c, keyMask)
        queue = deque([(0, start[0], start[1], 0)])
        seen = set([(start[0], start[1], 0)])
        allKeys = 0

        # bitmask for all needed keys
        for k in keysNeed:
            allKeys |= (1 << (ord(k) - ord('a')))

        while queue:
            cost, r, c, mask = queue.popleft()
            if mask == allKeys:
                return cost

            for (x, y) in dir:
                dx, dy = r + x, c + y
                if 0 <= dx < m and 0 <= dy < n:
                    curr = res[dx][dy]
                    if curr == '#':
                        continue
                    newMask = mask

                    # found key
                    if curr.isalpha() and curr.islower():
                        newMask |= (1 << (ord(curr) - ord('a')))

                    # found lock but don’t have key
                    if curr.isalpha() and curr.isupper() and not (newMask & (1 << (ord(curr.lower()) - ord('a')))):
                        continue

                    state = (dx, dy, newMask)
                    if state not in seen:
                        seen.add(state)
                        queue.append((cost + 1, dx, dy, newMask))

        return -1