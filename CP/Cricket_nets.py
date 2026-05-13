# cook your dish here
T = int(input())
for _ in range(T):
    X = int(input())
    if X<=20:
        print(X*10)
    else:
        print(200 + ((X - 20) // 2) * 5)