# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if not dislikes:
        return True

    q = [0]
    visited = {}
    group1 = []
    group2 = []

    while q:
        current = q.pop(0)

        if not dislikes[current]:
            q.append(current+1)
        
        for neigbor in dislikes[current]:
            if neigbor not in visited:
                visited[neigbor] = True
                q.append(neigbor)

            if current not in group1:
                if neigbor in group2:
                    return False
                group1.append(neigbor)
            else:
                if neigbor in group1:
                    return False
                group2.append(neigbor)

    return True


