def checkIfPossible(N,l1,l2):

    for i in range(N):
        if l1[i] not in l2:
            return(False)
    return(True)

def convertToInt(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return(l)
n = int(input())
for i in range(n):
    (tr,dr,ts,ds) = ([],[],[],[])
    (Ntr,tr,Ndr,dr,Nts,ts,Nds,ds) = (int(input()),convertToInt(input().split(' ')),int(input()),convertToInt(input().split(' ')),int(input()),convertToInt(input().split(' ')),int(input()),convertToInt(input().split(' ')))
    # print(Ntr,tr,Ndr,dr,Nts,ts,Nds,ds)


    if(checkIfPossible(Nts,ts,tr) and checkIfPossible(Nds,ds,dr)):
        print('yes')
    else:
        print('no')