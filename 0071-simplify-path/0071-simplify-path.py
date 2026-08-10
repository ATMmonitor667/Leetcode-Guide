class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = ['']  
        path = path.split('/')
        for i in path:
            if i == '' or i == '.':
                continue
            elif i == '..':
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(i)

        word = '/'.join(stack)

        if len(word) == 0:
            return '/'
        return word
      