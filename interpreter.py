#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mini-Scheme in ~200 lines: reader + eval + env + standard library.
# Features:
#  - Atoms: integers, floats, strings, booleans (#t/#f), symbols
#  - Lists: (a b c), quote, quasi omitted for brevity
#  - Special forms: quote, if, define, set!, lambda, begin, let, let*, letrec, and, or, cond
#  - Procedures: first-class (closures with lexical scope)
#  - Library: + - * /, = < <= > >=, cons car cdr list length null? pair? eq? equal?
#             number? symbol? boolean? string? display newline map filter foldl apply
# Limitations:
#  - No exact R5RS numeric tower; ints & floats only.
#  - No macro system; no tail-call elimination.

import math, operator as op
from collections import ChainMap

###############
#   Reader    #
###############

class ParseError(Exception): pass
Symbol = str

def tokenize(s: str):
    # Add spacing around parens and quotes; keep strings intact.
    tokens, i, n = [], 0, len(s)
    WH = ' \t\r\n'
    while i < n:
        c = s[i]
        if c in WH:
            i += 1; continue
        if c == ';':  # line comment
            while i < n and s[i] != '\n': i += 1
            continue
        if c == '"':  # string literal
            i += 1; buf = []
            while i < n:
                if s[i] == '\\':
                    i += 1
                    if i >= n: raise ParseError("unterminated string escape")
                    esc = s[i]; i += 1
                    mapping = {'n':'\n','t':'\t','r':'\r','"':'"','\\':'\\'}
                    buf.append(mapping.get(esc, esc))
                elif s[i] == '"':
                    i += 1; tokens.append('"'+''.join(buf)+'"'); break
                else:
                    buf.append(s[i]); i += 1
            else:
                raise ParseError("unterminated string")
            continue
        if c in '()\'':  # ' for (quote ...)
            if c == '\'':
                tokens.append('('); tokens.append('quote');  # sugar
                i += 1
                # Next token/expr will close by appending ')'
                # We'll rely on parse to add the ')'
                # Instead: push a marker; simpler is to insert after reading subexpr
                # For simplicity, handle it in reader below.
                # We'll flag here and let a tiny lookahead handle it:
                # Actually, do a tiny trick: emit a special marker and let reader expand.
                tokens[-1] = "'"
            else:
                tokens.append(c); i += 1
            continue
        # symbol/number/boolean
        j = i
        while j < n and s[j] not in WH + '()\'"':
            j += 1
        tokens.append(s[i:j])
        i = j
    return tokens

def read_from_tokens(tokens):
    # We implement a small recursive descent to S-expressions.
    # Special handling: quote sugar "'" expands to (quote X).
    i = 0
    def read_expr():
        nonlocal i
        if i >= len(tokens): raise ParseError("unexpected EOF")
        t = tokens[i]; i += 1
        if t == '(':
            lst = []
            while True:
                if i >= len(tokens): raise ParseError("unclosed '('")
                if tokens[i] == ')':
                    i += 1
                    return lst
                lst.append(read_expr())
        elif t == ')':
            raise ParseError("unexpected ')'")
        elif t == "'":   # expand into (quote <expr>)
            return ['quote', read_expr()]
        else:
            return atom(t)
    asts = []
    while i < len(tokens):
        asts.append(read_expr())
    return asts if len(asts) != 1 else asts[0]

def atom(t):
    # Booleans
    if t == '#t': return True
    if t == '#f': return False
    # String literal (already kept quoted)
    if len(t) >= 2 and t[0] == '"' and t[-1] == '"':
        return t[1:-1]
    # Number: int or float
    try:
        if '.' in t or 'e' in t or 'E' in t:
            return float(t)
        return int(t)
    except ValueError:
        return Symbol(t)

###############
#  Env & Proc #
###############

class Env(ChainMap):
    # ChainMap provides nested scopes naturally.
    def extend(self, vars, vals):
        return Env(dict(zip(vars, vals)), *self.maps)

class Procedure:
    __slots__ = ('params','body','env','name')
    def __init__(self, params, body, env, name='<lambda>'):
        self.params = params
        self.body = body
        self.env = env
        self.name = name
    def __call__(self, *args):
        local = dict(zip(self.params, args))
        new_env = Env(local, *self.env.maps)
        # (begin ...) semantics: evaluate body seq, return last
        result = None
        for expr in self.body:
            result = eval_s(expr, new_env)
        return result
    def __repr__(self):
        return f'<proc {self.name}/{len(self.params)}>'

###############
#  Primitives #
###############

def standard_env():
    env = Env({
        # arithmetic
        '+': lambda *a: sum(a),
        '-': lambda x, *y: x - sum(y) if y else -x,
        '*': lambda *a: math.prod(a) if a else 1,
        '/': lambda x, *y: op.truediv(x, math.prod(y)) if y else 1/x,
        'abs': abs, 'sqrt': math.sqrt, 'expt': pow, 'pow': pow,
        'remainder': op.mod, 'mod': op.mod, 'quotient': op.floordiv,
        # comparisons
        '=': lambda *a: all(a[i]==a[i+1] for i in range(len(a)-1)),
        '<': lambda *a: all(a[i]<a[i+1]  for i in range(len(a)-1)),
        '<=':lambda *a: all(a[i]<=a[i+1] for i in range(len(a)-1)),
        '>': lambda *a: all(a[i]>a[i+1]  for i in range(len(a)-1)),
        '>=':lambda *a: all(a[i]>=a[i+1] for i in range(len(a)-1)),
        # predicates
        'null?': lambda x: x==[],
        'pair?': lambda x: isinstance(x, list) and len(x)>0,
        'list?': lambda x: isinstance(x, list),
        'number?': lambda x: isinstance(x, (int,float)),
        'symbol?': lambda x: isinstance(x, str) and not isinstance(x, bool),
        'boolean?': lambda x: isinstance(x, bool),
        'string?': lambda x: isinstance(x, str),
        'eq?': lambda a,b: a is b,
        'equal?': lambda a,b: a==b,
        # lists
        'cons': lambda a,d: [a]+(d if isinstance(d, list) else [d]),
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'list': lambda *a: list(a),
        'length': lambda x: len(x),
        'append': lambda a,b: a+b,
        # I/O
        'display': lambda *a: print(*a, end=''),
        'newline': lambda : print(),
        # HOFs
        'map': lambda f, lst: list(map(f, lst)),
        'filter': lambda f, lst: list(filter(f, lst)),
        'foldl': lambda f, init, lst: _foldl(f, init, lst),
        'apply': lambda f, args: f(*args),
        # constants
        '#t': True, '#f': False,
    })
    return env

def _foldl(f, acc, lst):
    for x in lst:
        acc = f(acc, x)
    return acc

GLOBAL_ENV = standard_env()

###############
#   Evaluator #
###############

def eval_s(x, env=GLOBAL_ENV):
    # Evaluate Scheme expression in environment.
    if isinstance(x, Symbol):
        # variable reference
        for m in env.maps:
            if x in m: return m[x]
        raise NameError(f"unbound symbol: {x}")
    elif not isinstance(x, list):
        # literal
        return x
    if len(x) == 0:
        return []

    head = x[0]

    # Special forms
    if head == 'quote':  # (quote exp) or 'exp
        (_, exp) = x; return exp

    if head == 'if':     # (if test conseq alt)
        _, test, conseq, alt = x
        return eval_s(conseq, env) if truthy(eval_s(test, env)) else eval_s(alt, env)

    if head == 'begin':  # (begin e1 e2 ... en)
        result = None
        for exp in x[1:]:
            result = eval_s(exp, env)
        return result

    if head == 'define': # (define name expr) | (define (f args) body...)
        # function sugar
        if isinstance(x[1], list):
            _, sig, *body = x
            name = sig[0]; params = sig[1:]
            proc = Procedure(params, body, env, name=name)
            env.maps[0][name] = proc
            return name
        else:
            _, name, expr = x
            env.maps[0][name] = eval_s(expr, env)
            return name

    if head == 'set!':   # (set! var expr)
        _, name, expr = x
        val = eval_s(expr, env)
        for m in env.maps:
            if name in m:
                m[name] = val
                return val
        raise NameError(f"set!: unbound symbol {name}")

    if head == 'lambda': # (lambda (args...) body...)
        _, params, *body = x
        return Procedure(params, body, env)

    if head == 'let':    # (let ((v1 e1) (v2 e2) ...) body...)
        # Desugars into ((lambda (v1 v2 ...) body...) e1 e2 ...)
        _, bindings, *body = x
        vars = [b[0] for b in bindings]
        vals = [eval_s(b[1], env) for b in bindings]
        proc = Procedure(vars, body, env)
        return proc(*vals)

    if head == 'let*':   # sequential bindings
        _, bindings, *body = x
        new_env = Env({}, *env.maps)
        for b in bindings:
            new_env.maps[0][b[0]] = eval_s(b[1], new_env)
        result = None
        for exp in body:
            result = eval_s(exp, new_env)
        return result

    if head == 'letrec': # recursive bindings (procedures usually)
        _, bindings, *body = x
        frame = {}
        new_env = Env(frame, *env.maps)
        # Pre-bind names to placeholders
        for b in bindings:
            frame[b[0]] = None
        # Evaluate in new_env so lambdas capture it
        for b in bindings:
            frame[b[0]] = eval_s(b[1], new_env)
        result = None
        for exp in body:
            result = eval_s(exp, new_env)
        return result

    if head == 'and':
        # short-circuit
        for exp in x[1:]:
            val = eval_s(exp, env)
            if not truthy(val): return False
        return True

    if head == 'or':
        # short-circuit
        for exp in x[1:]:
            val = eval_s(exp, env)
            if truthy(val): return val
        return False

    if head == 'cond':
        # (cond (test expr...) ... (else expr...))
        for clause in x[1:]:
            tag = clause[0]
            if tag == 'else' or truthy(eval_s(tag, env)):
                result = None
                for exp in clause[1:]:
                    result = eval_s(exp, env)
                return result
        return None

    # Procedure call
    proc = eval_s(head, env)
    args = [eval_s(arg, env) for arg in x[1:]]
    return proc(*args)

def truthy(v):
    return v not in (False, [])

###############
#   REPL (opt)#
###############

def repl(prompt='scheme> '):
    import sys
    buf = ''
    depth = 0
    while True:
        try:
            line = input(prompt if depth == 0 else '... ')
        except EOFError:
            print(); break
        buf += '\n' + line
        # cheap balance check
        depth = buf.count('(') - buf.count(')')
        if depth > 0: continue
        if depth < 0:
            print("syntax error: too many ')'")
            buf, depth = '', 0; continue
        if buf.strip() == '': continue
        try:
            ast = read_from_tokens(tokenize(buf))
            val = eval_s(ast, GLOBAL_ENV)
            if val is not None:
                print(repr(val))
        except Exception as e:
            print("error:", e)
        buf = ''

if __name__ == '__main__':
    # Demo programs:
    program = r'''
    (define (square x) (* x x))
    (define (fact n) (if (= n 0) 1 (* n (fact (- n 1)))))
    (define (fib n) (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))

    (define xs (list 1 2 3 4 5))
    (display "xs length: ") (display (length xs)) (newline)

    (display "square 7 = ") (display (square 7)) (newline)
    (display "fact 6   = ") (display (fact 6)) (newline)
    (display "fib 10   = ") (display (fib 10)) (newline)

    (display "map square xs -> ") (display (map square xs)) (newline)

    (let ((a 2) (b 3))
      (display "let sum: ") (display (+ a b)) (newline))

    (let* ((a 2) (b (+ a 5)))
      (display "let* b: ") (display b) (newline))

    (letrec ((even? (lambda (n) (if (= n 0) #t (odd? (- n 1)))))
             (odd?  (lambda (n) (if (= n 0) #f (even? (- n 1))))))
      (display "even? 7 -> ") (display (even? 7)) (newline)
      (display "odd?  7 -> ") (display (odd? 7)) (newline))
    '''
    asts = read_from_tokens(tokenize(program))
    if isinstance(asts, list) and asts and isinstance(asts[0], list):
        for form in asts: eval_s(form, GLOBAL_ENV)
    else:
        eval_s(asts, GLOBAL_ENV)
    # Uncomment for interactive:
    # repl()
