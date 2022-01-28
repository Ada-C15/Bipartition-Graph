# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n2)
        Space Complexity: O(n)
    """
    if not dislikes:
        return True

    queue = deque()
    queue.append(0)

    check = len(dislikes) * [False]
    whites = set()
    blacks = set()

    while queue:
        x = queue.popleft()
        for i in dislikes[x]:
            if not check[i]:
                queue.append(i)

            if x not in whites:
                if i in blacks:
                    return False
                whites.add(i)
            else:
                if i in whites:
                    return False
                blacks.add(i)
                
        check[x] = True
        if not dislikes[x]:
            queue.append(x + 1)

    return True

