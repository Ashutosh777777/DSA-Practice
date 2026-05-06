"""
Problem: Election
Platform: CodeChef
Link: https://www.codechef.com/START237D/problems/ELECTION1
Approach: Majority Seats Calculation
Time Complexity: O(1)
Space Complexity: O(1)
"""

N, K = map(int, input().split())

required = (N // 2) + 1

if K < required:
    print(required - K)
else:
    print(0)

# A party needs strict majority = floor(N/2) + 1 seats.
# Calculate minimum seats required for majority.
# If current seats are less than required, print deficit.
# Otherwise, party already has majority → print 0.