#from ast import And
#from collections import deque
#from concurrent.futures.process import BrokenProcessPool 

#look into using above libraries? 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O("dogs"+:"dog relationships(dogs-1?)")
        Space Complexity: O("dogs")
        BFS?
    """
    borkers = len(dislikes)
    seen = [False for _ in range(borkers + 1)]
    dfs = [1 for _ in range(borkers + 1)]

    def _helper(borker, pupper):
        seen[borker] = True
        dfs[borker] = pupper
        for color in dislikes[borker]:
                if seen[color]:
                    if (pupper - dfs[color] + 1) % 2 != 0:
                        return False
                elif not _helper(color, pupper + 1): 
                    return False
        return True

    for borker in range(1, borkers):
        if not seen[borker]:
            if not _helper(borker, 1): return False  
    return True

    

