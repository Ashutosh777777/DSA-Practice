# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    entry = [0]*n
    entry[0] = a[0]
    for i in range(1, n):
        entry[i] = max(a[i], entry[i-1])
    ans = 0
    for i in range(n):
        ans += entry[i] - a[i]
    print(ans)