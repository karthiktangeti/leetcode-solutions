class Solution(object):
    def findDegrees(self, matrix):
        n = len(matrix)
        arr = []
        for i in range(n):
            arr.append(sum(matrix[i]))
        return arr
        