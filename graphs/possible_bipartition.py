# Can be used for BFS
from collections import deque 

# does breadth first search(BFS)
def partition_helper(visited, dislikes, starting_dog):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N + E)
            Since you will visit each node once, and loop through each of the edges in each node the Big-O of this algorithm is O(N + E) where N is the number of nodes in the graph and E is the number of edges since each node and each edge will be explored.
        Space Complexity: O(n)
            In the worst-case you will need to add each node to the Queue, so the space complexity is O(N) where N is the number of nodes in the graph.
    """  
    queue = deque()
    queue.append(starting_dog)
    # visited holds all the nodes.  It is set to false at beginning indicating it has not been visited 
    visited[starting_dog] = "group_1"
    if not dislikes[starting_dog]:
        return True
    while queue:
        
        current_dog = queue.popleft()
        # dislikes[current_dog] has value of dogs that the current dog doesn't like 
        for enemy_dog in dislikes[current_dog]:
            # don't want to compare current dog to itself
            #assign other dogs to other group if not assigned 
            # if not assigned/visited/they have value false
            # append the dogs that have not been visited to the queue
            if visited[enemy_dog] == False:
                queue.append(enemy_dog)
                # check current dog's group and assign the enemy dog the opposite group
                if visited[current_dog] == "group_1":
                    visited[enemy_dog] = "group_2" 
                elif visited[current_dog] == "group_2":
                    visited[enemy_dog] = "group_1"
            #check if current dogs group matches the enemy dog's group
            elif visited[current_dog] == visited[enemy_dog]:
                return False
    return True

    
def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(N)
        Space Complexity: O(N)
    """  
    # if empty array return True
    if not dislikes:
        return True
        

    visited = [False] * ((len(dislikes)+1))
    # return partition_helper(visited,dislikes, 0)
    
    for i in range(len(dislikes)):
        #dislike[i] i is not connected to any other node empty list for adjacency 7.  [] means it has no adjacencey. dog i does not dislike any other dog or you have visited dog you skip it.  
        if not visited[i]:
            #continue means you skip.return flow to the start of the loop while break is exit the loop
            # continue
        # i index of the dogs, breadth first search (done with queue)  i nodes of the dog 
            result = partition_helper(visited,dislikes, i)
            if not result:
                return False 
    return True

