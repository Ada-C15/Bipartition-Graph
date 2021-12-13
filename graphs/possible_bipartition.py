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

    if len(dislikes[0]) > 0:
        to_visit = [0]
    else:
        to_visit = [1]    

    group_a = set()
    group_b = set()
    visited = []
    while to_visit:
        current = to_visit.pop(0)
        visited.append(current)  
        a = True
        b = True
        for dislike in dislikes[current]:
            if dislike in group_a:
                a = False
            if dislike in group_b :
                b = False
            if dislike not in visited and dislike not in to_visit:
                to_visit.append(dislike)
        if a == True:
            group_a.add(current)
        elif b == True:
            group_b.add(current)
        else:
            return False

    return True

