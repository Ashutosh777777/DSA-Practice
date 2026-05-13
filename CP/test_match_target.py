# cook your dish here
X, Y, Z = map(int, input().split())

ans = max(0, X + Z - Y + 1)

print(ans)