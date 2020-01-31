# Leetcode 200 Number of islands
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input:
11000
11000
00100
00011

Output: 3
'''
 



class Solution(object):
    
    '''
    # method 1: DFS we simulate a flood and it will submerge the connected land 
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # corner case:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    count += 1
                    self.dfs(grid, m, n, x, y)
        return count
    
    def dfs(self, grid, m, n, x, y):
        # exit of recursive 1: out of the boundary
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        # exit of recursive 2： water
        if grid[x][y] == '0':
            return
        
        grid[x][y] = "0"
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in D:
            nx = x + dx
            ny = y + dy
            self.dfs(grid, m, n, nx, ny)
    
    '''
    
    # method 2: Union find
    # union find 的思路如下：遍历每个所有的点，并且当这个点是陆地时，我们做 self-representative, 并且搜索附近的点，如果有相邻的则UNION 这两个 set， 通过找到各自的representative合并
    # 注意union find需要压缩路径（path compression）
    
    
    def numIslands(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        near_by = set([])
        self.representative = {}
        self.count = 0
        
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                self.count += 1
                near_by.add((i, j))
                self.representative[(i, j)] = (i, j)
                for dx, dy in D:
                    nx = i + dx
                    ny = j + dy
                    if (nx, ny) in near_by:
                        self.union((nx, ny), (i, j))
        return self.count
    
    
    def union(self, point1, point2):
        representative_1 = self.find_representative(point1)
        representative_2 = self.find_representative(point2)
        if representative_1 != representative_2:
            self.count -= 1
            self.representative[representative_1] = representative_2

    def find_representative(self, point):
        path = []
        while point != self.representative[point]:
            path.append(point)
            point = self.representative[point]
        for p in path:
            self.representative[p] = point
        
        return point
   