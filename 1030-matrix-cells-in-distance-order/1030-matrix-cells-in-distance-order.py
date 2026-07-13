class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        arr =[]
        for r in range(rows):
            for c in range(cols):
                destance = abs(r - rCenter) + abs(c - cCenter)
                arr.append((destance,[r,c]))
        arr.sort()
        ans = []
        for d,c in arr:
            ans.append(c)
        return ans
        