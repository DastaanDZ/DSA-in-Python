def shuffle(l1,l2):
    l3 = []
    while l1 and l2:
        l3.append(l1.pop(0))
        l3.append(l2.pop(0))
    if l1:
        l3.extend(l1)
    if l2:
        l3.extend(l2)
    return l3

L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))