# Can be used for BFS
from collections import deque
import collections
from email.policy import default 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(V+E)
        Space Complexity: O(N)
    """
    # input = [ [], [2, 3], [1, 4], [1], [2]]
    # output =  True 

    #  input1 =  [ [],[2, 3],[1, 3],[1, 2]]
    # output = False 

    ### Note ###
    # I had a hard time to come with a solution on my own
    # After looking up online resources/videos, this solution made sense to me

    start_node = 0
    visited = [False] * len(dislikes)
    q = deque()
    q.append(start_node)

    # initialize two groups for neighboring nodes 
    group_a = set()
    group_b = set()

    # edge cases when dislikes is empty or the len is 1
    if not dislikes or len(dislikes) == 1:
        return True 

    while q:
        current = q.popleft() #start_node is 0, 
        visited[current] = True

        if not dislikes[current]:
            q.append(current + 1)

        # iterate through the nodes in dislikes 
        for neighbor in dislikes[current]:
            if not visited[neighbor]: # not visited is append to q 
                q.append(neighbor)

            if current not in group_a:
                if neighbor in group_b:
                    return False
                group_a.add(neighbor)
            else:
                if neighbor in group_a:
                    return False
                group_b.add(neighbor)

    return True
