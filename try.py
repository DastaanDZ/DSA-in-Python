def gcd(c,m,n):
    print(c)
    (a,b) = (max(m,n),min(m,n))
    if a%b == 0:
        return b
    else:
        return gcd(c,b,a%b)
c=0
print(gcd(c,24,130))