def sumsquare(l):
    even = []
    odd = []
    for i in range(len(l)):
        if l[i]%2==0:
            even.append(l[i])
        else:
            odd.append(l[i])
    for i in range(len(even)):
        sume = sume + even[i]**2
    for i in range(len(odd)):
        sumo = sumo + odd[i]**2

    return [sumo,sume]
    
L = eval(input())
print(sumsquare(L))