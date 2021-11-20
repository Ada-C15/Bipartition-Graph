# Can be used for BFS
from collections import deque 
# doubly ended queue > list because append and pop are O(1)

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    pen_a = set()
    pen_b = set()

    # I referenced the solutions shared by Sid and Jen
    # during Thursdays at Ada and read GeekForGeeks to
    # supplement my understanding of the solution

    # if the the list is empty
    if not dislikes:
        return True

    # indexes represent whether or not nodes have been visited
    visited = [False] * len(dislikes)

    q = deque()
    # add first index to q/deque
    # q=([0])
    q.append(0)

    # while there is a value in the deque
    while q:

        # popleft() used to delete an argument from left end of deque
        # current = 0
        current = q.popleft()

        # mark node as visited in initial list
        visited[current] = True

        # does current dog have dislikes?
        # go to dislikes to read nested list at index 0
        if not dislikes[current]:
            # if no disikes, add 1 (next index) to deque
            q.append(current+1)
        
        # otherwise, for every dog in this nested list of dislikes
        for dog in dislikes[current]:
            
            # if node has not been visited append to deque
            # meaning, that index will read False
            if not visited[dog]:
                # add to deque
                q.append(dog)

            # if dog (we are placing) is not in pen_a
            if current not in pen_a:

                # if enemy-dog is in pen_b
                if dog in pen_b:
                    return False
                
                # add enemy-dog to pen_a
                pen_a.add(dog)

            else:
                
                # if enemy-dog is in pen_a
                if dog in pen_a:
                    return False

                # add enemy-dog to pen_b
                pen_b.add(dog)
        
    return True
    


    # for dog_index in range(len(dislikes)):

    #     print("PEN A: ", dog_index, " - ", pen_a)
    #     print("PEN B: ", dog_index, " - ",  pen_b)

    #     danger_in_a = False
    #     danger_in_b = False

    #     for enemy in dislikes[dog_index]:

    #         if enemy in pen_a:
    #             danger_in_a = True
    #         elif enemy in pen_b:
    #             danger_in_b = True
        
    #     if danger_in_a == False:
    #         pen_a.add(dog_index)
    #     elif danger_in_b == False:
    #         pen_b.add(dog_index)
    #     else:
    #         return False

    #     print("PEN A: ", pen_a)
    #     print("PEN B: ", pen_b)
    #     print()

    # return True





