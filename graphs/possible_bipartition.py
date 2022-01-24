# Can be used for BFS
from collections import deque


def possible_bipartition(dislikes):
    if dislikes == []:
        return True

    start_node = 0
    visted = [False] * len(dislikes)
    q = deque()
    q.append(start_node)

    group_a = []
    group_b = []

    while q:
        current = q.popleft()
        visted[current] = True
        if not dislikes[current]:
            q.append(current + 1)

        for i in dislikes[current]:
            if visted[i] == False:
                q.append(i)

            if current not in group_a:
                if i in group_b:
                    return False
                group_a.append(i)
            else:
                if i in group_a:
                    return False
                group_b.append(i)

    return True

    pass
