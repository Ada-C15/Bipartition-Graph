# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n log n)
        Space Complexity: O(n)
    """
    n = len(dislikes)
    if n < 3:
        return True

    # creates an array of length n, will keep track of nodes visited
    visited = [False] * (n)

    # initializes a queue and two sets to hold two groups of puppies
    q = deque()
    q.append(1)
    visited[0] = True
    red = set()
    blue = set()
    red.add(1)
    
    #creates a dictionary to hold puppies and their enemies 
    dislike_dict = {}
    for i in range(0, n):
        dislike_dict[i] = dislikes[i]

    # loops through queue of nodes. 
    while len(q) > 0:
        pointerKey = q.popleft()
        # appends node to queue if it has not been visited. 
        # returns False if node is in other set already.
        for node in dislike_dict[pointerKey]:
            if visited[pointerKey] == False:
                q.append(node)
                if pointerKey not in red:
                    red.add(node)
                    if node in blue:
                        return False
                else:
                    blue.add(node)
                    if node in red:
                        return False
        visited[pointerKey] = True
    return True