class Solution(object):
    def isValid(self, s):
        myMap = { '(': ')', '[':']', '{':'}' }
        stack = []
        
        for char in s:
            if char in myMap:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                last_opener = stack.pop()
                
                if myMap[last_opener] != char:
                    return False
                    
        return len(stack) == 0
