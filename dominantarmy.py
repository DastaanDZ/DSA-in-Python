t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    n.sort()
    if (n[0]+n[1])<n[2]:
        print('YES')
    else:
        print('NO')