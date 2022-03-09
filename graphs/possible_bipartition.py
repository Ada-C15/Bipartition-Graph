# Can be used for BFS
from collections import deque
from pickle import FALSE 

def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        
        Time Complexity: O(1) to access the adjacency list, o(1) to iterate through the dog_dict hash map used to 
        organize the dislikes data into a more accessible format(w/out empty indices), o(n) to iterate through each value list of the 
        dictionary, which is dependent on the size of the input. 
        
        Space Complexity: O(n) for new varaibles created (visited list, dictionary) b/c the space occupied is dependent on the input. 
        O(E) for the adjacency list because each node in the dislikes array has a list of edges. 
    """
    
    #number of nodes/dogs
    num_dogs = len(dislikes)

    #if adjacency list is empty == True
    if num_dogs == 0:
        return True
    
    # # #You could put dislikes into an adjacecny dictionary to get rid of all empty values....
    dog_dict = { i : dislikes[i] for i in range(0, len(dislikes)) if len(dislikes[i]) != 0}
    
    #Set a value for a start node/dog to 1 b/c there is not always a dog 0
    current_dog = 0
    
    #track whether node has been vistited
    dogs_visited = [False for i in range(num_dogs)]
    
    #set start dog as visited in dog_visited
    dogs_visited[current_dog] = True
    
    # create a queue to do BFS and enqueue source vertex
    dogs_q = deque()
    dogs_q.append(current_dog)
    
    groupA =[]
    groupB =[]
    groupA.append(current_dog)
    
    while dogs_q:
        
        current_dog = dogs_q.pop()
        
        for dog, dislike in dog_dict.items():
            
            for dis in dislike:
                
                if dis not in dogs_visited:
                    dogs_visited[dis] = True
                    dogs_q.append(dis)
                    
                if dog in groupA and dog in groupB:
                    return False
                
                if dog not in groupA and dog not in groupB:
                    groupA.append(dis)
                
                elif dog in groupA and dog not in groupB:
                    groupB.append(dis)
                    
                        
                elif dog in groupB and dog not in groupA:
                    groupA.append(dis)   
            
        return True
    
        