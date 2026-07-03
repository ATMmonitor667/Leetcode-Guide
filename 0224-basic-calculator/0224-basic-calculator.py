class Parser:
    def __init__(self):
        self.index = 0
        self.value = 0
        self.s = ""

    def parse(self, s):
        self.s = s
        self.index = 0
        return self.expr()

    def _skip_spaces(self):
        while self.index < len(self.s) and self.s[self.index] == " ":
            self.index += 1

    def _apply(self, op, a, b):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return a // b
        return 0

    def number(self):
        self._skip_spaces()
        self.value = 0
        while self.index < len(self.s) and self.s[self.index].isdigit():
            self.value = self.value * 10 + int(self.s[self.index])
            self.index += 1
        return self.value

    def factor(self):
        self._skip_spaces()
        if self.index < len(self.s) and self.s[self.index] == "(":
            self.index += 1
            val = self.expr()
            self._skip_spaces()
            if self.index < len(self.s) and self.s[self.index] == ")":
                self.index += 1 
            return val
        return self.number()

    def term(self):
        result = self.factor()
        self._skip_spaces()
        while self.index < len(self.s) and self.s[self.index] in "*/":
            op = self.s[self.index]
            self.index += 1
            result = self._apply(op, result, self.factor())
            self._skip_spaces()
        return result

    def expr(self):
        result = self.term()
        self._skip_spaces()
        while self.index < len(self.s) and self.s[self.index] in "+-":
            op = self.s[self.index]
            self.index += 1
            result = self._apply(op, result, self.term())
            self._skip_spaces()
        return result

class Solution(object):
    def calculate(self, s):
        solver = Parser()
        return solver.parse(s)