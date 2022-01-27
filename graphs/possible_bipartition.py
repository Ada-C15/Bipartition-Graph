# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n+e)
        Space Complexity: O(n)
    """
    if len(dislikes) < 2:
        return True

    queue = deque([1])

    groups = {}
    groups[1] = 'X'
    seen = set([1])

    while len(queue) > 0:
        current = queue.popleft()
        group = groups[current]

        for dislike in dislikes[current]:
            if dislike in groups:
                if groups[dislike] == group:
                    return False
            else:
                groups[dislike] = 'X' if group == 'O' else 'O'

            if dislike not in seen:
                queue.append(dislike)
                seen.add(dislike)

    return True