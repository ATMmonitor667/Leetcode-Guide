class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
    
        graph = {}

        for start, end in paths:
            graph[start] = end

        def dfs(node):
            if node not in graph:
                return node
            return dfs(graph[node])

        return dfs(paths[0][0])