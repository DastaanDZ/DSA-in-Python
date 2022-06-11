from turtle import distance


def primlist(Wlist):
    infinity = 1+ max([d for u in Wlist.keys()
    for (v,d) in Wlist[u]])

    (visited,distance, nbr) = ({},{},{})

    for v in Wlist.keys():
        (visited[v],distance[v],nbr[v]) = (False, infinity,-1)
    visited[0] = True

    for(v,d) in Wlist[0]:
        (distance[v],nbr[v]) = (d,0)

    for i in range(len(1,Wlist.keys())):
        nextd = min([distance[v] for v in Wlist.keys()
        if not visited[v]])

        nextvlist = min([v for v in Wlist.keys()
        if (not visited[v]) and distance[v] == nextd])

        visited[nextv] = True
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                if d < distance[v]:
                    distance[v] = d
                    nbr[v] = nextv
    

        if nextv is None:
            break
        nextv = min(nextvlist)
        visited[nextv] = True
        
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                (distance[v],nbr[v]) = (min(distance[v],d), nextv)
    return (nbr)
    