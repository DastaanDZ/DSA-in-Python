s = input()

for i in range(len(s)):
    (s[i][0], s[i][1]) = (s[i][1], s[i][0])
print(s)
