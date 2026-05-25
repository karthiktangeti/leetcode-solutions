import sys
from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        cols = len(grid[0])
        rows = len(grid)
        distance = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 1
        queue = deque()
        queue.append([1,0,0])
        while len(queue):
            dist,i,j = queue.popleft()
            for x,y in [[1,0],[0,1],[-1,1],[1,-1],[1,1],[-1,-1],[0,-1],[-1,0]]:
                new_i,new_j = x + i, y + j
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] == 1:
                    continue
                dist_trev = dist + 1
                if dist_trev < distance[new_i][new_j]:
                    distance[new_i][new_j] = dist_trev
                    queue.append([dist_trev,new_i,new_j])
        if distance[rows - 1][cols - 1] == sys.maxsize:
            return -1
        return distance[rows - 1][cols - 1]