# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    b = input()
    i = 0
    while i<min(n, m) and (a[i] == b[i]):
        i+=1
    print(a[:i])