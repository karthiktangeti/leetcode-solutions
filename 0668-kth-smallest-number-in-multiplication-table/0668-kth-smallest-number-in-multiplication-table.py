class Solution(object):
    def findKthNumber(self, m, n, k):
        l = 0
        r = m* n
        while l < r:
            count = 0
            mid = (l + r)// 2
            for i in range(1,m+1):
                count += min(mid // i,n)
            if count < k:
                l = mid + 1
            else:
                r = mid
        return l 

        