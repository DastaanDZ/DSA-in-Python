# cook your dish here
t=int(input())
for _ in range(t):
    n,m,x=list(map(int,input().split()))
    n,m,x = list(map(int, input.split()))
    array=list(map(int,input().split()))
    print(n,m,x,array)
    arr=[]
    for i in range(n):
        arr.append([array[i],i])
    print('unsorted arr',arr)
    arr.sort()
    print('sorted arr',arr)
    i=n-1
    ans=[]
    while arr[i][0]>=m and i>=0:
        ans.append(arr[i][1])
        i-=1
    print('ans',ans)
    if len(ans)>=x:
        ans.sort()
        print(len(ans),end=" ")
        for i in ans:
            print(i+1,end=" ")
        print('')
    
    
    else:
        while len(ans)!=x:
            ans.append(arr[i][1])
            i-=1
        ans.sort()
        print(len(ans),end=" ")
        for i in ans:
            print(i+1,end=" ")
        print('')
            