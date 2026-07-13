# cook your dish here
n = int(input())
a = list(map(int, input().split()))

pal = [[False]*n for _ in range(n)]

for i in range(n):
    pal[i][i] = True
for l in range(2, n+1):
    for i in range(n-l+1):
        j = i+l-1
        if a[i] == a[j]:
            if l == 2:
                pal[i][j] = True
            else:
                pal[i][j] = pal[i+1][j-1]
d = [float('inf')]*n

for i in range(n):
    if pal[0][i]:
        d[i] = 1
    else:
        for j in range(i):
            if pal[j+1][i]:
                d[i] = min(d[i], d[j] + 1)
print(d[-1])