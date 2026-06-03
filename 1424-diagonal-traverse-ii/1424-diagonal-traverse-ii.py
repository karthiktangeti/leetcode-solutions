class Solution(object):
    def findDiagonalOrder(self, nums):
        n = len(nums)
        dist = {}
        arr = []
        for i in range(n):
            m = len(nums[i])
            for j in range(m):
                k = i + j
                if k not in dist:
                    dist[k] = []
                dist[k].append(nums[i][j])
            
        for i in sorted(dist.keys()):
            j = len(dist[i]) - 1
            while j >= 0:
                arr.append(dist[i][j])
                j -= 1
        return arr
            

                
        