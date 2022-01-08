# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
    #     Time Complexity: O(nm)
    #     Space Complexity: O(n)
    # """
    
    if dislikes == []:
        return True

    visited_dogs = [False] * len(dislikes)
    group_one = set()
    group_two = set()
    dog_queue = deque()
    dog_queue.append(0)

    while dog_queue != deque([]):
        current_dog = dog_queue.popleft()
        visited_dogs[current_dog] = True        
        if not dislikes[current_dog]:
            dog_queue.append(current_dog + 1)

        for dog in dislikes[current_dog]:
            if visited_dogs[dog] == False:              
                dog_queue.append(dog)
            
            if current_dog not in group_one and dog in group_two:                
                return False
            elif current_dog not in group_one:
                group_one.add(dog)
            elif dog in group_one:
                return False
            else:
                group_two.add(dog)    
    return True

# print(possible_bipartition([ [],
#                     [2, 3],
#                     [1, 4],
#                     [1],
#                     [2]
#                 ]) == True)

# print(possible_bipartition([ [],
#                     [2, 3],
#                     [1, 3],
#                     [1, 2]
#                 ]) == False)

