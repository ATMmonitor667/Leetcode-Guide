
# 🚀 LeetCode Guide

A comprehensive collection of algorithmic templates, data structures, and problem solutions for competitive programming and technical interviews.

## 📁 Repository Structure

### Core Algorithm Templates
- **`AdvancedTechniques.py`** - Mo's Algorithm, advanced optimization techniques
- **`AdvancedDSA.py`** - Segment Trees with Lazy Propagation, advanced data structures
- **`Dp.py`** - Dynamic Programming patterns including TSP, Digit DP, and Bitmask DP
- **`Graph.py`** - Graph algorithms (Dijkstra, Floyd-Warshall, 0-1 BFS, etc.)
- **`String.py`** - String algorithms including KMP, pattern matching
- **`SlidingWindow.py`** - Sliding window techniques and patterns

### Problem Solutions
- **`mySolutions/`** - Directory containing solutions to specific LeetCode problems
  - Find Edges in Shortest Paths
  - Maximize Subarray Sum After Removing All Occurrences of One Element
  - Number of Distinct Roll Sequences
  - Paint House III
  - Swim in Rising Water

## 🛠️ Features

### Advanced Data Structures
- **Lazy Propagation Segment Tree** - Efficient range updates and queries
- **Mo's Algorithm** - Square root decomposition for offline queries
- **Graph Algorithms** - Complete implementation of shortest path algorithms

### Dynamic Programming Patterns
- **Bitmask DP** - Traveling Salesman Problem (TSP) variations
- **Digit DP** - Count numbers with specific properties
- **Set Cover Problems** - Minimum actions to cover all positions

### String Algorithms
- **KMP Algorithm** - Efficient pattern matching
- **Advanced String Processing** - Multiple string manipulation techniques

### Graph Theory
- **Dijkstra's Algorithm** - Single-source shortest path
- **Floyd-Warshall** - All-pairs shortest path
- **0-1 BFS** - Specialized BFS for binary weights

## 📝 Usage

Each Python file contains well-documented classes and functions that can be directly imported and used:

```python
from AdvancedDSA import LazySegTree
from Graph import Solution as GraphSolution
from Dp import Solution as DPSolution

# Example: Using Lazy Segment Tree
arr = [1, 2, 3, 4, 5]
seg_tree = LazySegTree(arr)
seg_tree.range_add(0, 2, 10)  # Add 10 to range [0, 2]
result = seg_tree.range_sum(1, 3)  # Query sum in range [1, 3]

# Example: Using Dijkstra's algorithm
graph_solver = GraphSolution()
edges = [(0, 1, 2), (1, 2, 3), (0, 2, 6)]
distances = graph_solver.dijkstra(3, edges, 0)
```

## 🎯 Target Audience

- **Competitive Programmers** preparing for contests like Codeforces, AtCoder
- **Software Engineers** preparing for technical interviews at FAANG companies
- **Students** learning advanced algorithms and data structures
- **Anyone** looking to improve their problem-solving skills

## 📚 Algorithm Categories

### Graph Algorithms
- Shortest Path Algorithms
- Graph Traversal Techniques
- Specialized BFS/DFS variants

### Dynamic Programming
- Classical DP patterns
- Optimization techniques
- State space reduction methods

=======
- travelling salesmen problem


### Advanced Data Structures
- Range Query Data Structures
- Efficient Update Mechanisms
- Square Root Decomposition

### String Processing
- Pattern Matching
- String Hashing
- Advanced String Algorithms

## 🔧 Prerequisites

- Python 3.7+
- Basic understanding of algorithms and data structures
- Familiarity with competitive programming concepts

## 🤝 Contributing

Feel free to contribute by:
1. Adding new algorithm templates
2. Optimizing existing implementations
3. Adding more problem solutions
4. Improving documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🌟 Acknowledgments

- LeetCode for providing an excellent platform for practicing algorithms
- The competitive programming community for sharing knowledge and techniques



<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0001-two-sum) |
| [0004-median-of-two-sorted-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0004-median-of-two-sorted-arrays) |
| [0015-3sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0015-3sum) |
| [0039-combination-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0040-combination-sum-ii) |
| [0041-first-missing-positive](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0041-first-missing-positive) |
| [0054-spiral-matrix](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0054-spiral-matrix) |
| [0056-merge-intervals](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0056-merge-intervals) |
| [0066-plus-one](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0066-plus-one) |
| [0073-set-matrix-zeroes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0073-set-matrix-zeroes) |
| [0078-subsets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0090-subsets-ii) |
| [0150-evaluate-reverse-polish-notation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0150-evaluate-reverse-polish-notation) |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0200-number-of-islands](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0200-number-of-islands) |
| [0216-combination-sum-iii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0216-combination-sum-iii) |
| [0217-contains-duplicate](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0217-contains-duplicate) |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [0303-range-sum-query-immutable](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0303-range-sum-query-immutable) |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0349-intersection-of-two-arrays) |
| [0380-insert-delete-getrandom-o1](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0380-insert-delete-getrandom-o1) |
| [0419-battleships-in-a-board](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0419-battleships-in-a-board) |
| [0475-heaters](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0475-heaters) |
| [0485-max-consecutive-ones](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0485-max-consecutive-ones) |
| [0523-continuous-subarray-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0523-continuous-subarray-sum) |
| [0525-contiguous-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0525-contiguous-array) |
| [0540-single-element-in-a-sorted-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0540-single-element-in-a-sorted-array) |
| [0560-subarray-sum-equals-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0560-subarray-sum-equals-k) |
| [0658-find-k-closest-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0658-find-k-closest-elements) |
| [0705-design-hashset](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0706-design-hashmap) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [0735-asteroid-collision](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0735-asteroid-collision) |
| [0747-largest-number-at-least-twice-of-others](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0747-largest-number-at-least-twice-of-others) |
| [0827-making-a-large-island](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0827-making-a-large-island) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [0922-sort-array-by-parity-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0922-sort-array-by-parity-ii) |
| [0940-fruit-into-baskets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0940-fruit-into-baskets) |
| [0974-subarray-sums-divisible-by-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0974-subarray-sums-divisible-by-k) |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
| [1018-binary-prefix-divisible-by-5](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1018-binary-prefix-divisible-by-5) |
| [1200-minimum-absolute-difference](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1200-minimum-absolute-difference) |
| [1352-product-of-the-last-k-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1352-product-of-the-last-k-numbers) |
| [1381-design-a-stack-with-increment-operation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1381-design-a-stack-with-increment-operation) |
| [1470-shuffle-the-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1470-shuffle-the-array) |
| [1476-subrectangle-queries](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1476-subrectangle-queries) |
| [1656-design-an-ordered-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1656-design-an-ordered-stream) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [1833-find-the-highest-altitude](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1833-find-the-highest-altitude) |
| [1861-rotating-the-box](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1861-rotating-the-box) |
| [1929-concatenation-of-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1929-concatenation-of-array) |
| [2099-find-subsequence-of-length-k-with-the-largest-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2099-find-subsequence-of-length-k-with-the-largest-sum) |
| [2154-keep-multiplying-found-values-by-two](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2154-keep-multiplying-found-values-by-two) |
| [2441-largest-positive-integer-that-exists-with-its-negative](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2441-largest-positive-integer-that-exists-with-its-negative) |
| [2442-count-number-of-distinct-integers-after-reverse-operations](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2442-count-number-of-distinct-integers-after-reverse-operations) |
| [3747-maximum-difference-between-adjacent-elements-in-a-circular-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3747-maximum-difference-between-adjacent-elements-in-a-circular-array) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
| [3928-split-and-merge-array-transformation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3928-split-and-merge-array-transformation) |
| [4005-maximum-total-subarray-value-i](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/4005-maximum-total-subarray-value-i) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0001-two-sum) |
| [0041-first-missing-positive](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0041-first-missing-positive) |
| [0073-set-matrix-zeroes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0073-set-matrix-zeroes) |
| [0160-intersection-of-two-linked-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0160-intersection-of-two-linked-lists) |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0217-contains-duplicate) |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0349-intersection-of-two-arrays) |
| [0355-design-twitter](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0355-design-twitter) |
| [0380-insert-delete-getrandom-o1](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0380-insert-delete-getrandom-o1) |
| [0523-continuous-subarray-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0523-continuous-subarray-sum) |
| [0525-contiguous-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0525-contiguous-array) |
| [0560-subarray-sum-equals-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0560-subarray-sum-equals-k) |
| [0705-design-hashset](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0706-design-hashmap) |
| [0940-fruit-into-baskets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0940-fruit-into-baskets) |
| [0974-subarray-sums-divisible-by-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0974-subarray-sums-divisible-by-k) |
| [0987-vertical-order-traversal-of-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0987-vertical-order-traversal-of-a-binary-tree) |
| [1656-design-an-ordered-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1656-design-an-ordered-stream) |
| [2099-find-subsequence-of-length-k-with-the-largest-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2099-find-subsequence-of-length-k-with-the-largest-sum) |
| [2154-keep-multiplying-found-values-by-two](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2154-keep-multiplying-found-values-by-two) |
| [2441-largest-positive-integer-that-exists-with-its-negative](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2441-largest-positive-integer-that-exists-with-its-negative) |
| [2442-count-number-of-distinct-integers-after-reverse-operations](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2442-count-number-of-distinct-integers-after-reverse-operations) |
| [3928-split-and-merge-array-transformation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3928-split-and-merge-array-transformation) |
## Greedy
|  |
| ------- |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
| [4005-maximum-total-subarray-value-i](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/4005-maximum-total-subarray-value-i) |
## Sorting
|  |
| ------- |
| [0015-3sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0015-3sum) |
| [0056-merge-intervals](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0056-merge-intervals) |
| [0148-sort-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0148-sort-list) |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0217-contains-duplicate) |
| [0295-find-median-from-data-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0295-find-median-from-data-stream) |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [0349-intersection-of-two-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0349-intersection-of-two-arrays) |
| [0475-heaters](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0475-heaters) |
| [0658-find-k-closest-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0658-find-k-closest-elements) |
| [0747-largest-number-at-least-twice-of-others](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0747-largest-number-at-least-twice-of-others) |
| [0922-sort-array-by-parity-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0922-sort-array-by-parity-ii) |
| [0987-vertical-order-traversal-of-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0987-vertical-order-traversal-of-a-binary-tree) |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
| [1200-minimum-absolute-difference](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1200-minimum-absolute-difference) |
| [2099-find-subsequence-of-length-k-with-the-largest-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2099-find-subsequence-of-length-k-with-the-largest-sum) |
| [2154-keep-multiplying-found-values-by-two](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2154-keep-multiplying-found-values-by-two) |
| [2441-largest-positive-integer-that-exists-with-its-negative](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2441-largest-positive-integer-that-exists-with-its-negative) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Heap (Priority Queue)
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0023-merge-k-sorted-lists) |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [0295-find-median-from-data-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0295-find-median-from-data-stream) |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [0355-design-twitter](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0355-design-twitter) |
| [0658-find-k-closest-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0658-find-k-closest-elements) |
| [0703-kth-largest-element-in-a-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0703-kth-largest-element-in-a-stream) |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [2099-find-subsequence-of-length-k-with-the-largest-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2099-find-subsequence-of-length-k-with-the-largest-sum) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Matrix
|  |
| ------- |
| [0054-spiral-matrix](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0054-spiral-matrix) |
| [0073-set-matrix-zeroes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0073-set-matrix-zeroes) |
| [0200-number-of-islands](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0200-number-of-islands) |
| [0419-battleships-in-a-board](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0419-battleships-in-a-board) |
| [0827-making-a-large-island](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0827-making-a-large-island) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [1476-subrectangle-queries](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1476-subrectangle-queries) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [1861-rotating-the-box](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1861-rotating-the-box) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Divide and Conquer
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0004-median-of-two-sorted-arrays) |
| [0023-merge-k-sorted-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0023-merge-k-sorted-lists) |
| [0148-sort-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0148-sort-list) |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0190-reverse-bits](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0190-reverse-bits) |
| [0191-number-of-1-bits](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0191-number-of-1-bits) |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
## Counting
|  |
| ------- |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [1603-design-parking-system](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1603-design-parking-system) |
| [2442-count-number-of-distinct-integers-after-reverse-operations](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2442-count-number-of-distinct-integers-after-reverse-operations) |
## Simulation
|  |
| ------- |
| [0054-spiral-matrix](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0054-spiral-matrix) |
| [0735-asteroid-collision](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0735-asteroid-collision) |
| [1603-design-parking-system](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1603-design-parking-system) |
| [1929-concatenation-of-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1929-concatenation-of-array) |
| [2154-keep-multiplying-found-values-by-two](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2154-keep-multiplying-found-values-by-two) |
## Binary Search
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0004-median-of-two-sorted-arrays) |
| [0069-sqrtx](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0069-sqrtx) |
| [0349-intersection-of-two-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0349-intersection-of-two-arrays) |
| [0475-heaters](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0475-heaters) |
| [0540-single-element-in-a-sorted-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0540-single-element-in-a-sorted-array) |
| [0658-find-k-closest-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0658-find-k-closest-elements) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
## Sliding Window
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [0658-find-k-closest-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0658-find-k-closest-elements) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [0940-fruit-into-baskets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0940-fruit-into-baskets) |
## Prefix Sum
|  |
| ------- |
| [0303-range-sum-query-immutable](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0303-range-sum-query-immutable) |
| [0523-continuous-subarray-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0523-continuous-subarray-sum) |
| [0525-contiguous-array](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0525-contiguous-array) |
| [0560-subarray-sum-equals-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0560-subarray-sum-equals-k) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [0974-subarray-sums-divisible-by-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0974-subarray-sums-divisible-by-k) |
| [1352-product-of-the-last-k-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1352-product-of-the-last-k-numbers) |
| [1833-find-the-highest-altitude](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1833-find-the-highest-altitude) |
## Backtracking
|  |
| ------- |
| [0039-combination-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0039-combination-sum) |
| [0040-combination-sum-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0040-combination-sum-ii) |
| [0078-subsets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0090-subsets-ii) |
| [0216-combination-sum-iii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0216-combination-sum-iii) |
## Breadth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0102-binary-tree-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0102-binary-tree-level-order-traversal) |
| [0103-binary-tree-zigzag-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0103-binary-tree-zigzag-level-order-traversal) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0200-number-of-islands](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0200-number-of-islands) |
| [0429-n-ary-tree-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0429-n-ary-tree-level-order-traversal) |
| [0515-find-largest-value-in-each-tree-row](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0515-find-largest-value-in-each-tree-row) |
| [0617-merge-two-binary-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0617-merge-two-binary-trees) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0827-making-a-large-island](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0827-making-a-large-island) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [0987-vertical-order-traversal-of-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0987-vertical-order-traversal-of-a-binary-tree) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
| [3928-split-and-merge-array-transformation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3928-split-and-merge-array-transformation) |
## Math
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0002-add-two-numbers) |
| [0007-reverse-integer](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0007-reverse-integer) |
| [0009-palindrome-number](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0009-palindrome-number) |
| [0050-powx-n](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0050-powx-n) |
| [0066-plus-one](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0066-plus-one) |
| [0069-sqrtx](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0069-sqrtx) |
| [0150-evaluate-reverse-polish-notation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0150-evaluate-reverse-polish-notation) |
| [0380-insert-delete-getrandom-o1](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0380-insert-delete-getrandom-o1) |
| [0445-add-two-numbers-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0445-add-two-numbers-ii) |
| [0523-continuous-subarray-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0523-continuous-subarray-sum) |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
| [1352-product-of-the-last-k-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1352-product-of-the-last-k-numbers) |
| [2442-count-number-of-distinct-integers-after-reverse-operations](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2442-count-number-of-distinct-integers-after-reverse-operations) |
| [2443-sum-of-number-and-its-reverse](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2443-sum-of-number-and-its-reverse) |
## Queue
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [0933-number-of-recent-calls](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0933-number-of-recent-calls) |
## Monotonic Queue
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
## Bit Manipulation
|  |
| ------- |
| [0078-subsets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0078-subsets) |
| [0090-subsets-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0090-subsets-ii) |
| [0190-reverse-bits](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0190-reverse-bits) |
| [0191-number-of-1-bits](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0191-number-of-1-bits) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [1018-binary-prefix-divisible-by-5](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1018-binary-prefix-divisible-by-5) |
## Depth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0129-sum-root-to-leaf-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0129-sum-root-to-leaf-numbers) |
| [0200-number-of-islands](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0200-number-of-islands) |
| [0230-kth-smallest-element-in-a-bst](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0230-kth-smallest-element-in-a-bst) |
| [0419-battleships-in-a-board](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0419-battleships-in-a-board) |
| [0430-flatten-a-multilevel-doubly-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0430-flatten-a-multilevel-doubly-linked-list) |
| [0515-find-largest-value-in-each-tree-row](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0515-find-largest-value-in-each-tree-row) |
| [0538-convert-bst-to-greater-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0538-convert-bst-to-greater-tree) |
| [0617-merge-two-binary-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0617-merge-two-binary-trees) |
| [0776-n-ary-tree-postorder-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0776-n-ary-tree-postorder-traversal) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0827-making-a-large-island](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0827-making-a-large-island) |
| [0904-leaf-similar-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0904-leaf-similar-trees) |
| [0987-vertical-order-traversal-of-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0987-vertical-order-traversal-of-a-binary-tree) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
## Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0102-binary-tree-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0102-binary-tree-level-order-traversal) |
| [0103-binary-tree-zigzag-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0103-binary-tree-zigzag-level-order-traversal) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0129-sum-root-to-leaf-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0129-sum-root-to-leaf-numbers) |
| [0230-kth-smallest-element-in-a-bst](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0230-kth-smallest-element-in-a-bst) |
| [0429-n-ary-tree-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0429-n-ary-tree-level-order-traversal) |
| [0515-find-largest-value-in-each-tree-row](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0515-find-largest-value-in-each-tree-row) |
| [0538-convert-bst-to-greater-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0538-convert-bst-to-greater-tree) |
| [0617-merge-two-binary-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0617-merge-two-binary-trees) |
| [0700-search-in-a-binary-search-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0700-search-in-a-binary-search-tree) |
| [0703-kth-largest-element-in-a-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0703-kth-largest-element-in-a-stream) |
| [0776-n-ary-tree-postorder-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0776-n-ary-tree-postorder-traversal) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0904-leaf-similar-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0904-leaf-similar-trees) |
| [0987-vertical-order-traversal-of-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0987-vertical-order-traversal-of-a-binary-tree) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
## Binary Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0102-binary-tree-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0102-binary-tree-level-order-traversal) |
| [0103-binary-tree-zigzag-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0103-binary-tree-zigzag-level-order-traversal) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0129-sum-root-to-leaf-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0129-sum-root-to-leaf-numbers) |
| [0230-kth-smallest-element-in-a-bst](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0230-kth-smallest-element-in-a-bst) |
| [0515-find-largest-value-in-each-tree-row](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0515-find-largest-value-in-each-tree-row) |
| [0538-convert-bst-to-greater-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0538-convert-bst-to-greater-tree) |
| [0617-merge-two-binary-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0617-merge-two-binary-trees) |
| [0700-search-in-a-binary-search-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0700-search-in-a-binary-search-tree) |
| [0703-kth-largest-element-in-a-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0703-kth-largest-element-in-a-stream) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0904-leaf-similar-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0904-leaf-similar-trees) |
| [0987-vertical-order-traversal-of-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0987-vertical-order-traversal-of-a-binary-tree) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
## Union Find
|  |
| ------- |
| [0200-number-of-islands](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0200-number-of-islands) |
| [0827-making-a-large-island](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0827-making-a-large-island) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
## Stack
|  |
| ------- |
| [0150-evaluate-reverse-polish-notation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0150-evaluate-reverse-polish-notation) |
| [0155-min-stack](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0155-min-stack) |
| [0234-palindrome-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0234-palindrome-linked-list) |
| [0445-add-two-numbers-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0445-add-two-numbers-ii) |
| [0735-asteroid-collision](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0735-asteroid-collision) |
| [0776-n-ary-tree-postorder-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0776-n-ary-tree-postorder-traversal) |
| [1381-design-a-stack-with-increment-operation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1381-design-a-stack-with-increment-operation) |
## Linked List
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0021-merge-two-sorted-lists) |
| [0023-merge-k-sorted-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0023-merge-k-sorted-lists) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0148-sort-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0148-sort-list) |
| [0160-intersection-of-two-linked-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0160-intersection-of-two-linked-lists) |
| [0206-reverse-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0206-reverse-linked-list) |
| [0234-palindrome-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0234-palindrome-linked-list) |
| [0355-design-twitter](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0355-design-twitter) |
| [0430-flatten-a-multilevel-doubly-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0430-flatten-a-multilevel-doubly-linked-list) |
| [0445-add-two-numbers-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0445-add-two-numbers-ii) |
| [0705-design-hashset](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0706-design-hashmap) |
## Binary Search Tree
|  |
| ------- |
| [0230-kth-smallest-element-in-a-bst](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0230-kth-smallest-element-in-a-bst) |
| [0538-convert-bst-to-greater-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0538-convert-bst-to-greater-tree) |
| [0700-search-in-a-binary-search-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0700-search-in-a-binary-search-tree) |
| [0703-kth-largest-element-in-a-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0703-kth-largest-element-in-a-stream) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
## Geometry
|  |
| ------- |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
| [1014-k-closest-points-to-origin](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1014-k-closest-points-to-origin) |
## Two Pointers
|  |
| ------- |
| [0015-3sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0015-3sum) |
| [0148-sort-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0148-sort-list) |
| [0160-intersection-of-two-linked-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0160-intersection-of-two-linked-lists) |
| [0234-palindrome-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0234-palindrome-linked-list) |
| [0295-find-median-from-data-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0295-find-median-from-data-stream) |
| [0349-intersection-of-two-arrays](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0349-intersection-of-two-arrays) |
| [0475-heaters](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0475-heaters) |
| [0658-find-k-closest-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0658-find-k-closest-elements) |
| [0922-sort-array-by-parity-ii](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0922-sort-array-by-parity-ii) |
| [1861-rotating-the-box](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1861-rotating-the-box) |
| [2441-largest-positive-integer-that-exists-with-its-negative](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2441-largest-positive-integer-that-exists-with-its-negative) |
## Enumeration
|  |
| ------- |
| [2443-sum-of-number-and-its-reverse](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2443-sum-of-number-and-its-reverse) |
## Design
|  |
| ------- |
| [0155-min-stack](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0155-min-stack) |
| [0295-find-median-from-data-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0295-find-median-from-data-stream) |
| [0303-range-sum-query-immutable](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0303-range-sum-query-immutable) |
| [0355-design-twitter](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0355-design-twitter) |
| [0380-insert-delete-getrandom-o1](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0380-insert-delete-getrandom-o1) |
| [0703-kth-largest-element-in-a-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0703-kth-largest-element-in-a-stream) |
| [0705-design-hashset](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0706-design-hashmap) |
| [0933-number-of-recent-calls](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0933-number-of-recent-calls) |
| [1352-product-of-the-last-k-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1352-product-of-the-last-k-numbers) |
| [1381-design-a-stack-with-increment-operation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1381-design-a-stack-with-increment-operation) |
| [1476-subrectangle-queries](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1476-subrectangle-queries) |
| [1603-design-parking-system](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1603-design-parking-system) |
| [1656-design-an-ordered-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1656-design-an-ordered-stream) |
## Data Stream
|  |
| ------- |
| [0295-find-median-from-data-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0295-find-median-from-data-stream) |
| [0703-kth-largest-element-in-a-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0703-kth-largest-element-in-a-stream) |
| [0933-number-of-recent-calls](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0933-number-of-recent-calls) |
| [1352-product-of-the-last-k-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1352-product-of-the-last-k-numbers) |
| [1656-design-an-ordered-stream](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1656-design-an-ordered-stream) |
## Hash Function
|  |
| ------- |
| [0705-design-hashset](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0705-design-hashset) |
| [0706-design-hashmap](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0706-design-hashmap) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0347-top-k-frequent-elements) |
## Randomized
|  |
| ------- |
| [0380-insert-delete-getrandom-o1](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0380-insert-delete-getrandom-o1) |
## Recursion
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0021-merge-two-sorted-lists) |
| [0050-powx-n](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0050-powx-n) |
| [0206-reverse-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0206-reverse-linked-list) |
| [0234-palindrome-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0234-palindrome-linked-list) |
## Merge Sort
|  |
| ------- |
| [0023-merge-k-sorted-lists](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0023-merge-k-sorted-lists) |
| [0148-sort-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0148-sort-list) |
## Doubly-Linked List
|  |
| ------- |
| [0430-flatten-a-multilevel-doubly-linked-list](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0430-flatten-a-multilevel-doubly-linked-list) |
<!---LeetCode Topics End-->