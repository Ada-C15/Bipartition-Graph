from ast import And
from collections import deque
from concurrent.futures.process import BrokenProcessPool 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O("dogs"+:"dog relationships")
        Space Complexity: O("dogs")
        BFS?
    """
    if not dislikes:
        return True
    
    bork = len(dislikes)
    wolf_pack = [None] * bork
    good_bois = set()

    enqueue = deque()
    enqueue.append(0)

    while enqueue:
        pupper = enqueue.popleft()
        wolf_pack[pupper] = True

        if not dislikes[pupper]:
            enqueue.append(pupper+1)

        for borker in dislikes[pupper]:

            if not wolf_pack[borker]:
                enqueue.append(borker)
            
            if pupper not in good_bois:
                good_bois.add(borker)

            elif pupper not in good_bois and borker == "bad dog" or borker in good_bois:
                    return False

            else:
                borker = "bad dog"
            
    return True

