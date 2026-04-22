"""
Problem: Recover Palindrome
Platform: CodeChef
Link: https://www.codechef.com/START235D/problems/P2235
Approach: Check whether palindrome reconstruction is unique
Time Complexity: O(n)
Space Complexity: O(1)
"""
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    unique = True
    for i in range(n // 2):
        if s[i] == '?' and s[n - i - 1] == '?':
            unique = False
            break

    if n % 2 == 1 and s[n // 2] == '?':
        unique = False

    print("YES" if unique else "NO")

# If both mirrored characters are '?', multiple choices are possible, so answer is not unique.
# For odd length strings, a middle '?' also gives multiple possible palindromes.
# If no such ambiguous position exists, the palindrome can be reconstructed uniquely.
# Scan only half the string, so the solution runs in O(n) time.