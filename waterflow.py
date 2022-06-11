def waterflow(w,x,y,z):
    remaining  = x-w
    if remaining > y*z:
        return('unfilled')
    elif remaining == y*z:
        return('filled')
    else:
        return('overflow')

t = int(input())
for i in range(t):
    w,x,y,z= list(map(int, input().split()))
    print(waterflow(w,x,y,z))