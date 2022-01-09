# Can be used for BFS
from collections import deque
import collections 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N+E)
        Space Complexity: O(N)
        where N - number of vertices/nodes, E - number of edges
    """
    if len(dislikes) == 0:
        return True

    belongs_to_group = [False for i in range(len(dislikes))]
    queue = collections.deque()

    queue.append(1)
    belongs_to_group[1] = "group_a"

    while len(queue) > 0:
        current_dog = queue.popleft()
        for unwanted_dog in dislikes[current_dog]:
            if belongs_to_group[unwanted_dog] == belongs_to_group[current_dog]:
                return False
            elif belongs_to_group[unwanted_dog] == False:
                belongs_to_group[unwanted_dog] = "group_b" if belongs_to_group[current_dog] == "group_a" else "group_a"
                queue.append(unwanted_dog)
    
    return True


