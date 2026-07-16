class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3) * 3 + (j // 3)].add(board[i][j])

        def dfs(idx):
            if idx == len(empty):
                return True

            i, j = empty[idx]
            b = (i // 3) * 3 + (j // 3)

            for num in "123456789":
                if num in rows[i] or num in cols[j] or num in boxes[b]:
                    continue

                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                boxes[b].add(num)

                if dfs(idx + 1):
                    return True

                board[i][j] = "."
                rows[i].remove(num)
                cols[j].remove(num)
                boxes[b].remove(num)

            return False

        dfs(0)