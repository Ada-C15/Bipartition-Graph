def possible_bipartition(dislikes):
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
    
'''
    a graph is bipartite if its vertex set V can be partitioned into two sets, 
    X and Y, such that each edge meets a vertex in both X and Y groups,
    (edges in above problem are given as dislikes)
    or, each edge contains exactly one vertex of X set and one vertex of Y set. 
    i.e X can be colored blue and Y can be colored yellow, and no edge is monochromatic.
    (can also test if it does not have a cycle of an odd length. 
    measuring the cycles is difficult to solve in polynomial time)

    Common algorithms to solve for 2-colorability in testing for bipartite (directed/undirected):
    DFS: uses stack(last in, first out) <-solution below mirrors DFS
    BFS: uses a queue(first in, first out)
    similar time complexity for both:
    time complexity: O(dislikes) O(edges)
    space complexity: O(dogs*dislikes)... O(vertices*edges)? O(edges)?
''' 

