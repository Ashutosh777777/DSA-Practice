# cook your dish here
t = int(input())
for _ in range(t):
    r, y = map(int, input().split())
    if r>y:
        print(r)
    else:
        print(r + (y-r)//2)