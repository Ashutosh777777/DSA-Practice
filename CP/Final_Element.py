"""
Problem: Final Element
Platform: CodeChef
Link: https://www.codechef.com/
Approach: Simulation using XOR Array Reduction
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    while len(A) > 1:
        B = []

        for i in range(len(A) - 1):
            B.append(A[i] ^ A[i + 1])

        A = B

    print(A[0])

# Create a new array using XOR of adjacent elements.
# Replace original array with the new reduced array.
# Repeat until only one element remains.
# Final remaining element is the answer.