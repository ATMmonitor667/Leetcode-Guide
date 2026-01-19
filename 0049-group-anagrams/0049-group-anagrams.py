class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        What is the best way to do this?
        """
        graph = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            graph[key].append(s)
        return [val for val in graph.values()]