# Leetcode 130. Surrounded Region
'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''



class Solution(object):
    # BFS and searching the connected points 
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        # step 1: flipping all 'O' at the edge into 'W'
        from collections import deque
        que = deque()
        visited = set([])
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j] == 'O':
                        board[i][j] = 'W'
                        que.append([i, j])
                        visited.add((i, j))
        
        # step 2: BFS starting from all 'W' and searching for any connected 'O' and flipping them into 'W'  
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while que:
            cur_x, cur_y = que.popleft()
            for dx, dy in D:
                nx = cur_x + dx
                ny = cur_y + dy
                if (0 < nx < m) and (0 < ny < n) and board[nx][ny] == 'O' and (nx, ny) not in visited:
                    board[nx][ny] = 'W'
                    que.append([nx, ny])
                    visited.add((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'W':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board