class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        This is a depth multiplication parsing problem
        there shoudl be a cursor as that is required in most depth problems
        keep a stack if '(' add it to the stack keep a depth stack 
        '(' then add another '(' then see that the next on is ')' matches with the
        top of the stack pop both and add a '1' and then see that a ')' ')' matches with a number so pop both of the top from the
        '((()()(())))'
        (1 1 2 )
        (2+1+1)*2 = 8
        (8) = 16
        [16]
        while number pop from the stack and add it to value 
        """
        word = [str(i) for i in s]
        stack = []
        for i in range(len(word)):
            print(stack)
            if '(' == word[i]:
                stack.append(word[i])
            elif ')' == word[i] and stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                num = 0
                while len(stack)>1 and word[i] == ')' and stack[-1] != '(':
                    digit = stack.pop()
                    num+=digit
                num = num*2
                stack.pop() #this pops the '('
                stack.append(num)
        return sum(stack)