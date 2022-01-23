# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n * m)
        Space Complexity: O(n) ??
    """
    
    if not dislikes:
        return True
    
    if len(dislikes[0]) > 0:
        upcoming = [0]
    else:
        upcoming = [1]    

    group_one = set()
    group_two = set()
    hold_visited = []

    while upcoming:
        current_node = upcoming.pop(0)
        hold_visited.append(current_node)  

        a = True
        b = True

        for elem in dislikes[current_node]:
            if elem in group_one:
                a = False # flag to false
            if elem in group_two :
                b = False
            if (elem not in hold_visited) and (elem not in upcoming):
                upcoming.append(elem)

        if a == True:
            group_one.add(current_node)
        elif b == True:
            group_two.add(current_node)
        else:
            return False
    return True