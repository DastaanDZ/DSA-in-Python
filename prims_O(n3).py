from turtle import distance


def primlist(Wlist):
    infinity = 1+ max([d for u in Wlist.keys()
    for (v,d) in Wlist[u]])

    (visited,distance, treeedge) = ({},{},[])

    for v in Wlist.keys():
        (visited[v],distance[v]) = (False, infinity)

    for i in Wlist.keys():
        (mindist,nextv) = (infinity,None)
        for u in Wlist.keys():
            for (v,d) in Wlist[u]:
                if visited[u] and (not visited[v]) and d < mindist:
                    (mindist,nextv, nexte) = (d,v,(u,v))
                
        if nextv is None:
            break
        
        visited[nextv] = True
        treeedge.append(nexte)
        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                distance[v] = min(distance[v],d)
    return (treeedge,distance)
    