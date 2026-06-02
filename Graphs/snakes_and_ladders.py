"""
Problem: Snakes and Ladders
Platform: LeetCode
Link: https://leetcode.com/problems/snakes-and-ladders/
Approach: BFS / Shortest Path on Board
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from typing import List
from collections import deque

class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        # connection[i] stores where cell i leads to
        # -1 means normal cell
        connection = [-1] * (n * n + 1)

        node = 1
        left_to_right = True

        # Convert 2D board into 1D cell numbering
        for i in range(n - 1, -1, -1):

            if left_to_right:

                for j in range(n):

                    if board[i][j] != -1:
                        connection[node] = board[i][j]

                    node += 1

            else:

                for j in range(n - 1, -1, -1):

                    if board[i][j] != -1:
                        connection[node] = board[i][j]

                    node += 1

            left_to_right = not left_to_right

        # Build graph
        graph = {}

        for i in range(1, n * n + 1):

            graph[i] = []

            for dice in range(1, 7):

                nbr = i + dice

                if nbr <= n * n:

                    if connection[nbr] != -1:
                        graph[i].append(connection[nbr])

                    else:
                        graph[i].append(nbr)

        # BFS for shortest path
        q = deque()
        visited = [False] * (n * n + 1)

        q.append(1)
        visited[1] = True

        level = 0

        while q:

            size = len(q)

            for _ in range(size):

                pos = q.popleft()

                if pos == n * n:
                    return level

                for nbr in graph[pos]:

                    if not visited[nbr]:
                        visited[nbr] = True
                        q.append(nbr)

            level += 1

        return -1


# Convert the 2D snake-ladder board into 1D cell numbering.
# Numbering starts from bottom-left and alternates direction each row.
# For every cell, try all dice values from 1 to 6.
# If destination has snake or ladder, move to its connected cell.
# Use BFS because each dice throw counts as one move.
# First time we reach cell n*n gives the minimum number of moves.