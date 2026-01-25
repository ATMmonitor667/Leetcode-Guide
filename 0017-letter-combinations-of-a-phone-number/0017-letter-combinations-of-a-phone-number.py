class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        hashMap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        def dfs(i, path):
            if i == len(digits):
                res.append(path)
                return
            for char in hashMap[digits[i]]:
                dfs(i + 1, path + char) 
        
        dfs(0, '')
        return res