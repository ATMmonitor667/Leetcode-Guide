
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
| [0039-combination-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0039-combination-sum) |
| [0041-first-missing-positive](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0041-first-missing-positive) |
| [0054-spiral-matrix](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0054-spiral-matrix) |
| [0066-plus-one](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0066-plus-one) |
| [0073-set-matrix-zeroes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0073-set-matrix-zeroes) |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0217-contains-duplicate) |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [0419-battleships-in-a-board](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0419-battleships-in-a-board) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [0940-fruit-into-baskets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0940-fruit-into-baskets) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [1833-find-the-highest-altitude](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1833-find-the-highest-altitude) |
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
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0217-contains-duplicate) |
| [0940-fruit-into-baskets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0940-fruit-into-baskets) |
| [3928-split-and-merge-array-transformation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3928-split-and-merge-array-transformation) |
## Greedy
|  |
| ------- |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
| [4005-maximum-total-subarray-value-i](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/4005-maximum-total-subarray-value-i) |
## Sorting
|  |
| ------- |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0217-contains-duplicate](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0217-contains-duplicate) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Heap (Priority Queue)
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Matrix
|  |
| ------- |
| [0054-spiral-matrix](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0054-spiral-matrix) |
| [0073-set-matrix-zeroes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0073-set-matrix-zeroes) |
| [0419-battleships-in-a-board](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0419-battleships-in-a-board) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Divide and Conquer
|  |
| ------- |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
| [0190-reverse-bits](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0190-reverse-bits) |
## Counting
|  |
| ------- |
| [0169-majority-element](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0169-majority-element) |
## Simulation
|  |
| ------- |
| [0054-spiral-matrix](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0054-spiral-matrix) |
## Binary Search
|  |
| ------- |
| [0069-sqrtx](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0069-sqrtx) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
## Sliding Window
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [0940-fruit-into-baskets](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0940-fruit-into-baskets) |
## Prefix Sum
|  |
| ------- |
| [0713-subarray-product-less-than-k](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0713-subarray-product-less-than-k) |
| [1833-find-the-highest-altitude](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1833-find-the-highest-altitude) |
## Backtracking
|  |
| ------- |
| [0039-combination-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0039-combination-sum) |
## Breadth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0103-binary-tree-zigzag-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0103-binary-tree-zigzag-level-order-traversal) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
| [3928-split-and-merge-array-transformation](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3928-split-and-merge-array-transformation) |
## Math
|  |
| ------- |
| [0066-plus-one](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0066-plus-one) |
| [0069-sqrtx](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0069-sqrtx) |
## Queue
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
## Monotonic Queue
|  |
| ------- |
| [0239-sliding-window-maximum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0239-sliding-window-maximum) |
## Bit Manipulation
|  |
| ------- |
| [0190-reverse-bits](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0190-reverse-bits) |
| [0895-shortest-path-to-get-all-keys](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0895-shortest-path-to-get-all-keys) |
## Depth-First Search
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0129-sum-root-to-leaf-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0129-sum-root-to-leaf-numbers) |
| [0419-battleships-in-a-board](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0419-battleships-in-a-board) |
| [0776-n-ary-tree-postorder-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0776-n-ary-tree-postorder-traversal) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0904-leaf-similar-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0904-leaf-similar-trees) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
## Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0103-binary-tree-zigzag-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0103-binary-tree-zigzag-level-order-traversal) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0129-sum-root-to-leaf-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0129-sum-root-to-leaf-numbers) |
| [0776-n-ary-tree-postorder-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0776-n-ary-tree-postorder-traversal) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0904-leaf-similar-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0904-leaf-similar-trees) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
## Binary Tree
|  |
| ------- |
| [0100-same-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0100-same-tree) |
| [0103-binary-tree-zigzag-level-order-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0103-binary-tree-zigzag-level-order-traversal) |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
| [0129-sum-root-to-leaf-numbers](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0129-sum-root-to-leaf-numbers) |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
| [0904-leaf-similar-trees](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0904-leaf-similar-trees) |
| [1254-deepest-leaves-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1254-deepest-leaves-sum) |
| [2646-kth-largest-sum-in-a-binary-tree](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/2646-kth-largest-sum-in-a-binary-tree) |
## Union Find
|  |
| ------- |
| [1753-path-with-minimum-effort](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/1753-path-with-minimum-effort) |
## Stack
|  |
| ------- |
| [0776-n-ary-tree-postorder-traversal](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0776-n-ary-tree-postorder-traversal) |
## Linked List
|  |
| ------- |
| [0116-populating-next-right-pointers-in-each-node](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0116-populating-next-right-pointers-in-each-node) |
## Binary Search Tree
|  |
| ------- |
| [0799-minimum-distance-between-bst-nodes](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0799-minimum-distance-between-bst-nodes) |
<!---LeetCode Topics End-->