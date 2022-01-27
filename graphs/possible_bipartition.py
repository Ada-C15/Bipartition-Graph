# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E)
        Space Complexity: O(N)
    """
    if not dislikes:
        return True

    frontier = [0]
    visited = {}
    group1 = set()
    group2 = set()

    while frontier:
        current = frontier.pop(0)

        if not dislikes[current]:
            if (current+1) not in visited:
                visited[current+1] = True
                frontier.append(current+1)

        for neigbor in dislikes[current]:
            if neigbor not in visited:
                visited[neigbor] = True
                frontier.append(neigbor)

            if current not in group1:
                if neigbor in group2:
                    return False
                group1.add(neigbor)
            else:
                if neigbor in group1:
                    return False
                group2.add(neigbor)

    return True