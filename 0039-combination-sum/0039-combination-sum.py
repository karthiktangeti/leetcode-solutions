class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(ind,target,ds):
            if ind == len(candidates):
                if target == 0:
                    res.append(ds[:])
                return 
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                dfs(ind,target- candidates[ind],ds)
                ds.pop()
            dfs(ind + 1,target,ds)
                
        dfs(0,target,[])
        return res
        