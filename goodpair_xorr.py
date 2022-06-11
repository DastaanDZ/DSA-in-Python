for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    freq = {}
    for i in range(0,n):
        if (A[i]^B[i]) in freq.keys():
            freq[A[i]^B[i]] += 1
        else:
            freq[A[i]^B[i]] = 1

    ans = 0

    for i in freq.values():
        ans+=i*(i-1)//2

    print(ans)