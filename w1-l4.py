def expanding(l):
    diffi = abs(l[1] - l[0])
    for i in range(2,len(l)):
        diffa = abs(l[i] - l[i-1])
        if diffa - diffi <= 0:
            return False
        diffi = diffa
    return True

L = eval(input())
print(expanding(L))