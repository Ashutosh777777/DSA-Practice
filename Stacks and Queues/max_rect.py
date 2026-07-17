class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, self.largestRectangleArea(heights))

        return ans

    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        ans = 0

        for i in range(n + 1):
            cur = 0 if i == n else heights[i]

            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                ans = max(ans, h * w)

            stack.append(i)

        return ans