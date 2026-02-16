class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        
        if rootA == rootB:
            return False
            
        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA
            
        self.parent[rootB] = rootA
        self.rank[rootA] += self.rank[rootB]
        return True

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        # We know there are exactly 26 lowercase English letters.
        dsu = DSU(26)
        
        # Pass 1: Build the Truth (Process all '==' equations)
        for eq in equations:
            # eq[1] will be '=' for "==" and '!' for "!="
            if eq[1] == '=':
                # Map 'a'-'z' to 0-25
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                dsu.union(u, v)
                
        # Pass 2: Find the Lies (Process all '!=' equations)
        for eq in equations:
            if eq[1] == '!':
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                
                # If they share the same root, they are mathematically equal.
                # But this equation claims they are not. Contradiction found.
                if dsu.find(u) == dsu.find(v):
                    return False
                    
        return True





        