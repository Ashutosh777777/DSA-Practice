# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    flag = False

    for i in range(n-3):
        if "a" not in s[i:i+4] and "e" not in s[i:i+4] and "i" not in s[i:i+4] and "o" not in s[i:i+4] and "u" not in s[i:i+4]:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")
    