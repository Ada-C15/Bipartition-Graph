# Can be used for BFS
from collections import deque 
from pprint import pprint

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bi-partitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(nm)
        Space Complexity: O(n)
    """
    if not dislikes:
        return True

    dislikes_graph = {}
    for index, value in enumerate(dislikes):
        if index not in dislikes_graph:
            dislikes_graph[index] = value
        else:
            dislikes_graph[index] += value     
    pprint(dislikes_graph)

    visited = set()
    red = set()
    green = set()

    dogs_queue = deque()

    for i in range(len(dislikes_graph)):  # if graph nodes are not connected
        if i in visited:
            continue
        
        dogs_queue.append((i, "red"))   # target color/ add it to queue

        while dogs_queue:
            dog, pen = dogs_queue.popleft()  # process dog
            visited.add(i)   # once dog processed
            
            # if we've seen this dog before and it's in the opposite pen already
            if dog in red and pen == "green":
                return False
            elif dog in green and pen == "red":
                return False
            
            if dog not in red and dog not in green:  # haven't separated dog
                if pen == "green":
                    green.add(dog)  
                    visited.add(dog)
                    
                elif pen == "red":         
                    red.add(dog)   
                    visited.add(dog)
                    
                # process neighboors of dog / putting dislike dogs in opposite pen   
                for neighbor in dislikes_graph[dog]:  
                    if neighbor not in red and neighbor not in green:
                        if pen == "red":  # opposite pen!
                            dogs_queue.append((neighbor, "green"))
                        elif pen == "green":
                            dogs_queue.append((neighbor, "red"))

    return True
