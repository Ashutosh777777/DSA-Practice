# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    tar = a[0]+ a[n-1]
    possible = True
    
    for i in range(n//2):
        if a[i] + a[n-1-i] != tar:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("no")