# cook your dish here
t = int(input())
for _ in range(t):
    N, X, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    freq = {}
    for score in A:
        freq[score] = freq.get(score, 0) + 1

    scores = sorted(freq.keys(), reverse=True)
    eligible = 0

    for i in range(min(K, len(scores))):
        eligible += freq[scores[i]]
    print(min(eligible, X))