class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not len(board):
            return board

        h = len(board)
        w = len(board[0])

        if h == 1 or w == 1:
            return board

        # DFS寻找所有边界连通的 O, 使之为 -
        def dfs_flip(y,x, board):
            if board[y][x] != "O":
                return 0
            if board[y][x] == "O":
                board[y][x] = "-"
            if y+1 < h and board[y+1][x] == "O":
                dfs_flip(y+1,x,board)
            if y-1 >= 0 and board[y-1][x] == "O":
                dfs_flip(y-1,x,board)
            if x+1 < w and board[y][x+1] == "O":
                dfs_flip(y,x+1,board)
            if x-1 >= 0 and board[y][x-1] == "O":
                dfs_flip(y,x-1,board)

        # 从边界开始进行DFS
        for i in range(0,h):
            if board[i][0] == "O":
                dfs_flip(i, 0, board)
            if board[i][w-1] == "O":
                dfs_flip(i, w-1, board)
        for j in range(0,w):
            if board[0][j] == "O":
                dfs_flip(0, j, board)
            if board[h-1][j] == "O":
                dfs_flip(h-1,j,board)

        # 所有不与边界连通的 O 区域变成 X，所有 - 变成 O
        for y in range(0, len(board)):
            row = board[y]
            for x in range(0, len(board[0])):
                item = row[x]
                if item == 'O':
                    board[y][x] = 'X'
                if item == '-':
                    board[y][x] = 'O'
