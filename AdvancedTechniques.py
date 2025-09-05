from typing import List, Tuple, Callable
from collections import deque
import math
import random

INF = 10**18

class MosAlgo:
    def __init__(self, arr: List[int]):
        self.a = arr
        self.n = len(arr)
        self.B = max(1, int(self.n ** 0.5))
        # frequency map (for distinct count demo)
        self.freq = {}
        self.distinct = 0
        self.L = 0
        self.R = -1

    def _add(self, x: int):
        c = self.freq.get(x, 0)
        if c == 0: self.distinct += 1
        self.freq[x] = c + 1

    def _rem(self, x: int):
        c = self.freq[x]
        if c == 1:
            self.distinct -= 1
            del self.freq[x]
        else:
            self.freq[x] = c - 1

    def _move(self, l: int, r: int):
        while self.R < r:
            self.R += 1
            self._add(self.a[self.R])
        while self.R > r:
            self._rem(self.a[self.R])
            self.R -= 1
        while self.L < l:
            self._rem(self.a[self.L])
            self.L += 1
        while self.L > l:
            self.L -= 1
            self._add(self.a[self.L])

    def solve(self, queries: List[Tuple[int,int,int]]) -> List[int]:
        """
        queries: list of (l, r, idx). Returns ans in original order.
        """
        def key(q):
            b = q[0] // self.B
            return (b, q[1] if b % 2 == 0 else -q[1])  # little Hilbert-like tweak

        qs = sorted(queries, key=key)
        ans = [0]*len(queries)
        for l, r, i in qs:
            self._move(l, r)
            ans[i] = self.distinct
        return ans

# Usage:
# arr = [...]
# queries = [(l, r, idx), ...]
# mo = MosAlgo(arr)
# result = mo.solve(queries)


class SegTreePointSum:
    def __init__(self, n: int):
        self.N = 1
        while self.N < n: self.N <<= 1
        self.seg = [0]*(2*self.N)

    def point_set(self, i: int, v: int):
        i += self.N
        self.seg[i] = v
        i >>= 1
        while i:
            self.seg[i] = self.seg[i<<1] + self.seg[i<<1|1]
            i >>= 1

    def range_sum(self, l: int, r: int) -> int:
        l += self.N; r += self.N
        s = 0
        while l <= r:
            if l & 1: s += self.seg[l]; l += 1
            if not (r & 1): s += self.seg[r]; r -= 1
            l >>= 1; r >>= 1
        return s

class HLD:
    def __init__(self, n: int, adj: List[List[int]], values: List[int]):
        self.n = n
        self.adj = adj
        self.parent = [-1]*n
        self.depth  = [0]*n
        self.size   = [0]*n
        self.heavy  = [-1]*n
        self.head   = [0]*n
        self.pos    = [0]*n
        self.curpos = 0

        # 1) dfs to compute size & heavy child
        def dfs(u: int, p: int):
            self.parent[u] = p
            self.size[u] = 1
            maxsz = 0
            for v in self.adj[u]:
                if v == p: continue
                self.depth[v] = self.depth[u] + 1
                dfs(v, u)
                if self.size[v] > maxsz:
                    maxsz = self.size[v]
                    self.heavy[u] = v
                self.size[u] += self.size[v]
        dfs(0, -1)

        # 2) decompose into head chains
        def decompose(u: int, h: int):
            self.head[u] = h
            self.pos[u] = self.curpos
            self.curpos += 1
            if self.heavy[u] != -1:
                decompose(self.heavy[u], h)
                for v in self.adj[u]:
                    if v != self.parent[u] and v != self.heavy[u]:
                        decompose(v, v)
        decompose(0, 0)

        # 3) build segment tree on base array
        self.st = SegTreePointSum(n)
        for u in range(n):
            self.st.point_set(self.pos[u], values[u])

    def path_sum(self, a: int, b: int) -> int:
        res = 0
        while self.head[a] != self.head[b]:
            if self.depth[self.head[a]] < self.depth[self.head[b]]:
                a, b = b, a
            h = self.head[a]
            res += self.st.range_sum(self.pos[h], self.pos[a])
            a = self.parent[h]
        # same head
        if self.depth[a] > self.depth[b]:
            a, b = b, a
        res += self.st.range_sum(self.pos[a], self.pos[b])
        return res

    def point_update(self, u: int, new_val: int):
        self.st.point_set(self.pos[u], new_val)

# Usage:
# n, adj = ...
# values = initial node values
# hld = HLD(n, adj, values)
# hld.point_upda_

def binary_search_on_answer(lo: int, hi: int, feasible: Callable[[int], bool]) -> int:
    """
    Returns minimal x in [lo, hi] with feasible(x)=True; assumes monotone.
    If none feasible, returns hi+1.
    """
    ans = hi + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

# Usage:
# def feasible(x): ...
# res = binary_search_on_answer(0, 10**9, feasible)

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    dq = deque()  # stores indices, values decreasing
    out = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

def sliding_window_min(nums: List[int], k: int) -> List[int]: #=> Very important strategy, needs to be improved upon and mastered.
    dq = deque()  # increasing
    out = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] >= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

#This here is too advanced technique that I need to work on and master.

class LCT:
    class Node:
        __slots__ = ("ch", "p", "rev", "val", "sum", "is_root")
        def __init__(self, val=0):
            self.ch = [None, None]  # left,right
            self.p = None           # parent in aux tree
            self.rev = False        # lazy reverse flag
            self.val = val          # node value
            self.sum = val          # aggregate on splay
            self.is_root = True     # whether this node is a root of aux tree

    def __init__(self, n: int, values: List[int]=None):
        self.n = n
        self.t = [self.Node(0) for _ in range(n)]
        if values:
            for i, v in enumerate(values):
                self.t[i].val = v
                self._pull(self.t[i])

    # ---------- splay helpers ----------
    def _is_right(self, x):
        return x.p and x.p.ch[1] is x

    def _push(self, x):
        if x and x.rev:
            x.ch[0], x.ch[1] = x.ch[1], x.ch[0]
            if x.ch[0]: x.ch[0].rev ^= True
            if x.ch[1]: x.ch[1].rev ^= True
            x.rev = False

    def _pull(self, x):
        x.sum = x.val
        for c in x.ch:
            if c: x.sum += c.sum

    def _rotate(self, x):
        p = x.p
        gp = p.p
        d = 1 if p.ch[1] is x else 0
        b = x.ch[d ^ 1]

        # push down before rotate
        self._push(p); self._push(x)

        # rotation
        x.ch[d ^ 1] = p
        p.p = x
        p.ch[d] = b
        if b: b.p = p

        x.p = gp
        if gp:
            if gp.ch[0] is p: gp.ch[0] = x
            elif gp.ch[1] is p: gp.ch[1] = x
        x.is_root = p.is_root
        p.is_root = False

        self._pull(p); self._pull(x)

    def _splay(self, x):
        self._push(x)
        while not x.is_root:
            p = x.p
            gp = p.p
            if not p.is_root:
                if (p.ch[0] is x) == (gp.ch[0] is p):
                    self._rotate(p)
                else:
                    self._rotate(x)
            self._rotate(x)

    def _access(self, x):
        """Expose path to root; after this, x is the rightmost node on its aux chain."""
        last = None
        v = x
        while v:
            self._splay(v)
            if v.ch[1]:
                v.ch[1].is_root = True
                v.ch[1].p = v
            v.ch[1] = last
            if last:
                last.is_root = False
                last.p = v
            self._pull(v)
            last = v
            v = v.p
        self._splay(x)
        return last

    def _evert(self, x):
        self._access(x)
        x.rev ^= True
        self._push(x)
        self._pull(x)

    def _find_root(self, x):
        self._access(x)
        while x.ch[0]:
            self._push(x)
            x = x.ch[0]
        self._splay(x)
        return x

    # ---------- API ----------
    def make_root(self, u: int):
        self._evert(self.t[u])

    def connected(self, u: int, v: int) -> bool:
        ru = self._find_root(self.t[u])
        rv = self._find_root(self.t[v])
        return ru is rv

    def link(self, u: int, v: int):
        """Link u as child of v (assumes different trees)."""
        if self.connected(u, v):
            return  # already connected; ignore or raise
        self.make_root(u)
        # Now u is root of its tree
        self.t[u].p = self.t[v]  # preferred parent pointer
        # Access to update aux structures
        self._access(self.t[u])

    def cut(self, u: int, v: int):
        """Cut the edge u—v if it exists."""
        self.make_root(u)
        self._access(self.t[v])
        # Now path u..v is preferred; edge must be direct
        # v's left child should be u and u has no right child
        x = self.t[v]
        if x.ch[0] is self.t[u] and self.t[u].ch[1] is None:
            x.ch[0].p = None
            x.ch[0].is_root = True
            x.ch[0] = None
            self._pull(x)

    def set_val(self, u: int, value: int):
        x = self.t[u]
        self._access(x)
        x.val = value
        self._pull(x)

    def path_sum(self, u: int, v: int) -> int:
        self.make_root(u)
        self._access(self.t[v])
        return self.t[v].sum

# Usage:
# lct = LCT(n, values)  # values optional
# lct.link(u, v); lct.cut(u, v)
# lct.set_val(x, val)
# s = lct.path_sum(u, v)
