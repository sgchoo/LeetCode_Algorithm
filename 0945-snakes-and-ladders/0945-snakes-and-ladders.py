class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque
        n = len(board)

        def GetCurPosition(square):
            r, c = divmod(square, n)
            if c == 0 and r % 2 != 0:
                return n - r, n - 1 - c
            elif c == 0 and r % 2 == 0:
                return n - r, c
            elif c != 0 and r % 2 != 0:
                return n - r - 1, n - c
            elif c != 0 and r % 2 == 0:
                return n - r - 1, c - 1
            
            
        visited = set()
        que = deque()
        que.append((1, 0))

        while que:
            square, step = que.popleft()
            r, c = GetCurPosition(square)
            
            if board[r][c] != -1:
                square = board[r][c]
            if square == n*n:
                return step
            for dist in range(1, 7):
                new_square = square + dist
                if new_square <= n*n and new_square not in visited:
                    visited.add(new_square)
                    que.append((new_square, step + 1))
                    
        return -1