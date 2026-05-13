# cook your dish here
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    if N % 3 != 2:
        print(-1)
    else:
        ans = []
        p = [1, 1, 0, M - 1, M - 1, 0]

        for i in range(N):
            ans.append(p[i % 6])

        print(*ans)