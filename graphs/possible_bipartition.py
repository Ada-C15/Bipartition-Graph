# Can be used for BFS
from collections import deque 




def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    
    Input: dislikes = [ [], 
                    [2, 3], <-- node 1 neighbors
                    [1, 4], <-- node 2 neighbors
                    [1], <-- node 3 neighbors
                    [2] <-- node 4 nighbors
                  ]

Outer for loop to loop through each node.
Inner loop Another loop keeps going as long as que is not empty
Inner most loop loops through the neighbors of current node 

In order to be a bipartite graph, a node cannot be in same bucket as its neighbors
Return true if it is a bipartite graph
queues --> first one in first one out enque-->deque

    """
    if not dislikes:
        return True
    
    que = deque()
    red = set()
    green = set()
    
    for node in range(len(dislikes)):
        if node not in green and node not in red:
            que.appendleft(node)
        
        while que:
            current = que.pop()
            if current not in red and current not in green:
                red.add(current)
            elif current in green:
                green.add(current)
            else:
                red.add(current)
            
            for neighbor in dislikes[node]:
                if neighbor not in red or green:
                    que.appendleft(neighbor)
                if current not in red:
                    red.add(neighbor)
                    que.pop()
                elif current not in green: 
                    green.add(neighbor) 
                    que.pop()
                else:
                    return False             
    return True
                    
        
        


