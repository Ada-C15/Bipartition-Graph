from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(NE)
        Space Complexity: O(N)
    """
    # BFS solution
    N = len(dislikes)
    colors = [None] * N
    q = deque()
    for i in range(N):
        if colors[i] != None:
            continue
        q.append((i, "red"))
        while q:
            node, color = q.popleft()
            temp = "red"
            if not colors[node]:
                colors[node] = color
            for next in dislikes[node]:
                if colors[next] == colors[node]:
                    return False
                elif colors[next] and colors[next] != colors[node]:
                    continue
                elif not colors[next] and colors[node] == "red":
                    temp = "green"
                q.append((next, temp))
    return True

