"""
Problem: Balanced Positions in a Permutation
Platform: CodeChef
Link: https://www.codechef.com/START235D/problems/P3235
Approach: Brute Force counting for each index
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    count = 0

    for i in range(n):
        left = 0
        right = 0

        for j in range(i):
            if p[j] < p[i]:
                left += 1

        for j in range(i + 1, n):
            if p[j] > p[i]:
                right += 1

        if left == right:
            count += 1

    print(count)

# For each position, count smaller elements on the left and greater elements on the right.
# If both counts are equal, that position is balanced.
# Uses two inner loops for every index to compute the required values directly.
# Simple brute-force solution with O(n^2) time complexity.