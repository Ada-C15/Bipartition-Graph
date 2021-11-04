# Can be used for BFS
from collections import deque

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    # if an empty graph is passed in, return True
    if dislikes == []:
        return True

    # make a queue of dogs to check using deque
    dog_queue = deque()
    # puts the first dog in the queue to be searched
    dog_queue.append(0)
    # list of dogs already searched to account for duplicates/infinite loops in dog_queue
    searched = []

    # two groups the dogs are being divided into
    group_a = []
    group_b = []

    # helper function to determine whether all of the dog's dislikes are or aren't in a group
    def dislike_helper(group, index):
        for dislike in index:
            if dislike in group:
                return False
        return True

    # while the queue is not empty
    while dog_queue:
        # pop the first dog off the queue to check its relationships
        current_dog = dog_queue.popleft()
        if current_dog not in searched:
            # if the current dog being searched has no dislikes, append to list a (arbitrary)
            if dislikes[current_dog] == []:
                group_a.append(current_dog)
                # append the next dog in the graph to the queue so the loop won't exit due to an empty queue
                dog_queue.append(current_dog + 1)
            else:
                # append each dog in the current dog's dislikes to the queue to be searched
                for dog in dislikes[current_dog]:
                    dog_queue.append(dog)
                if dislike_helper(group_a, dislikes[current_dog]):
                    group_a.append(current_dog)
                elif dislike_helper(group_b, dislikes[current_dog]):
                    group_b.append(current_dog)
                else:
                    # if any of the dogs dislikes are in both lists and the dog cannot be placed without starting a fight
                    return False
            # append the dog to the searched list
            searched.append(current_dog)
    # if all the dogs can be assigned to groups with no fighting, return True
    return True

    # iterative loop using the helper function to pass 6/7 tests
    # keeping this here to for reference of my thought process before I tried using a queue

    # for i in range(len(dislikes)):
    #     if dislikes[i] == []:
    #         group_a.append(i)
    #     else:
    #         if helper(group_a, dislikes[i]):
    #             group_a.append(i)
    #         elif helper(group_b, dislikes[i]):
    #             group_b.append(i)
    #         else:
    #             return False
    # return True
