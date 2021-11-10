# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """

    if not dislikes:
        return True

    visited = [False] * len(dislikes)
    group_a = set()
    group_b = set()

    q = deque()
    q.append(0)

    while q:
        current = q.popleft()
        visited[current] = True        
        if not dislikes[current]:
            q.append(current+1)

        for dog in dislikes[current]:
            if not visited[dog]:              
                q.append(dog)

            if current not in group_a:
                if dog in group_b:
                    return False
                group_a.add(dog)    
            else:
                if dog in group_a:
                    return False
                group_b.add(dog)    
    
    return True

