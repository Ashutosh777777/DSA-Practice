# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = 0
    for i in range(n-1):
        m = max(m, min(a[i], a[i+1]))
    print(m)