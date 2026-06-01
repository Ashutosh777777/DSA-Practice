"""
Problem: Flood Fill
Platform: LeetCode
Link: https://leetcode.com/problems/flood-fill/
Approach: DFS / Graph Traversal
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

class Solution(object):

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        r = len(image)
        c = len(image[0])

        org_color = image[sr][sc]

        if org_color == color:
            return image

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def dfs(i, j):

            if (
                i < 0 or
                j < 0 or
                i >= r or
                j >= c or
                image[i][j] != org_color
            ):
                return

            image[i][j] = color

            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                dfs(ni, nj)

        dfs(sr, sc)

        return image


# Start DFS from the given pixel sr, sc.
# Store the original color of the starting pixel.
# Change only connected cells having the same original color.
# Explore 4 directions: up, right, down, and left.
# If original color is already equal to new color, return image directly.