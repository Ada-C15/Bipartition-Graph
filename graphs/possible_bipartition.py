# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Frogges > puppies
        Time Complexity: O(N*E)
        Space Complexity: O(n)
    """
    if not dislikes:
        return True

    the_queue = deque()
    the_queue.append(0)

    tracked = len(dislikes) * [False]
    frogges_one = set()
    frogges_two = set()

    while the_queue:
        curr = the_queue.popleft()
        tracked[curr] = True
        if not dislikes[curr]:
            the_queue.append(curr + 1)

        for frogge in dislikes[curr]:
            if not tracked[frogge]:
                the_queue.append(frogge)

            if curr not in frogges_one:
                if frogge in frogges_two:
                    return False
                frogges_one.add(frogge)
            else:
                if frogge in frogges_one:
                    return False
                frogges_two.add(frogge)

    return True

