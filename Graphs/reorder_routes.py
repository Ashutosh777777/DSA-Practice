class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        forward = [[] for _ in range(n)]
        backward = [[] for _ in range(n)]

        for a, b in connections:
            forward[a].append(b)    # original road a -> b
            backward[b].append(a)   # reverse direction for traversal

        visited = [False] * n
        self.ans = 0

        def dfs(node):
            visited[node] = True

            # Roads going away from 0 side need reversal
            for neighbour in forward[node]:
                if not visited[neighbour]:
                    self.ans += 1
                    dfs(neighbour)

            # Roads already coming toward 0 side are okay
            for neighbour in backward[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        dfs(0)
        return self.ans