# DSA Codex

## TOC

- [DSA Codex](#dsa-codex)
  - [TOC](#toc)
  - [About the Project](#about-the-project)
    - [Built With](#built-with)
  - [Algorithms](#algorithms)
    - [Sorting Algorithms](#sorting-algorithms)
    - [Search Algorithms](#search-algorithms)
  - [Data Structures](#data-structures)
    - [Graphs](#graphs)
  - [Getting Started](#getting-started)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## About the Project

This is a Python project that focuses on implementing and testing various data structures and algorithms. The project
currently includes implementations for sorting and search algorithms.

## [Algorithms](./algorithms)

This directory contains implementations for various algorithms. The algorithms are organized into subdirectories based
on their type (e.g. sorting, search, etc.). Each algorithm is implemented as a function that takes in an array of
numbers and performs the algorithm on the array. The functions return the sorted array or the index of the searched
item.

### [Sorting Algorithms](./algorithms/sort)

The project includes the following sorting algorithms:

- [Mergesort](./algorithms/sort/mergesort.py): This algorithm follows the divide and conquer paradigm. It divides the
  input array into two halves, sorts
  them separately and then merges them. The sorting is done by recursively dividing the array until we have single
  element arrays, and then merging these arrays in a sorted manner.

- [Quicksort](./algorithms/sort/quicksort.py): This is another divide and conquer algorithm. It works by selecting a '
  pivot' element from the array and
  partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the
  pivot. The sub-arrays are then recursively sorted.

### Search Algorithms

The project includes the following search algorithm:

- [Binary Search](./algorithms/search/binary.py): This search algorithm works on the principle of divide and conquer.
  For this algorithm to work
  properly, the data collection should be in the sorted form. Binary search looks for a particular item by comparing the
  middle most item of the collection. If a match occurs, then the index of the item is returned. If the middle item is
  greater than the item, then the item is searched in the sub-array to the left of the middle item. Otherwise, the item
  is searched for in the sub-array to the right of the middle item. This process continues on the sub-array as well
  until the size of the subarray reduces to zero.

## [Data Structures](./data_structures)

This directory contains implementations for various data structures. The data structures are organized into
subdirectories based on their type (e.g. linked list, tree, etc.). Each data structure is implemented as a class that
contains the necessary methods.

- [Linked List](./data_structures/linked_list.py)
- [Binary Search Tree](./data_structures/binary_search_tree.py)
- [Queue](./data_structures/queue.py)
- [Stack](./data_structures/stack.py)
- [Min Heap](./data_structures/minheap.py)
- [Trie](./data_structures/trie.py)

### [Graphs](./data_structures/graphs)

- [Adjacency List](./data_structures/graphs/graph_adjacency_list.py): This is a graph data structure that uses a list of
  lists to represent the edges in the graph. Each vertex in the graph is represented by an index in the list. The
  elements in the list at that index are the vertices that are connected to the vertex at that index.
- [Adjacency Matrix](./data_structures/graphs/graph_adjacency_matrix.py): This is a graph data structure that uses a matrix
  to represent the edges in the graph. Each vertex in the graph is represented by an index in the matrix. The elements
  in the matrix at that index are the vertices that are connected to the vertex at that index.



## Getting Started

To get a local copy up and running, follow these steps:

1. Clone the repo

```bash
git clone https://github.com/graffhyrum/dsa_codex.git
```

2. Navigate to the project directory

```bash
cd dsa_codex
```

3. Run the tests

```bash
python -m unittest discover
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
