def DishPrepareOrder(order):
    order.sort()
    o = []
    countd = []
    for dish in order:
        if [order.count(dish), dish] not in o:
            o.append([order.count(dish), dish])
        if order.count(dish) not in countd:
            countd.append(order.count(dish))
    # print(o)
    countd.sort(reverse=True)
    # print(countd)
    ans = []
    itr=0
    i=0
    while(i<len(o) and itr<len(countd)):
        if o[i][0] == countd[itr]:
            ans.append(o[i][1])
        if i==len(o)-1:
            itr += 1
            i=-1
        i+=1
    return(ans)
            

# order = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]
print(DishPrepareOrder(order))