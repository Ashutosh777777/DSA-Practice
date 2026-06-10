# cook your dish here
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    score = [0]*n
    direction = 1
    player = 0
    for card in range(k, 0, -1):
        score[player] += card
        
        if direction == 1:
            if player == n-1:
                direction=-1
            else:
                player+=1
        else:
            if player == 0:
                direction = 1
            else:
                player -= 1
    print(score[0])