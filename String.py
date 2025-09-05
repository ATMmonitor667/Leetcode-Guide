from typing import List, Tuple, Dict
from collections import deque, defaultdict
import random

# ============================================================
# 1) KMP (prefix-function) & search
# ============================================================
def kmp_prefix(p: str) -> List[int]:
    pi = [0]*len(p)
    j = 0
    for i in range(1, len(p)):
        while j and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
        pi[i] = j
    return pi

def kmp_search(s: str, p: str) -> List[int]:
    """Return all start indices where pattern p occurs in s."""
    if not p:
        return list(range(len(s)+1))
    pi = kmp_prefix(p)
    res, j = [], 0
    for i, ch in enumerate(s):
        while j and ch != p[j]:
            j = pi[j-1]
        if ch == p[j]:
            j += 1
        if j == len(p):
            res.append(i - j + 1)
            j = pi[j-1]
    return res

# ============================================================
# 2) Z-Algorithm (pattern matching or string analysis)
# Z[i] = LCP(s, s[i:])
# ============================================================
def z_function(s: str) -> List[int]:
    n = len(s)
    Z = [0]*n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    Z[0] = n
    return Z

# ============================================================
# 3) Rabin–Karp / Rolling Hash (double mod, optional)
# Provide prefix hashes & O(1) substring hash; search occurrences
# ============================================================
class RollingHash:
    def __init__(self, s: str, base: int = 911382323, mod: int = 10**9+7):
        self.mod = mod
        self.base = base
        n = len(s)
        self.pw = [1]*(n+1)
        self.h  = [0]*(n+1)
        for i, ch in enumerate(s, 1):
            self.pw[i] = (self.pw[i-1]*base) % mod
            self.h[i]  = (self.h[i-1]*base + ord(ch)) % mod

    def hash(self, l: int, r: int) -> int:
        """hash of s[l:r] (0-indexed, r exclusive)"""
        return (self.h[r] - self.h[l]*self.pw[r-l]) % self.mod

def rabin_karp_search(s: str, p: str) -> List[int]:
    if not p:
        return list(range(len(s)+1))
    rh_s = RollingHash(s)
    rh_p = RollingHash(p)
    target = rh_p.hash(0, len(p))
    res = []
    for i in range(0, len(s) - len(p) + 1):
        if rh_s.hash(i, i+len(p)) == target:
            # optional: verify to avoid collisions
            if s[i:i+len(p)] == p:
                res.append(i)
    return res

# ============================================================
# 4) Suffix Array + LCP (Kasai)
# SA via O(n log n) doubling; LCP via Kasai in O(n)
# ============================================================
def suffix_array(s: str) -> List[int]:
    n = len(s)
    k = 1
    sa = list(range(n))
    rnk = [ord(c) for c in s]
    tmp = [0]*n
    while True:
        sa.sort(key=lambda i: (rnk[i], rnk[i+k] if i+k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            a, b = sa[i-1], sa[i]
            tmp[b] = tmp[a] + ( (rnk[a], rnk[a+k] if a+k<n else -1)
                               < (rnk[b], rnk[b+k] if b+k<n else -1) )
        rnk = tmp[:]
        if rnk[sa[-1]] == n-1:
            break
        k <<= 1
    return sa

def kasai_lcp(s: str, sa: List[int]) -> List[int]:
    n = len(s)
    rank = [0]*n
    for i, pos in enumerate(sa):
        rank[pos] = i
    lcp = [0]*n
    k = 0
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = sa[rank[i]+1]
        while i+k < n and j+k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k: k -= 1
    return lcp[:-1]  # length n-1 (between neighboring suffixes)

# ============================================================
# 5) Suffix Automaton (SAM)
# - Build in O(n)
# - Count distinct substrings: sum(len[v]-len[link[v]])
# - Occurrences: need endpos counts propagated by length order
# ============================================================
class SuffixAutomaton:
    def __init__(self):
        self.next = []   # list of dict transitions
        self.link = []   # suffix link
        self.len  = []   # max length of state
        self.occur = []  # endpos count for occurrences
        self.last = 0
        self._new_state(0)  # root

    def _new_state(self, length: int):
        self.next.append({})
        self.link.append(-1)
        self.len.append(length)
        self.occur.append(0)
        return len(self.next)-1

    def extend(self, c: str):
        cur = self._new_state(self.len[self.last] + 1)
        self.occur[cur] = 1
        p = self.last
        while p != -1 and c not in self.next[p]:
            self.next[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][c]
            if self.len[p] + 1 == self.len[q]:
                self.link[cur] = q
            else:
                clone = self._new_state(self.len[p] + 1)
                self.next[clone] = self.next[q].copy()
                self.link[clone] = self.link[q]
                self.occur[clone] = 0
                while p != -1 and self.next[p].get(c, -1) == q:
                    self.next[p][c] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur

    def build(self, s: str):
        for ch in s:
            self.extend(ch)

    def distinct_substrings(self) -> int:
        # sum over states of (len[v] - len[link[v]])
        return sum(self.len[v] - (self.len[self.link[v]] if self.link[v] != -1 else 0)
                   for v in range(1, len(self.next)))  # skip root (v=0)

    def propagate_occurrences(self):
        # after build, call this to compute endpos counts per state
        order = sorted(range(len(self.len)), key=lambda v: self.len[v], reverse=True)
        for v in order:
            if self.link[v] != -1:
                self.occur[self.link[v]] += self.occur[v]

    def count_occurrence(self, pattern: str) -> int:
        v = 0
        for ch in pattern:
            if ch not in self.next[v]:
                return 0
            v = self.next[v][ch]
        return self.occur[v]  # only valid after propagate_occurrences()

# ============================================================
# 6) Aho–Corasick (multi-pattern matching)
# - Insert patterns -> build fail links -> search in text
# returns counts per pattern index
# ============================================================
class AhoCorasick:
    def __init__(self):
        self.goto = [defaultdict(int)]  # transitions by char -> node
        self.fail = [0]
        self.out  = [list()]           # list of pattern indices ending here

    def add(self, pat: str, idx: int):
        s = 0
        for ch in pat:
            if ch not in self.goto[s]:
                self.goto[s][ch] = len(self.goto)
                self.goto.append(defaultdict(int))
                self.fail.append(0)
                self.out.append([])
            s = self.goto[s][ch]
        self.out[s].append(idx)

    def build(self):
        q = deque()
        # depth 1
        for ch, nxt in self.goto[0].items():
            self.fail[nxt] = 0
            q.append(nxt)
        # BFS
        while q:
            v = q.popleft()
            for ch, u in self.goto[v].items():
                q.append(u)
                f = self.fail[v]
                while f and ch not in self.goto[f]:
                    f = self.fail[f]
                self.fail[u] = self.goto[f][ch] if ch in self.goto[f] else 0
                self.out[u].extend(self.out[self.fail[u]])

    def search(self, text: str, m: int) -> List[int]:
        """Return occurrences count per pattern index [0..m-1]."""
        res = [0]*m
        s = 0
        for ch in text:
            while s and ch not in self.goto[s]:
                s = self.fail[s]
            if ch in self.goto[s]:
                s = self.goto[s][ch]
            else:
                s = 0
            for idx in self.out[s]:
                res[idx] += 1
        return res

# ============================================================
# 7) Manacher’s Algorithm (longest palindromic substring in O(n))
# Returns (start, length) of LPS; also returns the substring if needed
# ============================================================
def manacher_longest_palindrome(s: str) -> Tuple[int, int]:
    # Transform: "^#a#b#...#z#$" to unify odd/even
    if not s:
        return (0, 0)
    t = "^#" + "#".join(s) + "#$"
    n = len(t)
    p = [0]*n
    center = right = 0
    for i in range(1, n-1):
        mirror = 2*center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
    # Find max
    max_len, center_idx = max((p[i], i) for i in range(1, n-1))
    start = (center_idx - max_len)//2  # map back to original string
    return (start, max_len)

def longest_palindromic_substring(s: str) -> str:
    i, L = manacher_longest_palindrome(s)
    return s[i:i+L]
# ============================================================