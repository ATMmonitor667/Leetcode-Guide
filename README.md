
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
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/0001-two-sum) |
## Greedy
|  |
| ------- |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Sorting
|  |
| ------- |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Heap (Priority Queue)
|  |
| ------- |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
## Matrix
|  |
| ------- |
| [3764-maximum-sum-with-at-most-k-elements](https://github.com/ATMmonitor667/Leetcode-Guide/tree/master/3764-maximum-sum-with-at-most-k-elements) |
<!---LeetCode Topics End-->