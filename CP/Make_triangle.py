"""
Problem: Make Triangle
Platform: CodeChef
Link: https://www.codechef.com/START237D/problems/MAKETRIANGLE
Approach: Triangle Inequality + Minimum Increments
Time Complexity: O(1)
Space Complexity: O(1)
"""

T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())

    largest = max(X, Y, Z)
    other_sum = X + Y + Z - largest

    ans = max(largest - other_sum + 1, 0)
    print(ans)

# For a non-degenerate triangle, sum of two smaller sides must be > largest side.
# Only the largest side condition matters after finding max side.
# If other_sum > largest, triangle is already valid → 0 moves.
# Otherwise, increase smaller sides until other_sum becomes largest + 1.