from collections import defaultdict
class Solution(object):
    def diagonalSort(self, mat):
        n = len(mat)
        m = len(mat[0])
        des = defaultdict(list)
        for i in range(n):
            for j in range(m):
                des[i - j].append(mat[i][j])
        for k in des:
            des[k].sort()
        for i in range(n):
            for j in range(m):
                mat[i][j] = des[i - j].pop(0)
        return mat

        