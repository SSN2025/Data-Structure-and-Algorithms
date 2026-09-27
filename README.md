# Data Structures and Algorithms

A collection of implementations, notes, and practice programs covering fundamental **Data Structures and Algorithms (DSA)** concepts.

This repository is primarily used for learning, implementing, and experimenting with algorithms in Python.

## Topics Covered

### Divide and Conquer

Implementations and experiments related to algorithms that solve problems by dividing them into smaller subproblems.

* Merge Sort
* Fast Fourier Transform (FFT)
* Polynomial multiplication
* Other divide-and-conquer techniques

### Graph Algorithms

Implementations of fundamental graph algorithms and graph traversal techniques.

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Dijkstra's Algorithm
* Bellman-Ford Algorithm
* Kruskal's Algorithm
* Prim's Algorithm
* Topological Sort / Kahn's Algorithm
* Strongly Connected Components
* Minimum Spanning Trees
* Shortest Path Algorithms

### Greedy Algorithms

Algorithms based on making locally optimal choices with the goal of obtaining a globally optimal solution.

* Activity Selection
* Huffman Coding
* Minimum Spanning Tree algorithms
* Other greedy problem-solving techniques

### Huffman Coding

`HuffmanCoding.py` contains an implementation of **Huffman Coding**, a lossless data compression algorithm based on variable-length prefix codes.

The implementation demonstrates the use of:

* Binary trees
* Priority queues / min-heaps
* Greedy algorithms
* Prefix encoding

## Repository Structure

```text
Data-Structure-and-Algorithms/
│
├── Divide and conquer/
│   ├── ...
│   └── ...
│
├── Graphs/
│   ├── BFS
│   ├── DFS
│   ├── Dijkstra
│   ├── Bellman-Ford
│   ├── Kruskal
│   ├── Prim
│   └── ...
│
├── Greedy/
│   ├── Activity Selection
│   └── ...
│
├── HuffmanCoding.py
│
└── README.md
```

The exact contents of each directory may grow as more algorithms and implementations are added.

## Goals

The main goals of this repository are to:

* Understand the logic behind common algorithms.
* Implement algorithms from scratch rather than relying on built-in solutions.
* Analyze time and space complexity.
* Practice solving algorithmic problems.
* Experiment with different implementations and data structures.
* Maintain a reference for DSA coursework and future problem solving.

## Complexity Analysis

Where appropriate, implementations are accompanied by analysis of:

**Time Complexity**

`O(...)`, `Θ(...)`, and `Ω(...)`

**Space Complexity**

Including auxiliary space used by data structures, recursion, and temporary storage.

## Language

Most implementations in this repository are written in:

**Python**

Libraries such as NumPy may be used in some implementations for working with matrices and numerical data.

## Running the Code

Clone the repository:

```bash
git clone https://github.com/SSN2025/Data-Structure-and-Algorithms.git
cd Data-Structure-and-Algorithms
```

Individual Python programs can then be executed with:

```bash
python3 filename.py
```

For Jupyter notebooks:

```bash
jupyter notebook
```

## Learning Approach

The implementations in this repository focus on understanding the algorithm rather than treating the code as a black box.

For each algorithm, the general workflow is:

```text
Problem
   ↓
Understand the idea
   ↓
Design the algorithm
   ↓
Implement
   ↓
Test on examples
   ↓
Analyze complexity
   ↓
Optimize if necessary
```

## References

Some of the concepts and algorithms are based on standard Data Structures and Algorithms coursework and commonly used algorithm textbooks and references.

## Status

This is an ongoing learning repository. New algorithms, optimizations, explanations, and implementations will be added as the study of DSA progresses.
