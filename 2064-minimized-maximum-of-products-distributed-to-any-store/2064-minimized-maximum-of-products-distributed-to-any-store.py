class Solution(object):
    def minimizedMaximum(self, n, quantities):
        l = 1
        r = max(quantities)
        while l < r:
            mid = (l + r) // 2
            stores = 0
            for q in quantities:
                stores +=  (q + mid - 1) // mid
            if stores <= n:
                r = mid
            else:
                l  = mid + 1
        return l