"""
Problem: Dividing Candies
Platform: CodeChef
Link: https://www.codechef.com/START237D/problems/DIVKIDS
Approach: Linear Search for Maximum Divisible Jar
Time Complexity: O(n)
Space Complexity: O(1)
"""

T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0

    for num in A:
        if num % X == 0:
            ans = max(ans, num)

    print(ans)

# Chef can choose only jars whose candies are divisible by X.
# Check every jar one by one.
# Keep the maximum jar value that is divisible by X.
# If no valid jar exists, ans remains 0.