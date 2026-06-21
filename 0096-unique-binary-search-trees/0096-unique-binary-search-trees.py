class Solution(object):
    def numTrees(self, n):
        dq =[0] * (n+1)
        dq[0] = dq[1] =1
        for i in range(2,n +1):
            for j in range(1,i +1):
                dq[i] += dq[j-1]*dq[i-j]
        return dq[n]