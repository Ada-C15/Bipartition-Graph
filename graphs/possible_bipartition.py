
def possible_bipartition(dislikes):
    """ Will return True or False if the given graph
        can be bipartitioned without neighboring nodes put
        into the same partition.
        Time Complexity: ?
        Space Complexity: ?
    """
    if len(dislikes)<=1:
        return True

    dislikes = [x for x in dislikes if len(x)>=2]
    # print(dislikes)

    my_set = set([item for sublist in dislikes for item in sublist])
    # print(my_set)

    n = len(my_set)
    dic = dict()
    for num in my_set:
        dic[num]=[]
    for num in my_set:
        for i in range(len(dislikes)):
            if num in dislikes[i]:
                for n in dislikes[i]:
                    if n!= num:
                        dic[num].append(n)
    print(dic)

    
    colors = [0 for _ in range(n+1)]
    print(colors) 
    
    def helper( person_id, group_num ):
        colors[person_id] = 1
        for the_other in dic[ person_id ]:
            if colors[the_other] == group_num :
                return False
            if colors[the_other] == 0 and (not helper(the_other, -1)):
                return False
        return True
        
    for person_id in range(1, n+1):
        if colors[person_id] == 0 and (not helper( person_id, 1)):
            return False 
    return True