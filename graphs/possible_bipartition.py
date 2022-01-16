# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
        Space Complexity: O(n)
    """
    N = len(dislikes)
    dogs = [None] * N
    queued = deque()

    for i in range(N):
        if dogs[i] != None:
            continue
        queued.append((i, "Baker"))
        while queued:
            node, dog = queued.popleft()
            puppy = "Baker"
            if not dogs[node]:
                dogs[node] = dog
            for next in dislikes[node]:
                if dogs[next] == dogs[node]:
                    return False
                elif dogs[next] and dogs[next] != dogs[node]:
                    continue
                elif not dogs[next] and dogs[node] == "Baker":
                    puppy = "Jpug"
                queued.append((next, puppy))
    return True