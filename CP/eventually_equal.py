from math import gcd
# cook your dish here
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b:
        print(0)
    elif gcd(a, c) == gcd(b, c):
        print(1)

    elif gcd(a, c + 1) == gcd(b, c + 1):
        print(2)

    else:
        print(3)