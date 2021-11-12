# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    visited = [False] * len(dislikes)
    color = [-1] * len(dislikes)

    def dfs(v, c):
        visited[v] = True
        color[v] = c
        for u in dislikes[v]:
            if not visited[u]:
                dfs(u, 1 - c)

    for i in range(len(dislikes)):
        if not visited[i]:
            dfs(i, 0)

    for i in range(len(dislikes)):
        for j in dislikes[i]:
            if color[i] == color[j]:
                return False

    return True

