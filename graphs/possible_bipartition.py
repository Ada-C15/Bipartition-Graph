# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    groups = [set(), set()]

    not_checked = {i for i in range(len(dislikes))}
    to_check = []

    while not_checked:
        if not to_check:
            dog = not_checked.pop()
            
        else:
            dog = to_check.pop()
            not_checked.remove(dog)

        dog_dislikes = set(dislikes[dog])
        for other_dog in dislikes[dog]:
            if other_dog in not_checked:
                to_check.append(other_dog)

        if not groups[0].intersection(dog_dislikes):
            groups[0].add(dog)
        elif  not groups[1].intersection(dog_dislikes):
            groups[1].add(dog)
        else:
            return False

    return True
        