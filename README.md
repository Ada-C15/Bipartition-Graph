# Partitioning a Graph

In this exercise you will take in an adjacency list and determine if you can divide dogs into two groups where no two dogs that are known for fighting each other are in the same group.  This is a variation on the [graph coloring](https://en.wikipedia.org/wiki/Graph_coloring) problem as it can be extended to breaking the graph into `k` groups, each labeled with a color.

## Learning Goals

In this exercise you should be able to:

- Work with an adjacency list to process a graph.
- Navigate a graph through a traversal

## Description

Given a set of N puppies (numbered 0, 1, 2, ..., N - 1), we would like to split them into two groups of any size to use two play areas.

Some dogs have a history of fighting with specific other dogs and shouldn't be put into the same play area.

Formally, if dislikes[i] = [a, b], it means dog i is not allowed to put in the same group as dog a or dog b.

Return true if and only if it is possible to split the dogs into two groups where no fighting will occur.

### Example 1

```
Input: dislikes = [ [],
                    [2, 3],
                    [1, 4],
                    [1],
                    [2]
                  ]
Output: true
```

Explanation: group1 [0, 1, 4], group2 [2, 3]

### Example 2

```
Input: dislikes = [ [],
                    [2, 3],
                    [1, 3],
                    [1, 2]
                  ]
Output: false
```

Explanation: All the nodes 1-3 are interconnected and so there is no way to split them up.

### Example 3

```
Input: dislikes = [ [],
                    [2, 5],
                    [1, 3],
                    [2, 4],
                    [3, 5],
                    [1, 4]
                  ]
Output: false
```

### Note

The graph is undirected, so if dog 1 dislikes dog 2, then dog 2 also dislikes dog 1.

## Source

- [Leetocde 886. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)
