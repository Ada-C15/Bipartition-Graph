def possible_bipartition(dislikes):
    #bipartite if its vertex set V can be partitioned into two sets, 
    #X and Y, such that each hyperedge(dislikes given in this problem are the edges) meets a vertex in both X and Y groups
    #each edge contains exactly one vertex of X group and one vertex of Y group, 
    #so e.g. X can be colored blue and Y can be colored yellow and no edge is monochromatic.
    #can also test if it does not have a cycle of an odd length. 
    #Measuring the cycles is difficult to solve in polynomial time. 
    #common algorithms to solve for 2-colorability in testing for bipartite (directed/undirected):
    #DFS uses stack(last in, first out) <-solution below mirrors DFS
    #BFS uses a queue(first in, first out)
    #similar time complexity for both:
    #time complexity: O(dislikes)
    #space complexity: O(dogs*dislikes)
    dogs = len(dislikes)
    if dogs == 0:
        return True
    graph = {dog:dislikes[dog] for dog in range(0,len(dislikes))} #adjacency list
    sets_visited = [None]*(dogs) #X = True, Y = False, "not visited" = None
    
    for i in range(dogs):

            if sets_visited[i] == None:
                if not search(graph, sets_visited, i, True): return False

    return True
    
def search(graph, sets, vertex, group):
            
            if sets[vertex] == None:
                sets[vertex] = group
                neighbors = set()
                for neighbor in graph[vertex]:
                    neighbor_works = search(graph, sets, neighbor, not group)
                    neighbors.add(neighbor_works)
                return all(neighbors) #returns True if all True, else False

            
            return sets[vertex] == group
    

    

