"""
Problem: Contest Registration Fee
Platform: CodeChef
Link: https://www.codechef.com/START235D/problems/P1235
Approach: Direct condition check
Time Complexity: O(1)
Space Complexity: O(1)
"""
X, Y = map(int, input().split())
if Y > X:
    print(100)
else:
    print(0)

# First X users register for free, so check whether Alice is within that range.
# If Y <= X, Alice pays 0 because her registration is free.
# Otherwise, she registers after the free limit and pays 100.
# This is a direct one-condition problem with constant time complexity.