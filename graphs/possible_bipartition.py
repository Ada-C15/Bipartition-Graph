# Can be used for BFS
from collections import deque 


    


def possible_bipartition(dislikes):
    
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: O(Nodes + Edges) 
          - Every edge for a dog starting with the first dog and exploring all edges. Edges are only expored once and all nodes must be
          colored.
        Space Complexity: O(Nodes + Edges)
         - The adjacency list has O + E space complexity. Each node and edge requires an array or list space, but it is
         not squre when stored in 2 dimensions.
    """

    if not dislikes:
        return True  

    color = {}
    for i in range(len(dislikes)):
        
        if i not in color:
            # Implement a stack for the marked path
            color[i] = 0
            stack = [(i, 0)]
            while stack:
                node, paint = stack.pop() # Remove from stack, "marked" for coloring.  
                dog = dislikes[node]
                for enemy in dog:
                    if enemy in color:
                        if color[enemy] != (paint+1)%2:
                            return False
                    else:
                        stack.append((enemy, (paint+1)%2))
                        color[enemy] = (paint+1)%2                   
    return True


    
    
    
    
    
    
    
    
    
    






