# Leetcode 305. Number of Islands II
'''
A 2d grid map of m rows and n columns is initially filled with water.
We may perform an addLand operation which turns the water at position (row, col) into a land. 
Given a list of positions to operate, count the number of islands after each addLand operation. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
'''


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        output = []
        self.temp_size = 0
        near_by = set([])
        self.representative = {}
        
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for x, y in positions:
            if (x, y) in near_by:
                output.append(self.temp_size)
                continue
                
            near_by.add((x, y))
            self.temp_size += 1
            self.representative[(x, y)] = (x, y)
            for dx, dy in D:
                nx = x + dx
                ny = y + dy
                if (nx, ny) in near_by:
                    self.union((nx, ny), (x, y))
            output.append(self.temp_size)
        return output
    
    def union(self, point1, point2):
        representative_1 = self.find_representative(point1)
        representative_2 = self.find_representative(point2)
        if representative_1 != representative_2:
            self.temp_size -= 1
            self.representative[representative_1] = representative_2
    
    def find_representative(self, point):
        path = []
        while point != self.representative[point]:
            path.append(point)
            point = self.representative[point]
        for p in path:
            self.representative[p] = point
        return point
        