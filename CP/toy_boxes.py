# cook your dish here
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    
    a = sorted(w)
    
    s = sum(a)

    x = sum(a[:k])
    y = sum(a[n-k:])

    print(max(abs(s - 2*x), abs(s - 2*y)))