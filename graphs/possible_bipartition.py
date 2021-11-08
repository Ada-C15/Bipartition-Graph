# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    n = len(dislikes)
    if n < 3:
        return True

    visited = [False] * (n)

    print(visited)
    q = deque()
    q.append(1)
    visited[0] = True
    red = set()
    red.add(1)
    blue = set()

    dislike_dict = {}

    for i in range(0, n):
        dislike_dict[i] = dislikes[i]

    # for i in range(1, n-1):

    while len(q) > 0:
        print(q)
        pointerKey = q.popleft()
        print(pointerKey)

        print(visited)
        print(q)
        for node in dislike_dict[pointerKey]:
            if visited[pointerKey] == False:
                q.append(node)
                if pointerKey not in red:
                    red.add(node)
                    print(red, blue)
                    if node in blue:
                        print(False)
                        return False
                else:
                    blue.add(node)
                    print(red, blue)
                    if node in red:
                        print(False)
                        return False
        visited[pointerKey] = True
    print(visited)
    print(True)
    return True


# dislikes = [[], [2, 3], [1, 4], [1], [2]]
# possibleBipartition(dislikes)
