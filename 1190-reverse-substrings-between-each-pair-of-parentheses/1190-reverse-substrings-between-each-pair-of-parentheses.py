class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        current_string = ""
        
        for char in s:
            if char == '(':
                stack.append(current_string)
                current_string = ""
            elif char == ')':
                reversed_part = current_string[::-1]
                prefix = stack.pop()
                current_string = prefix + reversed_part
            else:
                current_string += char
                
        return current_string