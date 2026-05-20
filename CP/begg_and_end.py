# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = float("inf")
    
    for i in range(n):
        for j in range(i+1, n):
            if a[i]==a[j]:
                cost = i+(n-1-j)
                ans = min(ans, cost)
    
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)