import random
from typing import List, Optional, Tuple

INF = 10**18

# ------------------------------------------------------------
# 1) Segment Tree with Lazy Propagation (range add, range sum)
# ------------------------------------------------------------
class LazySegTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n: self.size <<= 1
        self.seg = [0]*(2*self.size)
        self.lz  = [0]*(2*self.size)
        # build
        for i, v in enumerate(arr):
            self.seg[self.size+i] = v
        for i in range(self.size-1, 0, -1):
            self.seg[i] = self.seg[i<<1] + self.seg[i<<1|1]
    def _apply(self, idx: int, add: int, length: int):
        self.seg[idx] += add * length
        self.lz[idx]  += add
    def _push(self, idx: int, length: int):
        if self.lz[idx]:
            mid_len = length // 2
            self._apply(idx<<1,     self.lz[idx], mid_len)
            self._apply(idx<<1|1,   self.lz[idx], length - mid_len)
            self.lz[idx] = 0
    def _range_add(self, idx: int, l: int, r: int, ql: int, qr: int, val: int):
        if qr < l or r < ql: return
        if ql <= l and r <= qr:
            self._apply(idx, val, r-l+1)
            return
        self._push(idx, r-l+1)
        m = (l+r)//2
        self._range_add(idx<<1, l, m, ql, qr, val)
        self._range_add(idx<<1|1, m+1, r, ql, qr, val)
        self.seg[idx] = self.seg[idx<<1] + self.seg[idx<<1|1]
    def range_add(self, l: int, r: int, val: int):
        self._range_add(1, 0, self.size-1, l, r, val)
    def _range_sum(self, idx: int, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or r < ql: return 0
        if ql <= l and r <= qr: return self.seg[idx]
        self._push(idx, r-l+1)
        m = (l+r)//2
        return self._range_sum(idx<<1, l, m, ql, qr) + self._range_sum(idx<<1|1, m+1, r, ql, qr)
    def range_sum(self, l: int, r: int) -> int:
        return self._range_sum(1, 0, self.size-1, l, r)


# ------------------------------------------------------------
# 2) Fenwick Tree (Binary Indexed Tree)
#    - point add, prefix sum
#    - optional range add / range sum via two BITs
# ------------------------------------------------------------
class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.ft = [0]*(n+1)
    def add(self, i: int, delta: int):
        # 0-indexed external; internally 1-indexed
        i += 1
        while i <= self.n:
            self.ft[i] += delta
            i += i & -i
    def sum(self, i: int) -> int:
        # prefix sum [0..i]
        i += 1
        s = 0
        while i > 0:
            s += self.ft[i]
            i -= i & -i
        return s
    def range_sum(self, l: int, r: int) -> int:
        return self.sum(r) - (self.sum(l-1) if l > 0 else 0)

# Range add / range sum using two BITs:
class FenwickRange:
    def __init__(self, n: int):
        self.n = n
        self.B1 = Fenwick(n)
        self.B2 = Fenwick(n)
    def _add(self, ft: Fenwick, idx: int, delta: int):
        ft.add(idx, delta)
    def range_add(self, l: int, r: int, val: int):
        # add val to [l, r]
        self._add(self.B1, l, val)
        self._add(self.B1, r+1, -val)
        self._add(self.B2, l, val*(l-1))
        self._add(self.B2, r+1, -val*r)
    def _prefix_sum(self, x: int) -> int:
        return self.B1.sum(x)*x - self.B2.sum(x)
    def range_sum(self, l: int, r: int) -> int:
        return self._prefix_sum(r) - (self._prefix_sum(l-1) if l > 0 else 0)


# ------------------------------------------------------------
# 3) Persistent Segment Tree (point update, range sum)
#    Each update returns a new root (version).
#    Use when you need historical queries / k-th queries over versions.
# ------------------------------------------------------------
class PSTNode:
    __slots__ = ("left", "right", "val")
    def __init__(self, left: Optional['PSTNode']=None, right: Optional['PSTNode']=None, val: int=0):
        self.left = left
        self.right = right
        self.val = val
class PersistentSegTree:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        def build(l: int, r: int) -> PSTNode:
            if l == r:
                return PSTNode(val=arr[l])
            m = (l+r)//2
            left = build(l, m)
            right = build(m+1, r)
            return PSTNode(left, right, left.val + right.val)
        self.versions = [build(0, self.n-1)]  # version 0
    def _update(self, node: PSTNode, l: int, r: int, idx: int, delta: int) -> PSTNode:
        if l == r:
            return PSTNode(val=node.val + delta)
        m = (l+r)//2
        if idx <= m:
            new_left = self._update(node.left, l, m, idx, delta)
            return PSTNode(new_left, node.right, new_left.val + node.right.val)
        else:
            new_right = self._update(node.right, m+1, r, idx, delta)
            return PSTNode(node.left, new_right, node.left.val + new_right.val)
    def point_update_new_version(self, version_idx: int, pos: int, delta: int) -> int:
        root = self._update(self.versions[version_idx], 0, self.n-1, pos, delta)
        self.versions.append(root)
        return len(self.versions) - 1  # new version id
    def _query(self, node: PSTNode, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or r < ql: return 0
        if ql <= l and r <= qr: return node.val
        m = (l+r)//2
        return self._query(node.left, l, m, ql, qr) + self._query(node.right, m+1, r, ql, qr)
    def range_sum(self, version_idx: int, l: int, r: int) -> int:
        return self._query(self.versions[version_idx], 0, self.n-1, l, r)


# ------------------------------------------------------------
# 4) Treap (Randomized Balanced BST) with Order Statistics
#    Supports: insert(x), erase(x), count_less(x), kth(k: 0-indexed)
# ------------------------------------------------------------
class TreapNode:
    __slots__ = ("key", "prio", "left", "right", "sz")
    def __init__(self, key: int):
        self.key = key
        self.prio = random.randint(1, 1<<30)
        self.left = None
        self.right = None
        self.sz = 1

def _sz(t: Optional[TreapNode]) -> int:
    return t.sz if t else 0

def _pull(t: TreapNode):
    t.sz = 1 + _sz(t.left) + _sz(t.right)

def _split(t: Optional[TreapNode], key: int) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
    # split by key: left <= key-1, right >= key
    if not t: return None, None
    if t.key < key:
        a, b = _split(t.right, key)
        t.right = a
        _pull(t)
        return t, b
    else:
        a, b = _split(t.left, key)
        t.left = b
        _pull(t)
        return a, t
def _merge(a: Optional[TreapNode], b: Optional[TreapNode]) -> Optional[TreapNode]:
    if not a or not b: return a or b
    if a.prio > b.prio:
        a.right = _merge(a.right, b)
        _pull(a)
        return a
    else:
        b.left = _merge(a, b.left)
        _pull(b)
        return b
class Treap:
    def __init__(self):
        self.root: Optional[TreapNode] = None
    def insert(self, x: int):
        # Allow duplicates: split by key x, then split right by x+1 to isolate equals
        left, right = _split(self.root, x)
        mid, right = _split(right, x+1)
        new_node = TreapNode(x)
        mid = _merge(mid, new_node)
        self.root = _merge(_merge(left, mid), right)
    def erase(self, x: int):
        left, right = _split(self.root, x)
        mid, right = _split(right, x+1)  # mid holds all = x
        # remove one x
        # to remove all x's: set mid=None
        def _erase_one(t: Optional[TreapNode]) -> Optional[TreapNode]:
            if not t: return None
            # remove a node with key x from t (which all equal x)
            # just discard root by merging its children once
            return _merge(t.left, t.right)
        mid = _erase_one(mid)
        self.root = _merge(_merge(left, mid), right)
    def count_less(self, x: int) -> int:
        # number of keys < x
        left, right = _split(self.root, x)
        res = _sz(left)
        self.root = _merge(left, right)
        return res
    def kth(self, k: int) -> Optional[int]:
        # 0-indexed k-th smallest; return None if out of range
        t = self.root
        while t:
            lsz = _sz(t.left)
            if k < lsz:
                t = t.left
            elif k == lsz:
                return t.key
            else:
                k -= lsz + 1
                t = t.right
        return None


# ------------------------------------------------------------
# 5) Sparse Table (RMQ - Range Minimum Query), O(1) query
# ------------------------------------------------------------
class SparseTableMin:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.LOG = [0]*(self.n+1)
        for i in range(2, self.n+1):
            self.LOG[i] = self.LOG[i//2] + 1
        K = self.LOG[self.n] + 1
        self.st = [[0]*self.n for _ in range(K)]
        self.st[0] = arr[:]
        j = 1
        while (1 << j) <= self.n:
            step = 1 << j
            half = step >> 1
            row = self.st[j]
            prev = self.st[j-1]
            for i in range(self.n - step + 1):
                row[i] = min(prev[i], prev[i + half])
            j += 1
    def range_min(self, l: int, r: int) -> int:
        # inclusive l..r
        k = self.LOG[r - l + 1]
        return min(self.st[k][l], self.st[k][r - (1 << k) + 1])


# ------------------------------------------------------------
# 6) Union-Find with Rollback (DSU Rollback)
#    - No path compression; union by size/rank; supports rollback()
# ------------------------------------------------------------
class DSURollback:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.sz  = [1]*n
        self.ops = []  # stack of (changed, a, b) to rollback
        self.cc  = n   # number of components
    def find(self, a: int) -> int:
        while a != self.par[a]:
            a = self.par[a]
        return a
    def union(self, a: int, b: int) -> bool:
        a = self.find(a); b = self.find(b)
        if a == b:
            self.ops.append((0, -1, -1))  # no-op marker
            return False
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        # attach b under a
        self.par[b] = a
        self.sz[a] += self.sz[b]
        self.ops.append((1, a, b))
        self.cc -= 1
        return True
    def snapshot(self) -> int:
        return len(self.ops)
    def rollback(self, snap: Optional[int]=None):
        # if snap is None: rollback one step; else rollback to snapshot
        if snap is None:
            snaps = len(self.ops) - 1
            if snaps < 0: return
            snap = snaps
        while len(self.ops) > snap:
            flag, a, b = self.ops.pop()
            if flag == 1:
                # revert union
                self.sz[a] -= self.sz[b]
                self.par[b] = b
                self.cc += 1
            # if flag == 0: was a no-op, nothing to undo
