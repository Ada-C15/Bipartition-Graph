def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(n)
        Space Complexity: O(n)
        DFS
    """
    dogs = len(dislikes)
    if dogs == 0:
        return True
    graph = {dog:dislikes[dog] for dog in range(0,len(dislikes))} 
    sets_visited = [None]*(dogs)
    
    for i in range(dogs):

            if sets_visited[i] == None:
                if not search(graph, sets_visited, i, True): return False

    return True
    
def search(graph, sets, vertex, set):
            
            if sets[vertex] == None:
                sets[vertex] = set
                return all(search(graph, sets, neighbor, not set) for neighbor in graph[vertex])

            return sets[vertex] == set
    

