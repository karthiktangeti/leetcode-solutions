class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        arr = [[rStart,cStart]]
        step = 1
        c = cStart
        r = rStart
        while len(arr) < rows * cols:
            for i in range(step):
                c += 1
                if 0 <= c < cols and 0 <= r < rows:
                    arr.append([r,c])
            for i in range(step):
                r += 1
                if 0 <= c < cols and 0 <= r < rows:
                    arr.append([r,c])
            step += 1
            for i in range(step):
                c -= 1
                if 0 <= c < cols and 0 <= r < rows:
                    arr.append([r,c])
            for i in range(step):
                r -= 1
                if 0 <= c < cols and 0 <= r < rows:
                    arr.append([r,c])
            step += 1
        return arr
        