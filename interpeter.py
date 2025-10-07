class LispInterpreter:
    def __init__(self, src):
        self.tokens = self.tokenize(src)
        self.i = 0

    def tokenize(self, s):
        s = s.replace('(', ' ( ').replace(')', ' ) ')
        return s.split()

    def get(self):
        tok = self.tokens[self.i]; self.i+=1; return tok

    def peek(self):
        return self.tokens[self.i] if self.i < len(self.tokens) else None

    def eval(self, env):
        tok = self.get()
        if tok == '(':
            op = self.get()
            if op == 'add':
                a = self.eval(env)
                b = self.eval(env)
                assert self.get() == ')'
                return a+b
            if op == 'let':
                env.append(env[-1].copy())
                while True:
                    if self.peek() == ')':  # end
                        self.get(); val = 0; env.pop(); return val
                    # lookahead: if next token is var name and next after is not ')'
                    name = self.get()
                    if self.peek() == ')':
                        # actually final expr
                        val = self.value_of(name, env)
                        assert self.get()==')'; env.pop(); return val
                    val = self.eval(env)
                    env[-1][name]=val
            else: # fallback
                self.i-=1
                v = self.eval(env)
                assert self.get()==')'
                return v
        else:
            return self.value_of(tok, env)

    def value_of(self, t, env):
        if t.lstrip('-').isdigit():
            return int(t)
        for scope in reversed(env):
            if t in scope: return scope[t]
        return 0

def evaluate(expr):
    return LispInterpreter(expr).eval([{}])

print(evaluate("(add 1 (add 56 3))"))