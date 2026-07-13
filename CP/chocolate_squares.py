import math
# cook your dish here
t = int(input())
for _ in range(t):
    l, b = map(int, input().split())
    print(math.gcd(l, b))